from operator import itemgetter
from typing import Any, Callable, List, Mapping, Optional, Union

from aibaba-ai-core.messages import BaseMessage
from aibaba-ai-core.output_parsers.openai_functions import JsonOutputFunctionsParser
from aibaba-ai-core.runnables import RouterRunnable, Runnable
from aibaba-ai-core.runnables.base import RunnableBindingBase
from typing_extensions import TypedDict


class OpenAIFunction(TypedDict):
    """A function description for ChatOpenAI"""

    name: str
    """The name of the function."""
    description: str
    """The description of the function."""
    parameters: dict
    """The parameters to the function."""


class OpenAIFunctionsRouter(RunnableBindingBase[BaseMessage, Any]):
    """A runnable that routes to the selected function."""

    functions: Optional[List[OpenAIFunction]]

    def __init__(
        self,
        runnables: Mapping[
            str,
            Union[
                Runnable[dict, Any],
                Callable[[dict], Any],
            ],
        ],
        functions: Optional[List[OpenAIFunction]] = None,
    ):
        if functions is not None:
            assert len(functions) == len(runnables)
            assert all(func["name"] in runnables for func in functions)
        router = (
            JsonOutputFunctionsParser(args_only=False)
            | {"key": itemgetter("name"), "input": itemgetter("arguments")}
            | RouterRunnable(runnables)
        )
        super().__init__(bound=router, kwargs={}, functions=functions)
