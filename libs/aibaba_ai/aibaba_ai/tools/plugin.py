from typing import TYPE_CHECKING, Any

from langchain._api import create_importer

if TYPE_CHECKING:
    from aibaba_ai_community.tools import AIPluginTool
    from aibaba_ai_community.tools.plugin import AIPlugin, AIPluginToolSchema, ApiConfig

# Create a way to dynamically look up deprecated imports.
# Used to consolidate logic for raising deprecation warnings and
# handling optional imports.
DEPRECATED_LOOKUP = {
    "ApiConfig": "aibaba_ai_community.tools.plugin",
    "AIPlugin": "aibaba_ai_community.tools.plugin",
    "AIPluginToolSchema": "aibaba_ai_community.tools.plugin",
    "AIPluginTool": "aibaba_ai_community.tools",
}

_import_attribute = create_importer(__package__, deprecated_lookups=DEPRECATED_LOOKUP)


def __getattr__(name: str) -> Any:
    """Look up attributes dynamically."""
    return _import_attribute(name)


__all__ = [
    "ApiConfig",
    "AIPlugin",
    "AIPluginToolSchema",
    "AIPluginTool",
]
