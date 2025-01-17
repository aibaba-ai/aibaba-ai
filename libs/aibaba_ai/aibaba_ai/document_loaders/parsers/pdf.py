from typing import TYPE_CHECKING, Any

from langchain._api import create_importer

if TYPE_CHECKING:
    from aibaba_ai_community.document_loaders.parsers.pdf import (
        AmazonTextractPDFParser,
        DocumentIntelligenceParser,
        PDFMinerParser,
        PDFPlumberParser,
        PyMuPDFParser,
        PyPDFium2Parser,
        PyPDFParser,
        extract_from_images_with_rapidocr,
    )

# Create a way to dynamically look up deprecated imports.
# Used to consolidate logic for raising deprecation warnings and
# handling optional imports.
DEPRECATED_LOOKUP = {
    "extract_from_images_with_rapidocr": (
        "aibaba_ai_community.document_loaders.parsers.pdf"
    ),
    "PyPDFParser": "aibaba_ai_community.document_loaders.parsers.pdf",
    "PDFMinerParser": "aibaba_ai_community.document_loaders.parsers.pdf",
    "PyMuPDFParser": "aibaba_ai_community.document_loaders.parsers.pdf",
    "PyPDFium2Parser": "aibaba_ai_community.document_loaders.parsers.pdf",
    "PDFPlumberParser": "aibaba_ai_community.document_loaders.parsers.pdf",
    "AmazonTextractPDFParser": "aibaba_ai_community.document_loaders.parsers.pdf",
    "DocumentIntelligenceParser": "aibaba_ai_community.document_loaders.parsers.pdf",
}

_import_attribute = create_importer(__package__, deprecated_lookups=DEPRECATED_LOOKUP)


def __getattr__(name: str) -> Any:
    """Look up attributes dynamically."""
    return _import_attribute(name)


__all__ = [
    "extract_from_images_with_rapidocr",
    "PyPDFParser",
    "PDFMinerParser",
    "PyMuPDFParser",
    "PyPDFium2Parser",
    "PDFPlumberParser",
    "AmazonTextractPDFParser",
    "DocumentIntelligenceParser",
]
