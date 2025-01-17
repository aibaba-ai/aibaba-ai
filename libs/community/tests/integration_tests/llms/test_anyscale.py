"""Test Anyscale API wrapper."""

from aibaba_ai_community.llms.anyscale import Anyscale


def test_anyscale_call() -> None:
    """Test valid call to Anyscale."""
    llm = Anyscale()
    output = llm.invoke("Say foo:")
    assert isinstance(output, str)
