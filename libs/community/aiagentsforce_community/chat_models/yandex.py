"""Wrapper around YandexGPT chat models."""

from __future__ import annotations

import logging
from typing import Any, Callable, Dict, List, Optional, cast

from aiagentsforce_core.callbacks import (
    AsyncCallbackManagerForLLMRun,
    CallbackManagerForLLMRun,
)
from aiagentsforce_core.language_models.chat_models import BaseChatModel
from aiagentsforce_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
    SystemMessage,
)
from aiagentsforce_core.outputs import ChatGeneration, ChatResult
from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from aiagentsforce_community.llms.utils import enforce_stop_tokens
from aiagentsforce_community.llms.yandex import _BaseYandexGPT

logger = logging.getLogger(__name__)


def _parse_message(role: str, text: str) -> Dict:
    return {"role": role, "text": text}


def _parse_chat_history(history: List[BaseMessage]) -> List[Dict[str, str]]:
    """Parse a sequence of messages into history.

    Returns:
        A list of parsed messages.
    """
    chat_history = []
    for message in history:
        content = cast(str, message.content)
        if isinstance(message, HumanMessage):
            chat_history.append(_parse_message("user", content))
        if isinstance(message, AIMessage):
            chat_history.append(_parse_message("assistant", content))
        if isinstance(message, SystemMessage):
            chat_history.append(_parse_message("system", content))
    return chat_history


