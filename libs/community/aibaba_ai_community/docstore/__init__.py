"""**Docstores** are classes to store and load Documents.

The **Docstore** is a simplified version of the Document Loader.

**Class hierarchy:**

.. code-block::

    Docstore --> <name> # Examples: InMemoryDocstore, Wikipedia

**Main helpers:**

.. code-block::

    Document, AddableMixin
"""

import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from aibaba_ai_community.docstore.arbitrary_fn import (
        DocstoreFn,
    )
    from aibaba_ai_community.docstore.in_memory import (
        InMemoryDocstore,
    )
    from aibaba_ai_community.docstore.wikipedia import (
        Wikipedia,
    )

_module_lookup = {
    "DocstoreFn": "aibaba_ai_community.docstore.arbitrary_fn",
    "InMemoryDocstore": "aibaba_ai_community.docstore.in_memory",
    "Wikipedia": "aibaba_ai_community.docstore.wikipedia",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


__all__ = ["DocstoreFn", "InMemoryDocstore", "Wikipedia"]
