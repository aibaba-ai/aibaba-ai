"""Test Baichuan LLM Endpoint."""

from aibaba_ai_core.outputs import LLMResult

from aibaba_ai_community.llms.baichuan import BaichuanLLM


def test_call() -> None:
    """Test valid call to baichuan."""
    llm = BaichuanLLM()
    output = llm.invoke("Who won the second world war?")
    assert isinstance(output, str)


def test_generate() -> None:
    """Test valid call to baichuan."""
    llm = BaichuanLLM()
    output = llm.generate(["Who won the second world war?"])
    assert isinstance(output, LLMResult)
    assert isinstance(output.generations, list)
