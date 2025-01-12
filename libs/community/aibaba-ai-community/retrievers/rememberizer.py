from typing import List

from aibaba-ai-core.callbacks import CallbackManagerForRetrieverRun
from aibaba-ai-core.documents import Document
from aibaba-ai-core.retrievers import BaseRetriever

from aiagentsforce_community.utilities.rememberizer import RememberizerAPIWrapper


class RememberizerRetriever(BaseRetriever, RememberizerAPIWrapper):
    """`Rememberizer` retriever.

    It wraps load() to get_relevant_documents().
    It uses all RememberizerAPIWrapper arguments without any change.
    """

    def _get_relevant_documents(
        self, query: str, *, run_manager: CallbackManagerForRetrieverRun
    ) -> List[Document]:
        return self.load(query=query)
