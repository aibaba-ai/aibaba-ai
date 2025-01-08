"""**Memory** maintains Chain state, incorporating context from past runs.

**Class hierarchy for Memory:**

.. code-block::

    BaseMemory --> BaseChatMemory --> <name>Memory  # Examples: ZepMemory, MotorheadMemory

**Main helpers:**

.. code-block::

    BaseChatMessageHistory

**Chat Message History** stores the chat message history in different stores.

**Class hierarchy for ChatMessageHistory:**

.. code-block::

    BaseChatMessageHistory --> <name>ChatMessageHistory  # Example: ZepChatMessageHistory

**Main helpers:**

.. code-block::

    AIMessage, BaseMessage, HumanMessage
"""  # noqa: E501

from typing import TYPE_CHECKING, Any

from langchain._api import create_importer
from langchain.memory.buffer import (
    ConversationBufferMemory,
    ConversationStringBufferMemory,
)
from langchain.memory.buffer_window import ConversationBufferWindowMemory
from langchain.memory.combined import CombinedMemory
from langchain.memory.entity import (
    ConversationEntityMemory,
    InMemoryEntityStore,
    RedisEntityStore,
    SQLiteEntityStore,
    UpstashRedisEntityStore,
)
from langchain.memory.readonly import ReadOnlySharedMemory
from langchain.memory.simple import SimpleMemory
from langchain.memory.summary import ConversationSummaryMemory
from langchain.memory.summary_buffer import ConversationSummaryBufferMemory
from langchain.memory.token_buffer import ConversationTokenBufferMemory
from langchain.memory.vectorstore import VectorStoreRetrieverMemory
from langchain.memory.vectorstore_token_buffer_memory import (
    ConversationVectorStoreTokenBufferMemory,  # avoid circular import
)

if TYPE_CHECKING:
    from aiagentsforce_community.chat_message_histories import (
        AstraDBChatMessageHistory,
        CassandraChatMessageHistory,
        ChatMessageHistory,
        CosmosDBChatMessageHistory,
        DynamoDBChatMessageHistory,
        ElasticsearchChatMessageHistory,
        FileChatMessageHistory,
        MomentoChatMessageHistory,
        MongoDBChatMessageHistory,
        PostgresChatMessageHistory,
        RedisChatMessageHistory,
        SingleStoreDBChatMessageHistory,
        SQLChatMessageHistory,
        StreamlitChatMessageHistory,
        UpstashRedisChatMessageHistory,
        XataChatMessageHistory,
        ZepChatMessageHistory,
    )
    from aiagentsforce_community.memory.kg import ConversationKGMemory
    from aiagentsforce_community.memory.motorhead_memory import MotorheadMemory
    from aiagentsforce_community.memory.zep_memory import ZepMemory


# Create a way to dynamically look up deprecated imports.
# Used to consolidate logic for raising deprecation warnings and
# handling optional imports.
DEPRECATED_LOOKUP = {
    "MotorheadMemory": "aiagentsforce_community.memory.motorhead_memory",
    "ConversationKGMemory": "aiagentsforce_community.memory.kg",
    "ZepMemory": "aiagentsforce_community.memory.zep_memory",
    "AstraDBChatMessageHistory": "aiagentsforce_community.chat_message_histories",
    "CassandraChatMessageHistory": "aiagentsforce_community.chat_message_histories",
    "ChatMessageHistory": "aiagentsforce_community.chat_message_histories",
    "CosmosDBChatMessageHistory": "aiagentsforce_community.chat_message_histories",
    "DynamoDBChatMessageHistory": "aiagentsforce_community.chat_message_histories",
    "ElasticsearchChatMessageHistory": "aiagentsforce_community.chat_message_histories",
    "FileChatMessageHistory": "aiagentsforce_community.chat_message_histories",
    "MomentoChatMessageHistory": "aiagentsforce_community.chat_message_histories",
    "MongoDBChatMessageHistory": "aiagentsforce_community.chat_message_histories",
    "PostgresChatMessageHistory": "aiagentsforce_community.chat_message_histories",
    "RedisChatMessageHistory": "aiagentsforce_community.chat_message_histories",
    "SingleStoreDBChatMessageHistory": "aiagentsforce_community.chat_message_histories",
    "SQLChatMessageHistory": "aiagentsforce_community.chat_message_histories",
    "StreamlitChatMessageHistory": "aiagentsforce_community.chat_message_histories",
    "UpstashRedisChatMessageHistory": "aiagentsforce_community.chat_message_histories",
    "XataChatMessageHistory": "aiagentsforce_community.chat_message_histories",
    "ZepChatMessageHistory": "aiagentsforce_community.chat_message_histories",
}


_import_attribute = create_importer(__package__, deprecated_lookups=DEPRECATED_LOOKUP)


def __getattr__(name: str) -> Any:
    """Look up attributes dynamically."""
    return _import_attribute(name)


__all__ = [
    "AstraDBChatMessageHistory",
    "CassandraChatMessageHistory",
    "ChatMessageHistory",
    "CombinedMemory",
    "ConversationBufferMemory",
    "ConversationBufferWindowMemory",
    "ConversationEntityMemory",
    "ConversationKGMemory",
    "ConversationStringBufferMemory",
    "ConversationSummaryBufferMemory",
    "ConversationSummaryMemory",
    "ConversationTokenBufferMemory",
    "ConversationVectorStoreTokenBufferMemory",
    "CosmosDBChatMessageHistory",
    "DynamoDBChatMessageHistory",
    "ElasticsearchChatMessageHistory",
    "FileChatMessageHistory",
    "InMemoryEntityStore",
    "MomentoChatMessageHistory",
    "MongoDBChatMessageHistory",
    "MotorheadMemory",
    "PostgresChatMessageHistory",
    "ReadOnlySharedMemory",
    "RedisChatMessageHistory",
    "RedisEntityStore",
    "SingleStoreDBChatMessageHistory",
    "SQLChatMessageHistory",
    "SQLiteEntityStore",
    "SimpleMemory",
    "StreamlitChatMessageHistory",
    "VectorStoreRetrieverMemory",
    "XataChatMessageHistory",
    "ZepChatMessageHistory",
    "ZepMemory",
    "UpstashRedisEntityStore",
    "UpstashRedisChatMessageHistory",
]
