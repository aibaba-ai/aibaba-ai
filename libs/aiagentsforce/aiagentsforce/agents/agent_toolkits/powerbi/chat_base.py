from typing import TYPE_CHECKING, Any

from langchain._api import create_importer

if TYPE_CHECKING:
    from aiagentsforce_community.agent_toolkits.powerbi.chat_base import (
        create_pbi_chat_agent,
    )

# Create a way to dynamically look up deprecated imports.
# Used to consolidate logic for raising deprecation warnings and
# handling optional imports.
DEPRECATED_LOOKUP = {
    "create_pbi_chat_agent": "aiagentsforce_community.agent_toolkits.powerbi.chat_base"
}

_import_attribute = create_importer(__package__, deprecated_lookups=DEPRECATED_LOOKUP)


def __getattr__(name: str) -> Any:
    """Look up attributes dynamically."""
    return _import_attribute(name)


__all__ = [
    "create_pbi_chat_agent",
]
