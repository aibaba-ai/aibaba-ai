import json
import operator
from typing import Any, Literal, Optional, Union, cast

from pydantic import model_validator
from typing_extensions import NotRequired, Self, TypedDict

from aibaba_ai_core.messages.base import (
    BaseMessage,
    BaseMessageChunk,
    merge_content,
)
from aibaba_ai_core.messages.tool import (
    InvalidToolCall,
    ToolCall,
    ToolCallChunk,
    default_tool_chunk_parser,
    default_tool_parser,
)
from aibaba_ai_core.messages.tool import (
    invalid_tool_call as create_invalid_tool_call,
)
from aibaba_ai_core.messages.tool import (
    tool_call as create_tool_call,
)
from aibaba_ai_core.messages.tool import (
    tool_call_chunk as create_tool_call_chunk,
)
from aibaba_ai_core.utils._merge import merge_dicts, merge_lists
from aibaba_ai_core.utils.json import parse_partial_json
from aibaba_ai_core.utils.usage import _dict_int_op


class InputTokenDetails(TypedDict, total=False):
    """Breakdown of input token counts.

    Does *not* need to sum to full input token count. Does *not* need to have all keys.

    Example:

        .. code-block:: python

            {
                "audio": 10,
                "cache_creation": 200,
                "cache_read": 100,
            }

    .. versionadded:: 0.3.9
    """

    audio: int
    """Audio input tokens."""
    cache_creation: int
    """Input tokens that were cached and there was a cache miss.

    Since there was a cache miss, the cache was created from these tokens.
    """
    cache_read: int
    """Input tokens that were cached and there was a cache hit.

    Since there was a cache hit, the tokens were read from the cache. More precisely,
    the model state given these tokens was read from the cache.
    """


class OutputTokenDetails(TypedDict, total=False):
    """Breakdown of output token counts.

    Does *not* need to sum to full output token count. Does *not* need to have all keys.

    Example:

        .. code-block:: python

            {
                "audio": 10,
                "reasoning": 200,
            }

    .. versionadded:: 0.3.9
    """

    audio: int
    """Audio output tokens."""
    reasoning: int
    """Reasoning output tokens.

    Tokens generated by the model in a chain of thought process (i.e. by OpenAI's o1
    models) that are not returned as part of model output.
    """


class UsageMetadata(TypedDict):
    """Usage metadata for a message, such as token counts.

    This is a standard representation of token usage that is consistent across models.

    Example:

        .. code-block:: python

            {
                "input_tokens": 350,
                "output_tokens": 240,
                "total_tokens": 590,
                "input_token_details": {
                    "audio": 10,
                    "cache_creation": 200,
                    "cache_read": 100,
                },
                "output_token_details": {
                    "audio": 10,
                    "reasoning": 200,
                }
            }

    .. versionchanged:: 0.3.9

        Added ``input_token_details`` and ``output_token_details``.
    """

    input_tokens: int
    """Count of input (or prompt) tokens. Sum of all input token types."""
    output_tokens: int
    """Count of output (or completion) tokens. Sum of all output token types."""
    total_tokens: int
    """Total token count. Sum of input_tokens + output_tokens."""
    input_token_details: NotRequired[InputTokenDetails]
    """Breakdown of input token counts.
 
    Does *not* need to sum to full input token count. Does *not* need to have all keys.
    """
    output_token_details: NotRequired[OutputTokenDetails]
    """Breakdown of output token counts.

    Does *not* need to sum to full output token count. Does *not* need to have all keys.
    """


