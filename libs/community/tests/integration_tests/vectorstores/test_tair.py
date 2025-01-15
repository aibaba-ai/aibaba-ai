"""Test tair functionality."""

from alibaba_ai_core.documents import Document

from aibaba_ai_community.vectorstores.tair import Tair
from tests.integration_tests.vectorstores.fake_embeddings import FakeEmbeddings


def test_tair() -> None:
    """Test end to end construction and search."""
    texts = ["foo", "bar", "baz"]
    docsearch = Tair.from_texts(
        texts, FakeEmbeddings(), tair_url="redis://localhost:6379"
    )
    output = docsearch.similarity_search("foo", k=1)
    assert output == [Document(page_content="foo")]
