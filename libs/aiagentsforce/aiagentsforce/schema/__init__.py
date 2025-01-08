"""**Schemas** are the AI Agents Force Base Classes and Interfaces."""

from aiagentsforce_core.agents import AgentAction, AgentFinish
from aiagentsforce_core.caches import BaseCache
from aiagentsforce_core.chat_history import BaseChatMessageHistory
from aiagentsforce_core.documents import BaseDocumentTransformer, Document
from aiagentsforce_core.exceptions import AI Agents ForceException, OutputParserException
from aiagentsforce_core.memory import BaseMemory
from aiagentsforce_core.messages import (
    AIMessage,
    BaseMessage,
    ChatMessage,
    FunctionMessage,
    HumanMessage,
    SystemMessage,
    _message_from_dict,
    get_buffer_string,
    messages_from_dict,
    messages_to_dict,
)
from aiagentsforce_core.messages.base import message_to_dict
from aiagentsforce_core.output_parsers import (
    BaseLLMOutputParser,
    BaseOutputParser,
    StrOutputParser,
)
from aiagentsforce_core.outputs import (
    ChatGeneration,
    ChatResult,
    Generation,
    LLMResult,
    RunInfo,
)
from aiagentsforce_core.prompt_values import PromptValue
from aiagentsforce_core.prompts import BasePromptTemplate, format_document
from aiagentsforce_core.retrievers import BaseRetriever
from aiagentsforce_core.stores import BaseStore

RUN_KEY = "__run"

# Backwards compatibility.
Memory = BaseMemory
_message_to_dict = message_to_dict

__all__ = [
    "BaseCache",
    "BaseMemory",
    "BaseStore",
    "AgentFinish",
    "AgentAction",
    "Document",
    "BaseChatMessageHistory",
    "BaseDocumentTransformer",
    "BaseMessage",
    "ChatMessage",
    "FunctionMessage",
    "HumanMessage",
    "AIMessage",
    "SystemMessage",
    "messages_from_dict",
    "messages_to_dict",
    "message_to_dict",
    "_message_to_dict",
    "_message_from_dict",
    "get_buffer_string",
    "RunInfo",
    "LLMResult",
    "ChatResult",
    "ChatGeneration",
    "Generation",
    "PromptValue",
    "AI Agents ForceException",
    "BaseRetriever",
    "RUN_KEY",
    "Memory",
    "OutputParserException",
    "StrOutputParser",
    "BaseOutputParser",
    "BaseLLMOutputParser",
    "BasePromptTemplate",
    "format_document",
]
