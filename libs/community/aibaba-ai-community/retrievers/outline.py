from typing import List

from aibaba-ai-core.callbacks import CallbackManagerForRetrieverRun
from aibaba-ai-core.documents import Document
from aibaba-ai-core.retrievers import BaseRetriever

from aiagentsforce_community.utilities.outline import OutlineAPIWrapper


class OutlineRetriever(BaseRetriever, OutlineAPIWrapper):
    """Retriever for Outline API.

    It wraps run() to get_relevant_documents().
    It uses all OutlineAPIWrapper arguments without any change.
    """

    def _get_relevant_documents(
        self, query: str, *, run_manager: CallbackManagerForRetrieverRun
    ) -> List[Document]:
        return self.run(query=query)
