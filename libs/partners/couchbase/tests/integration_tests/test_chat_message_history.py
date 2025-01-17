"""Test Couchbase Chat Message History functionality"""

import os
import time
from datetime import datetime, timedelta
from typing import Any

import pytest
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions
from langchain.memory import ConversationBufferMemory
from aibaba_ai_core.messages import AIMessage, HumanMessage

from langchain_couchbase.chat_message_histories import CouchbaseChatMessageHistory
from tests.utils import fetch_document_expiry_time, get_document_keys

CONNECTION_STRING = os.getenv("COUCHBASE_CONNECTION_STRING", "")
BUCKET_NAME = os.getenv("COUCHBASE_BUCKET_NAME", "")
SCOPE_NAME = os.getenv("COUCHBASE_SCOPE_NAME", "")
MESSAGE_HISTORY_COLLECTION_NAME = os.getenv(
    "COUCHBASE_CHAT_HISTORY_COLLECTION_NAME", ""
)
USERNAME = os.getenv("COUCHBASE_USERNAME", "")
PASSWORD = os.getenv("COUCHBASE_PASSWORD", "")
SLEEP_DURATION = 0.2


def set_all_env_vars() -> bool:
    """Check if all environment variables are set"""
    return all(
        [
            CONNECTION_STRING,
            BUCKET_NAME,
            SCOPE_NAME,
            MESSAGE_HISTORY_COLLECTION_NAME,
            USERNAME,
            PASSWORD,
        ]
    )


def get_cluster() -> Any:
    """Get a couchbase cluster object"""
    auth = PasswordAuthenticator(USERNAME, PASSWORD)
    options = ClusterOptions(auth)
    connect_string = CONNECTION_STRING
    cluster = Cluster(connect_string, options)

    # Wait until the cluster is ready for use.
    cluster.wait_until_ready(timedelta(seconds=5))

    return cluster


@pytest.fixture()
def cluster() -> Any:
    """Get a couchbase cluster object"""
    return get_cluster()