class ChatYandexGPT(_BaseYandexGPT, BaseChatModel):
    """YandexGPT large language models.

    There are two authentication options for the service account
    with the ``ai.languageModels.user`` role:
        - You can specify the token in a constructor parameter `iam_token`
        or in an environment variable `YC_IAM_TOKEN`.
        - You can specify the key in a constructor parameter `api_key`
        or in an environment variable `YC_API_KEY`.

    Example:
        .. code-block:: python

            from aiagentsforce_community.chat_models import ChatYandexGPT
            chat_model = ChatYandexGPT(iam_token="t1.9eu...")

    """

    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> ChatResult:
        """Generate next turn in the conversation.
        Args:
            messages: The history of the conversation as a list of messages.
            stop: The list of stop words (optional).
            run_manager: The CallbackManager for LLM run, it's not used at the moment.

        Returns:
            The ChatResult that contains outputs generated by the model.

        Raises:
            ValueError: if the last message in the list is not from human.
        """
        text = completion_with_retry(self, messages=messages)
        text = text if stop is None else enforce_stop_tokens(text, stop)
        message = AIMessage(content=text)
        return ChatResult(generations=[ChatGeneration(message=message)])

    async def _agenerate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[AsyncCallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> ChatResult:
        """Async method to generate next turn in the conversation.

        Args:
            messages: The history of the conversation as a list of messages.
            stop: The list of stop words (optional).
            run_manager: The CallbackManager for LLM run, it's not used at the moment.

        Returns:
            The ChatResult that contains outputs generated by the model.

        Raises:
            ValueError: if the last message in the list is not from human.
        """
        text = await acompletion_with_retry(self, messages=messages)
        text = text if stop is None else enforce_stop_tokens(text, stop)
        message = AIMessage(content=text)
        return ChatResult(generations=[ChatGeneration(message=message)])


def _make_request(
    self: ChatYandexGPT,
    messages: List[BaseMessage],
) -> str:
    try:
        import grpc
        from google.protobuf.wrappers_pb2 import DoubleValue, Int64Value

        try:
            from yandex.cloud.ai.foundation_models.v1.text_common_pb2 import (
                CompletionOptions,
                Message,
            )
            from yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2 import (  # noqa: E501
                CompletionRequest,
            )
            from yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2_grpc import (  # noqa: E501
                TextGenerationServiceStub,
            )
        except ModuleNotFoundError:
            from yandex.cloud.ai.foundation_models.v1.foundation_models_pb2 import (
                CompletionOptions,
                Message,
            )
            from yandex.cloud.ai.foundation_models.v1.foundation_models_service_pb2 import (  # noqa: E501
                CompletionRequest,
            )
            from yandex.cloud.ai.foundation_models.v1.foundation_models_service_pb2_grpc import (  # noqa: E501
                TextGenerationServiceStub,
            )
    except ImportError as e:
        raise ImportError(
            "Please install YandexCloud SDK  with `pip install yandexcloud` \
            or upgrade it to recent version."
        ) from e
    if not messages:
        raise ValueError("You should provide at least one message to start the chat!")
    message_history = _parse_chat_history(messages)
    channel_credentials = grpc.ssl_channel_credentials()
    channel = grpc.secure_channel(self.url, channel_credentials)
    request = CompletionRequest(
        model_uri=self.model_uri,
        completion_options=CompletionOptions(
            temperature=DoubleValue(value=self.temperature),
            max_tokens=Int64Value(value=self.max_tokens),
        ),
        messages=[Message(**message) for message in message_history],
    )
    stub = TextGenerationServiceStub(channel)
    res = stub.Completion(request, metadata=self.grpc_metadata)
    return list(res)[0].alternatives[0].message.text


async def _amake_request(self: ChatYandexGPT, messages: List[BaseMessage]) -> str:
    try:
        import asyncio

        import grpc
        from google.protobuf.wrappers_pb2 import DoubleValue, Int64Value

        try:
            from yandex.cloud.ai.foundation_models.v1.text_common_pb2 import (
                CompletionOptions,
                Message,
            )
            from yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2 import (  # noqa: E501
                CompletionRequest,
                CompletionResponse,
            )
            from yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2_grpc import (  # noqa: E501
                TextGenerationAsyncServiceStub,
            )
        except ModuleNotFoundError:
            from yandex.cloud.ai.foundation_models.v1.foundation_models_pb2 import (
                CompletionOptions,
                Message,
            )
            from yandex.cloud.ai.foundation_models.v1.foundation_models_service_pb2 import (  # noqa: E501
                CompletionRequest,
                CompletionResponse,
            )
            from yandex.cloud.ai.foundation_models.v1.foundation_models_service_pb2_grpc import (  # noqa: E501
                TextGenerationAsyncServiceStub,
            )
        from yandex.cloud.operation.operation_service_pb2 import GetOperationRequest
        from yandex.cloud.operation.operation_service_pb2_grpc import (
            OperationServiceStub,
        )
    except ImportError as e:
        raise ImportError(
            "Please install YandexCloud SDK  with `pip install yandexcloud` \
            or upgrade it to recent version."
        ) from e
    if not messages:
        raise ValueError("You should provide at least one message to start the chat!")
    message_history = _parse_chat_history(messages)
    operation_api_url = "operation.api.cloud.yandex.net:443"
    channel_credentials = grpc.ssl_channel_credentials()
    async with grpc.aio.secure_channel(self.url, channel_credentials) as channel:
        request = CompletionRequest(
            model_uri=self.model_uri,
            completion_options=CompletionOptions(
                temperature=DoubleValue(value=self.temperature),
                max_tokens=Int64Value(value=self.max_tokens),
            ),
            messages=[Message(**message) for message in message_history],
        )
        stub = TextGenerationAsyncServiceStub(channel)
        operation = await stub.Completion(request, metadata=self.grpc_metadata)
        async with grpc.aio.secure_channel(
            operation_api_url, channel_credentials
        ) as operation_channel:
            operation_stub = OperationServiceStub(operation_channel)
            while not operation.done:
                await asyncio.sleep(1)
                operation_request = GetOperationRequest(operation_id=operation.id)
                operation = await operation_stub.Get(
                    operation_request,
                    metadata=self.grpc_metadata,
                )

        completion_response = CompletionResponse()
        operation.response.Unpack(completion_response)
        return completion_response.alternatives[0].message.text


def _create_retry_decorator(llm: ChatYandexGPT) -> Callable[[Any], Any]:
    from grpc import RpcError

    min_seconds = llm.sleep_interval
    max_seconds = 60
    return retry(
        reraise=True,
        stop=stop_after_attempt(llm.max_retries),
        wait=wait_exponential(multiplier=1, min=min_seconds, max=max_seconds),
        retry=(retry_if_exception_type((RpcError))),
        before_sleep=before_sleep_log(logger, logging.WARNING),
    )


def completion_with_retry(llm: ChatYandexGPT, **kwargs: Any) -> Any:
    """Use tenacity to retry the completion call."""
    retry_decorator = _create_retry_decorator(llm)

    @retry_decorator
    def _completion_with_retry(**_kwargs: Any) -> Any:
        return _make_request(llm, **_kwargs)

    return _completion_with_retry(**kwargs)


async def acompletion_with_retry(llm: ChatYandexGPT, **kwargs: Any) -> Any:
    """Use tenacity to retry the async completion call."""
    retry_decorator = _create_retry_decorator(llm)

    @retry_decorator
    async def _completion_with_retry(**_kwargs: Any) -> Any:
        return await _amake_request(llm, **_kwargs)

    return await _completion_with_retry(**kwargs)
