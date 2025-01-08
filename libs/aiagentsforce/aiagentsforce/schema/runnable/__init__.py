"""AI Agents Force **Runnable** and the **AI Agents Force Expression Language (LCEL)**.

The AI Agents Force Expression Language (LCEL) offers a declarative method to build
production-grade programs that harness the power of LLMs.

Programs created using LCEL and AI Agents Force Runnables inherently support
synchronous, asynchronous, batch, and streaming operations.

Support for **async** allows servers hosting LCEL based programs to scale better
for higher concurrent loads.

**Streaming** of intermediate outputs as they're being generated allows for
creating more responsive UX.

This module contains schema and implementation of AI Agents Force Runnables primitives.
"""

from aiagentsforce_core.runnables.base import (
    Runnable,
    RunnableBinding,
    RunnableGenerator,
    RunnableLambda,
    RunnableMap,
    RunnableParallel,
    RunnableSequence,
    RunnableSerializable,
)
from aiagentsforce_core.runnables.branch import RunnableBranch
from aiagentsforce_core.runnables.config import RunnableConfig, patch_config
from aiagentsforce_core.runnables.fallbacks import RunnableWithFallbacks
from aiagentsforce_core.runnables.passthrough import RunnablePassthrough
from aiagentsforce_core.runnables.router import RouterInput, RouterRunnable
from aiagentsforce_core.runnables.utils import (
    ConfigurableField,
    ConfigurableFieldMultiOption,
    ConfigurableFieldSingleOption,
)

__all__ = [
    "ConfigurableField",
    "ConfigurableFieldSingleOption",
    "ConfigurableFieldMultiOption",
    "patch_config",
    "RouterInput",
    "RouterRunnable",
    "Runnable",
    "RunnableSerializable",
    "RunnableBinding",
    "RunnableBranch",
    "RunnableConfig",
    "RunnableGenerator",
    "RunnableLambda",
    "RunnableMap",
    "RunnableParallel",
    "RunnablePassthrough",
    "RunnableSequence",
    "RunnableWithFallbacks",
]