@pytest.mark.skipif(
    not set_all_env_vars(), reason="Missing Couchbase environment variables"
)
class TestCouchbaseCache:
    def test_memory_with_message_store(self, cluster: Any) -> None:
        """Test chat message history with a message store"""

        message_history = CouchbaseChatMessageHistory(
            cluster=cluster,
            bucket_name=BUCKET_NAME,
            scope_name=SCOPE_NAME,
            collection_name=MESSAGE_HISTORY_COLLECTION_NAME,
            session_id="test-session",
        )

        memory = ConversationBufferMemory(
            memory_key="baz", chat_memory=message_history, return_messages=True
        )

        # clear the memory
        memory.chat_memory.clear()

        # wait for the messages to be cleared
        time.sleep(SLEEP_DURATION)
        assert memory.chat_memory.messages == []

        # add some messages
        ai_message = AIMessage(content="Hello, how are you doing ?")
        user_message = HumanMessage(content="I'm good, how are you?")
        memory.chat_memory.add_messages([ai_message, user_message])

        # wait until the messages can be retrieved
        time.sleep(SLEEP_DURATION)

        # check that the messages are in the memory
        messages = memory.chat_memory.messages
        assert len(messages) == 2

        # check that the messages are in the order of creation
        assert messages == [ai_message, user_message]

        # clear the memory
        memory.chat_memory.clear()
        time.sleep(SLEEP_DURATION)
        assert memory.chat_memory.messages == []

    def test_memory_with_separate_sessions(self, cluster: Any) -> None:
        """Test the chat message history with multiple sessions"""

        message_history_a = CouchbaseChatMessageHistory(
            cluster=cluster,
            bucket_name=BUCKET_NAME,
            scope_name=SCOPE_NAME,
            collection_name=MESSAGE_HISTORY_COLLECTION_NAME,
            session_id="test-session-a",
        )

        message_history_b = CouchbaseChatMessageHistory(
            cluster=cluster,
            bucket_name=BUCKET_NAME,
            scope_name=SCOPE_NAME,
            collection_name=MESSAGE_HISTORY_COLLECTION_NAME,
            session_id="test-session-b",
        )

        memory_a = ConversationBufferMemory(
            memory_key="a", chat_memory=message_history_a, return_messages=True
        )
        memory_b = ConversationBufferMemory(
            memory_key="b", chat_memory=message_history_b, return_messages=True
        )

        # clear the memory
        memory_a.chat_memory.clear()
        memory_b.chat_memory.clear()

        # add some messages
        ai_message = AIMessage(content="Hello, how are you doing ?")
        user_message = HumanMessage(content="I'm good, how are you?")
        memory_a.chat_memory.add_ai_message(ai_message)
        memory_b.chat_memory.add_user_message(user_message)

        # wait until the messages can be retrieved
        time.sleep(SLEEP_DURATION)

        # check that the messages are in the memory
        messages_a = memory_a.chat_memory.messages
        messages_b = memory_b.chat_memory.messages
        assert len(messages_a) == 1
        assert len(messages_b) == 1
        assert messages_a == [ai_message]
        assert messages_b == [user_message]

        # clear the memory
        memory_a.chat_memory.clear()
        time.sleep(SLEEP_DURATION)
        # ensure that only the session that is cleared is empty
        assert memory_a.chat_memory.messages == []
        assert memory_b.chat_memory.messages == [user_message]

        # clear the other session's memory
        memory_b.chat_memory.clear()
        time.sleep(SLEEP_DURATION)
        assert memory_b.chat_memory.messages == []

    def test_memory_message_with_ttl(self, cluster: Any) -> None:
        """Test chat message history with a message being saved with a TTL"""
        ttl = timedelta(minutes=5)
        session_id = "test-session-ttl"
        message_history = CouchbaseChatMessageHistory(
            cluster=cluster,
            bucket_name=BUCKET_NAME,
            scope_name=SCOPE_NAME,
            collection_name=MESSAGE_HISTORY_COLLECTION_NAME,
            session_id=session_id,
            ttl=ttl,
        )

        memory = ConversationBufferMemory(
            memory_key="baz", chat_memory=message_history, return_messages=True
        )

        # clear the memory
        memory.chat_memory.clear()

        # wait for the messages to be cleared
        time.sleep(SLEEP_DURATION)
        assert memory.chat_memory.messages == []

        # add some messages
        ai_message = AIMessage(content="Hello, how are you doing ?")
        memory.chat_memory.add_ai_message(ai_message)

        # wait until the messages can be retrieved
        time.sleep(SLEEP_DURATION)

        # check that the messages are in the memory
        messages = memory.chat_memory.messages
        assert len(messages) == 1

        # check that the messages are in the order of creation
        assert messages == [ai_message]

        # Check the document's expiry time by fetching it from the database
        fetch_documents_query = (
            f"SELECT meta().id, * from `{MESSAGE_HISTORY_COLLECTION_NAME}` doc"
            f" WHERE doc.session_id = '{session_id}'"
        )

        document_keys = get_document_keys(
            cluster=cluster,
            bucket_name=BUCKET_NAME,
            scope_name=SCOPE_NAME,
            query=fetch_documents_query,
        )
        assert len(document_keys) == 1

        # Ensure that the document will expire within the TTL

        document_expiry_time = fetch_document_expiry_time(
            cluster=cluster,
            bucket_name=BUCKET_NAME,
            scope_name=SCOPE_NAME,
            collection_name=MESSAGE_HISTORY_COLLECTION_NAME,
            document_key=document_keys[0],
        )
        current_time = datetime.now()
        assert document_expiry_time - current_time < ttl

    def test_memory_messages_with_ttl(self, cluster: Any) -> None:
        """Test chat message history with messages being stored with a TTL"""
        ttl = timedelta(minutes=5)
        session_id = "test-session-ttl"
        message_history = CouchbaseChatMessageHistory(
            cluster=cluster,
            bucket_name=BUCKET_NAME,
            scope_name=SCOPE_NAME,
            collection_name=MESSAGE_HISTORY_COLLECTION_NAME,
            session_id=session_id,
            ttl=ttl,
        )

        memory = ConversationBufferMemory(
            memory_key="baz", chat_memory=message_history, return_messages=True
        )

        # clear the memory
        memory.chat_memory.clear()

        # wait for the messages to be cleared
        time.sleep(SLEEP_DURATION)
        assert memory.chat_memory.messages == []

        # add some messages
        ai_message = AIMessage(content="Hello, how are you doing ?")
        user_message = HumanMessage(content="I'm good, how are you?")
        memory.chat_memory.add_messages([ai_message, user_message])

        # wait until the messages can be retrieved
        time.sleep(SLEEP_DURATION)

        # check that the messages are in the memory
        messages = memory.chat_memory.messages
        assert len(messages) == 2

        # check that the messages are in the order of creation
        assert messages == [ai_message, user_message]

        # Check the documents' expiry time by fetching the documents from the database
        fetch_documents_query = (
            f"SELECT meta().id, * from `{MESSAGE_HISTORY_COLLECTION_NAME}` doc"
            f" WHERE doc.session_id = '{session_id}'"
        )

        document_keys = get_document_keys(
            cluster=cluster,
            bucket_name=BUCKET_NAME,
            scope_name=SCOPE_NAME,
            query=fetch_documents_query,
        )
        assert len(document_keys) == 2

        # Ensure that each document will expire within the TTL
        for document_key in document_keys:
            document_expiry_time = fetch_document_expiry_time(
                cluster=cluster,
                bucket_name=BUCKET_NAME,
                scope_name=SCOPE_NAME,
                collection_name=MESSAGE_HISTORY_COLLECTION_NAME,
                document_key=document_key,
            )
            current_time = datetime.now()
            assert document_expiry_time - current_time < ttl
