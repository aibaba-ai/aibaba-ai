"""**Cross encoders** are wrappers around cross encoder models from different APIs and
    services.

**Cross encoder models** can be LLMs or not.

**Class hierarchy:**

.. code-block::

    BaseCrossEncoder --> <name>CrossEncoder  # Examples: SagemakerEndpointCrossEncoder
"""

import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from aibaba_ai_community.cross_encoders.base import (
        BaseCrossEncoder,
    )
    from aibaba_ai_community.cross_encoders.fake import (
        FakeCrossEncoder,
    )
    from aibaba_ai_community.cross_encoders.huggingface import (
        HuggingFaceCrossEncoder,
    )
    from aibaba_ai_community.cross_encoders.sagemaker_endpoint import (
        SagemakerEndpointCrossEncoder,
    )

__all__ = [
    "BaseCrossEncoder",
    "FakeCrossEncoder",
    "HuggingFaceCrossEncoder",
    "SagemakerEndpointCrossEncoder",
]

_module_lookup = {
    "BaseCrossEncoder": "aibaba_ai_community.cross_encoders.base",
    "FakeCrossEncoder": "aibaba_ai_community.cross_encoders.fake",
    "HuggingFaceCrossEncoder": "aibaba_ai_community.cross_encoders.huggingface",
    "SagemakerEndpointCrossEncoder": "aibaba_ai_community.cross_encoders.sagemaker_endpoint",  # noqa: E501
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")
