"""Test PromptLayerChatOpenAI wrapper."""

import pytest
from aibaba_ai_core.callbacks import CallbackManager
from aibaba_ai_core.messages import BaseMessage, HumanMessage, SystemMessage
from aibaba_ai_core.outputs import ChatGeneration, ChatResult, LLMResult

from aibaba_ai_community.chat_models.promptlayer_openai import PromptLayerChatOpenAI
from tests.unit_tests.callbacks.fake_callback_handler import FakeCallbackHandler


def test_promptlayer_chat_openai() -> None:
    """Test PromptLayerChatOpenAI wrapper."""
    chat = PromptLayerChatOpenAI(max_tokens=10)  # type: ignore[call-arg]
    message = HumanMessage(content="Hello")
    response = chat.invoke([message])
    assert isinstance(response, BaseMessage)
    assert isinstance(response.content, str)


def test_promptlayer_chat_openai_system_message() -> None:
    """Test PromptLayerChatOpenAI wrapper with system message."""
    chat = PromptLayerChatOpenAI(max_tokens=10)  # type: ignore[call-arg]
    system_message = SystemMessage(content="You are to chat with the user.")
    human_message = HumanMessage(content="Hello")
    response = chat.invoke([system_message, human_message])
    assert isinstance(response, BaseMessage)
    assert isinstance(response.content, str)


def test_promptlayer_chat_openai_generate() -> None:
    """Test PromptLayerChatOpenAI wrapper with generate."""
    chat = PromptLayerChatOpenAI(max_tokens=10, n=2)  # type: ignore[call-arg]
    message = HumanMessage(content="Hello")
    response = chat.generate([[message], [message]])
    assert isinstance(response, LLMResult)
    assert len(response.generations) == 2
    for generations in response.generations:
        assert len(generations) == 2
        for generation in generations:
            assert isinstance(generation, ChatGeneration)
            assert isinstance(generation.text, str)
            assert generation.text == generation.message.content


def test_promptlayer_chat_openai_multiple_completions() -> None:
    """Test PromptLayerChatOpenAI wrapper with multiple completions."""
    chat = PromptLayerChatOpenAI(max_tokens=10, n=5)  # type: ignore[call-arg]
    message = HumanMessage(content="Hello")
    response = chat._generate([message])
    assert isinstance(response, ChatResult)
    assert len(response.generations) == 5
    for generation in response.generations:
        assert isinstance(generation.message, BaseMessage)
        assert isinstance(generation.message.content, str)


def test_promptlayer_chat_openai_streaming() -> None:
    """Test that streaming correctly invokes on_llm_new_token callback."""
    callback_handler = FakeCallbackHandler()
    callback_manager = CallbackManager([callback_handler])
    chat = PromptLayerChatOpenAI(  # type: ignore[call-arg]
        max_tokens=10,
        streaming=True,
        temperature=0,
        callback_manager=callback_manager,
        verbose=True,
    )
    message = HumanMessage(content="Hello")
    response = chat.invoke([message])
    assert callback_handler.llm_streams > 0
    assert isinstance(response, BaseMessage)


def test_promptlayer_chat_openai_invalid_streaming_params() -> None:
    """Test that streaming correctly invokes on_llm_new_token callback."""
    with pytest.raises(ValueError):
        PromptLayerChatOpenAI(  # type: ignore[call-arg]
            max_tokens=10,
            streaming=True,
            temperature=0,
            n=5,
        )


async def test_async_promptlayer_chat_openai() -> None:
    """Test async generation."""
    chat = PromptLayerChatOpenAI(max_tokens=10, n=2)  # type: ignore[call-arg]
    message = HumanMessage(content="Hello")
    response = await chat.agenerate([[message], [message]])
    assert isinstance(response, LLMResult)
    assert len(response.generations) == 2
    for generations in response.generations:
        assert len(generations) == 2
        for generation in generations:
            assert isinstance(generation, ChatGeneration)
            assert isinstance(generation.text, str)
            assert generation.text == generation.message.content


async def test_async_promptlayer_chat_openai_streaming() -> None:
    """Test that streaming correctly invokes on_llm_new_token callback."""
    callback_handler = FakeCallbackHandler()
    callback_manager = CallbackManager([callback_handler])
    chat = PromptLayerChatOpenAI(  # type: ignore[call-arg]
        max_tokens=10,
        streaming=True,
        temperature=0,
        callback_manager=callback_manager,
        verbose=True,
    )
    message = HumanMessage(content="Hello")
    response = await chat.agenerate([[message], [message]])
    assert callback_handler.llm_streams > 0
    assert isinstance(response, LLMResult)
    assert len(response.generations) == 2
    for generations in response.generations:
        assert len(generations) == 1
        for generation in generations:
            assert isinstance(generation, ChatGeneration)
            assert isinstance(generation.text, str)
            assert generation.text == generation.message.content
