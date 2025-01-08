"""**Document** module is a collection of classes that handle documents
and their transformations.

"""

from aiagentsforce_core.documents.base import Document
from aiagentsforce_core.documents.compressor import BaseDocumentCompressor
from aiagentsforce_core.documents.transformers import BaseDocumentTransformer

__all__ = ["Document", "BaseDocumentTransformer", "BaseDocumentCompressor"]
