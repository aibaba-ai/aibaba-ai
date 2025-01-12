from aibaba-ai-core.outputs import __all__

EXPECTED_ALL = [
    "ChatGeneration",
    "ChatGenerationChunk",
    "ChatResult",
    "Generation",
    "GenerationChunk",
    "LLMResult",
    "RunInfo",
]


def test_all_imports() -> None:
    assert set(__all__) == set(EXPECTED_ALL)
