"""Standard Aibaba AI interface tests"""

from typing import Type

from aibaba_ai_core.embeddings import Embeddings
from langchain_tests.integration_tests.embeddings import EmbeddingsIntegrationTests

from aiagentsforce_openai import OpenAIEmbeddings


class TestOpenAIStandard(EmbeddingsIntegrationTests):
    @property
    def embeddings_class(self) -> Type[Embeddings]:
        return OpenAIEmbeddings

    @property
    def embedding_model_params(self) -> dict:
        return {"model": "text-embedding-3-small", "dimensions": 128}
