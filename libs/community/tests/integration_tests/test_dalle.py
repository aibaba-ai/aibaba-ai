"""Integration test for DallE API Wrapper."""

from aibaba_ai_community.utilities.dalle_image_generator import DallEAPIWrapper


def test_call() -> None:
    """Test that call returns a URL in the output."""
    search = DallEAPIWrapper()  # type: ignore[call-arg]
    output = search.run("volcano island")
    assert "https://oaidalleapi" in output
