"""Test StochasticAI API wrapper."""

from aibaba_ai_community.llms.stochasticai import StochasticAI


def test_stochasticai_call() -> None:
    """Test valid call to StochasticAI."""
    llm = StochasticAI()
    output = llm.invoke("Say foo:")
    assert isinstance(output, str)
