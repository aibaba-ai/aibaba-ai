# Backwards compatibility.
from aiagentsforce_core.language_models import BaseLanguageModel
from aiagentsforce_core.language_models.llms import (
    LLM,
    BaseLLM,
)

__all__ = [
    "BaseLanguageModel",
    "BaseLLM",
    "LLM",
]
