from typing import TYPE_CHECKING, Any

from langchain._api import create_importer

if TYPE_CHECKING:
    from aiagentsforce_community.llms import PromptLayerOpenAI, PromptLayerOpenAIChat

# Create a way to dynamically look up deprecated imports.
# Used to consolidate logic for raising deprecation warnings and
# handling optional imports.
DEPRECATED_LOOKUP = {
    "PromptLayerOpenAI": "aiagentsforce_community.llms",
    "PromptLayerOpenAIChat": "aiagentsforce_community.llms",
}

_import_attribute = create_importer(__package__, deprecated_lookups=DEPRECATED_LOOKUP)


def __getattr__(name: str) -> Any:
    """Look up attributes dynamically."""
    return _import_attribute(name)


__all__ = [
    "PromptLayerOpenAI",
    "PromptLayerOpenAIChat",
]