class AIMessage(BaseMessage):
    """Message from an AI.

    AIMessage is returned from a chat model as a response to a prompt.

    This message represents the output of the model and consists of both
    the raw output as returned by the model together standardized fields
    (e.g., tool calls, usage metadata) added by the Aibaba AI framework.
    """

    example: bool = False
    """Use to denote that a message is part of an example conversation.

    At the moment, this is ignored by most models. Usage is discouraged.
    """

    tool_calls: list[ToolCall] = []
    """If provided, tool calls associated with the message."""
    invalid_tool_calls: list[InvalidToolCall] = []
    """If provided, tool calls with parsing errors associated with the message."""
    usage_metadata: Optional[UsageMetadata] = None
    """If provided, usage metadata for a message, such as token counts.

    This is a standard representation of token usage that is consistent across models.
    """

    type: Literal["ai"] = "ai"
    """The type of the message (used for deserialization). Defaults to "ai"."""

    def __init__(
        self, content: Union[str, list[Union[str, dict]]], **kwargs: Any
    ) -> None:
        """Pass in content as positional arg.

        Args:
            content: The content of the message.
            kwargs: Additional arguments to pass to the parent class.
        """
        super().__init__(content=content, **kwargs)

    @classmethod
    def get_lc_namespace(cls) -> list[str]:
        """Get the namespace of the langchain object.

        Returns:
            The namespace of the langchain object.
            Defaults to ["langchain", "schema", "messages"].
        """
        return ["langchain", "schema", "messages"]

    @property
    def lc_attributes(self) -> dict:
        """Attrs to be serialized even if they are derived from other init args."""
        return {
            "tool_calls": self.tool_calls,
            "invalid_tool_calls": self.invalid_tool_calls,
        }

    @model_validator(mode="before")
    @classmethod
    def _backwards_compat_tool_calls(cls, values: dict) -> Any:
        check_additional_kwargs = not any(
            values.get(k)
            for k in ("tool_calls", "invalid_tool_calls", "tool_call_chunks")
        )
        if check_additional_kwargs and (
            raw_tool_calls := values.get("additional_kwargs", {}).get("tool_calls")
        ):
            try:
                if issubclass(cls, AIMessageChunk):  # type: ignore
                    values["tool_call_chunks"] = default_tool_chunk_parser(
                        raw_tool_calls
                    )
                else:
                    parsed_tool_calls, parsed_invalid_tool_calls = default_tool_parser(
                        raw_tool_calls
                    )
                    values["tool_calls"] = parsed_tool_calls
                    values["invalid_tool_calls"] = parsed_invalid_tool_calls
            except Exception:
                pass

        # Ensure "type" is properly set on all tool call-like dicts.
        if tool_calls := values.get("tool_calls"):
            updated: list = []
            for tc in tool_calls:
                updated.append(
                    create_tool_call(**{k: v for k, v in tc.items() if k != "type"})
                )
            values["tool_calls"] = updated
        if invalid_tool_calls := values.get("invalid_tool_calls"):
            updated = []
            for tc in invalid_tool_calls:
                updated.append(
                    create_invalid_tool_call(
                        **{k: v for k, v in tc.items() if k != "type"}
                    )
                )
            values["invalid_tool_calls"] = updated

        if tool_call_chunks := values.get("tool_call_chunks"):
            updated = []
            for tc in tool_call_chunks:
                updated.append(
                    create_tool_call_chunk(
                        **{k: v for k, v in tc.items() if k != "type"}
                    )
                )
            values["tool_call_chunks"] = updated

        return values

    def pretty_repr(self, html: bool = False) -> str:
        """Return a pretty representation of the message.

        Args:
            html: Whether to return an HTML-formatted string.
                 Defaults to False.

        Returns:
            A pretty representation of the message.
        """
        base = super().pretty_repr(html=html)
        lines = []

        def _format_tool_args(tc: Union[ToolCall, InvalidToolCall]) -> list[str]:
            lines = [
                f"  {tc.get('name', 'Tool')} ({tc.get('id')})",
                f" Call ID: {tc.get('id')}",
            ]
            if tc.get("error"):
                lines.append(f"  Error: {tc.get('error')}")
            lines.append("  Args:")
            args = tc.get("args")
            if isinstance(args, str):
                lines.append(f"    {args}")
            elif isinstance(args, dict):
                for arg, value in args.items():
                    lines.append(f"    {arg}: {value}")
            return lines

        if self.tool_calls:
            lines.append("Tool Calls:")
            for tc in self.tool_calls:
                lines.extend(_format_tool_args(tc))
        if self.invalid_tool_calls:
            lines.append("Invalid Tool Calls:")
            for itc in self.invalid_tool_calls:
                lines.extend(_format_tool_args(itc))
        return (base.strip() + "\n" + "\n".join(lines)).strip()


