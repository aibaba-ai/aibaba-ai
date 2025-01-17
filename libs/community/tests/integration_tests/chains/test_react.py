"""Integration test for self ask with search."""

from langchain.agents.react.base import ReActChain

from aibaba_ai_community.docstore import Wikipedia
from aibaba_ai_community.llms.openai import OpenAI


def test_react() -> None:
    """Test functionality on a prompt."""
    llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo-instruct")  # type: ignore[call-arg]
    react = ReActChain(llm=llm, docstore=Wikipedia())
    question = (
        "Author David Chanoff has collaborated with a U.S. Navy admiral "
        "who served as the ambassador to the United Kingdom under "
        "which President?"
    )
    output = react.run(question)
    assert output == "Bill Clinton"
