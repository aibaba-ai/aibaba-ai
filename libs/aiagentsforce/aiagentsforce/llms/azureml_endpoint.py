from typing import TYPE_CHECKING, Any

from langchain._api import create_importer

if TYPE_CHECKING:
    from aiagentsforce_community.llms import AzureMLOnlineEndpoint
    from aiagentsforce_community.llms.azureml_endpoint import (
        AzureMLEndpointClient,
        ContentFormatterBase,
        CustomOpenAIContentFormatter,
        DollyContentFormatter,
        GPT2ContentFormatter,
        HFContentFormatter,
        OSSContentFormatter,
    )

# Create a way to dynamically look up deprecated imports.
# Used to consolidate logic for raising deprecation warnings and
# handling optional imports.
DEPRECATED_LOOKUP = {
    "AzureMLEndpointClient": "aiagentsforce_community.llms.azureml_endpoint",
    "ContentFormatterBase": "aiagentsforce_community.llms.azureml_endpoint",
    "GPT2ContentFormatter": "aiagentsforce_community.llms.azureml_endpoint",
    "OSSContentFormatter": "aiagentsforce_community.llms.azureml_endpoint",
    "HFContentFormatter": "aiagentsforce_community.llms.azureml_endpoint",
    "DollyContentFormatter": "aiagentsforce_community.llms.azureml_endpoint",
    "CustomOpenAIContentFormatter": "aiagentsforce_community.llms.azureml_endpoint",
    "AzureMLOnlineEndpoint": "aiagentsforce_community.llms",
}

_import_attribute = create_importer(__package__, deprecated_lookups=DEPRECATED_LOOKUP)


def __getattr__(name: str) -> Any:
    """Look up attributes dynamically."""
    return _import_attribute(name)


__all__ = [
    "AzureMLEndpointClient",
    "ContentFormatterBase",
    "GPT2ContentFormatter",
    "OSSContentFormatter",
    "HFContentFormatter",
    "DollyContentFormatter",
    "CustomOpenAIContentFormatter",
    "AzureMLOnlineEndpoint",
]
