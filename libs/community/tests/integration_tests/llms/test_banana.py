"""Test BananaDev API wrapper."""

from aibaba_ai_community.llms.bananadev import Banana


def test_banana_call() -> None:
    """Test valid call to BananaDev."""
    llm = Banana()
    output = llm.invoke("Say foo:")
    assert isinstance(output, str)