AIMessage.model_rebuild()


class AIMessageChunk(AIMessage, BaseMessageChunk):
    """Message chunk from an AI."""

    # Ignoring mypy re-assignment here since we're overriding the value
    # to make sure that the chunk variant can be discriminated from the
    # non-chunk variant.
    type: Literal["AIMessageChunk"] = "AIMessageChunk"  # type: ignore
    """The type of the message (used for deserialization).
    Defaults to "AIMessageChunk"."""

    tool_call_chunks: list[ToolCallChunk] = []
    """If provided, tool call chunks associated with the message."""

    @classmethod
    def get_lc_namespace(cls) -> list[str]:
        """Get the namespace of the langchain object.

        Returns:
            The namespace of the langchain object.
            Defaults to ["langchain", "schema", "messages"].
        """
        return ["langchain", "schema", "messages"]

    @property
    def lc_attributes(self) -> dict:
        """Attrs to be serialized even if they are derived from other init args."""
        return {
            "tool_calls": self.tool_calls,
            "invalid_tool_calls": self.invalid_tool_calls,
        }

    @model_validator(mode="after")
    def init_tool_calls(self) -> Self:
        """Initialize tool calls from tool call chunks.

        Args:
            values: The values to validate.

        Returns:
            The values with tool calls initialized.

        Raises:
            ValueError: If the tool call chunks are malformed.
        """
        if not self.tool_call_chunks:
            if self.tool_calls:
                self.tool_call_chunks = [
                    create_tool_call_chunk(
                        name=tc["name"],
                        args=json.dumps(tc["args"]),
                        id=tc["id"],
                        index=None,
                    )
                    for tc in self.tool_calls
                ]
            if self.invalid_tool_calls:
                tool_call_chunks = self.tool_call_chunks
                tool_call_chunks.extend(
                    [
                        create_tool_call_chunk(
                            name=tc["name"], args=tc["args"], id=tc["id"], index=None
                        )
                        for tc in self.invalid_tool_calls
                    ]
                )
                self.tool_call_chunks = tool_call_chunks

            return self
        tool_calls = []
        invalid_tool_calls = []
        for chunk in self.tool_call_chunks:
            try:
                args_ = parse_partial_json(chunk["args"]) if chunk["args"] != "" else {}  # type: ignore[arg-type]
                if isinstance(args_, dict):
                    tool_calls.append(
                        create_tool_call(
                            name=chunk["name"] or "",
                            args=args_,
                            id=chunk["id"],
                        )
                    )
                else:
                    msg = "Malformed args."
                    raise ValueError(msg)
            except Exception:
                invalid_tool_calls.append(
                    create_invalid_tool_call(
                        name=chunk["name"],
                        args=chunk["args"],
                        id=chunk["id"],
                        error=None,
                    )
                )
        self.tool_calls = tool_calls
        self.invalid_tool_calls = invalid_tool_calls
        return self

    def __add__(self, other: Any) -> BaseMessageChunk:  # type: ignore
        if isinstance(other, AIMessageChunk):
            return add_ai_message_chunks(self, other)
        elif isinstance(other, (list, tuple)) and all(
            isinstance(o, AIMessageChunk) for o in other
        ):
            return add_ai_message_chunks(self, *other)
        return super().__add__(other)


