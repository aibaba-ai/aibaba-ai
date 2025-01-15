"""Test Pipeline Cloud API wrapper."""

from aibaba_ai_community.llms.pipelineai import PipelineAI


def test_pipelineai_call() -> None:
    """Test valid call to Pipeline Cloud."""
    llm = PipelineAI()
    output = llm.invoke("Say foo:")
    assert isinstance(output, str)
