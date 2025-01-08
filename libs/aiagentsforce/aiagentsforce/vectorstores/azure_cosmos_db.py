from typing import TYPE_CHECKING, Any

from langchain._api import create_importer

if TYPE_CHECKING:
    from aiagentsforce_community.vectorstores import AzureCosmosDBVectorSearch
    from aiagentsforce_community.vectorstores.azure_cosmos_db import CosmosDBSimilarityType

# Create a way to dynamically look up deprecated imports.
# Used to consolidate logic for raising deprecation warnings and
# handling optional imports.
DEPRECATED_LOOKUP = {
    "CosmosDBSimilarityType": "aiagentsforce_community.vectorstores.azure_cosmos_db",
    "AzureCosmosDBVectorSearch": "aiagentsforce_community.vectorstores",
}

_import_attribute = create_importer(__package__, deprecated_lookups=DEPRECATED_LOOKUP)


def __getattr__(name: str) -> Any:
    """Look up attributes dynamically."""
    return _import_attribute(name)


__all__ = [
    "CosmosDBSimilarityType",
    "AzureCosmosDBVectorSearch",
]