def add_ai_message_chunks(
    left: AIMessageChunk, *others: AIMessageChunk
) -> AIMessageChunk:
    """Add multiple AIMessageChunks together."""
    if any(left.example != o.example for o in others):
        msg = "Cannot concatenate AIMessageChunks with different example values."
        raise ValueError(msg)

    content = merge_content(left.content, *(o.content for o in others))
    additional_kwargs = merge_dicts(
        left.additional_kwargs, *(o.additional_kwargs for o in others)
    )
    response_metadata = merge_dicts(
        left.response_metadata, *(o.response_metadata for o in others)
    )

    # Merge tool call chunks
    if raw_tool_calls := merge_lists(
        left.tool_call_chunks, *(o.tool_call_chunks for o in others)
    ):
        tool_call_chunks = [
            create_tool_call_chunk(
                name=rtc.get("name"),
                args=rtc.get("args"),
                index=rtc.get("index"),
                id=rtc.get("id"),
            )
            for rtc in raw_tool_calls
        ]
    else:
        tool_call_chunks = []

    # Token usage
    if left.usage_metadata or any(o.usage_metadata is not None for o in others):
        usage_metadata: Optional[UsageMetadata] = left.usage_metadata
        for other in others:
            usage_metadata = add_usage(usage_metadata, other.usage_metadata)
    else:
        usage_metadata = None

    return left.__class__(
        example=left.example,
        content=content,
        additional_kwargs=additional_kwargs,
        tool_call_chunks=tool_call_chunks,
        response_metadata=response_metadata,
        usage_metadata=usage_metadata,
        id=left.id,
    )


def add_usage(
    left: Optional[UsageMetadata], right: Optional[UsageMetadata]
) -> UsageMetadata:
    """Recursively add two UsageMetadata objects.

    Example:
        .. code-block:: python

            from aibaba_ai_core.messages.ai import add_usage

            left = UsageMetadata(
                input_tokens=5,
                output_tokens=0,
                total_tokens=5,
                input_token_details=InputTokenDetails(cache_read=3)
            )
            right = UsageMetadata(
                input_tokens=0,
                output_tokens=10,
                total_tokens=10,
                output_token_details=OutputTokenDetails(reasoning=4)
            )

            add_usage(left, right)

        results in

        .. code-block:: python

            UsageMetadata(
                input_tokens=5,
                output_tokens=10,
                total_tokens=15,
                input_token_details=InputTokenDetails(cache_read=3),
                output_token_details=OutputTokenDetails(reasoning=4)
            )

    """
    if not (left or right):
        return UsageMetadata(input_tokens=0, output_tokens=0, total_tokens=0)
    if not (left and right):
        return cast(UsageMetadata, left or right)

    return UsageMetadata(
        **cast(
            UsageMetadata,
            _dict_int_op(
                cast(dict, left),
                cast(dict, right),
                operator.add,
            ),
        )
    )


def subtract_usage(
    left: Optional[UsageMetadata], right: Optional[UsageMetadata]
) -> UsageMetadata:
    """Recursively subtract two UsageMetadata objects.

    Token counts cannot be negative so the actual operation is max(left - right, 0).

    Example:
        .. code-block:: python

            from aibaba_ai_core.messages.ai import subtract_usage

            left = UsageMetadata(
                input_tokens=5,
                output_tokens=10,
                total_tokens=15,
                input_token_details=InputTokenDetails(cache_read=4)
            )
            right = UsageMetadata(
                input_tokens=3,
                output_tokens=8,
                total_tokens=11,
                output_token_details=OutputTokenDetails(reasoning=4)
            )

            subtract_usage(left, right)

        results in

        .. code-block:: python

            UsageMetadata(
                input_tokens=2,
                output_tokens=2,
                total_tokens=4,
                input_token_details=InputTokenDetails(cache_read=4),
                output_token_details=OutputTokenDetails(reasoning=0)
            )

    """
    if not (left or right):
        return UsageMetadata(input_tokens=0, output_tokens=0, total_tokens=0)
    if not (left and right):
        return cast(UsageMetadata, left or right)

    return UsageMetadata(
        **cast(
            UsageMetadata,
            _dict_int_op(
                cast(dict, left),
                cast(dict, right),
                (lambda le, ri: max(le - ri, 0)),
            ),
        )
    )