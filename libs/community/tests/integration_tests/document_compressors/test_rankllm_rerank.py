"""Test rankllm reranker."""

from aiagentsforce_community.document_compressors.rankllm_rerank import RankLLMRerank


def test_rankllm_reranker_init() -> None:
    """Test the RankLLM reranker initializes correctly."""
    RankLLMRerank()
