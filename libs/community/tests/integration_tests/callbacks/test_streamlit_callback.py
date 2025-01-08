"""Integration tests for the StreamlitCallbackHandler module."""

import pytest

# Import the internal StreamlitCallbackHandler from its module - and not from
# the `aiagentsforce_community.callbacks.streamlit` package - so that we don't end up using
# Streamlit's externally-provided callback handler.
from aiagentsforce_community.callbacks.streamlit.streamlit_callback_handler import (
    StreamlitCallbackHandler,
)
from aiagentsforce_community.llms import OpenAI


@pytest.mark.requires("streamlit")
def test_streamlit_callback_agent() -> None:
    import streamlit as st
    from langchain.agents import AgentType, initialize_agent, load_tools

    streamlit_callback = StreamlitCallbackHandler(st.container())

    llm = OpenAI(temperature=0)
    tools = load_tools(["serpapi", "llm-math"], llm=llm)
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    agent.run(
        "Who is Olivia Wilde's boyfriend? "
        "What is his current age raised to the 0.23 power?",
        callbacks=[streamlit_callback],
    )
