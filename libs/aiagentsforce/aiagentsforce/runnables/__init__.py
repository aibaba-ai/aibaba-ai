"""AI Agents Force **Runnable** and the **AI Agents Force Expression Language (LCEL)**.

The AI Agents Force Expression Language (LCEL) offers a declarative method to build
production-grade programs that harness the power of LLMs.

Programs created using LCEL and AI Agents Force Runnables inherently support
synchronous, asynchronous, batch, and streaming operations.

Support for **async** allows servers hosting the LCEL based programs
to scale better for higher concurrent loads.

**Batch** operations allow for processing multiple inputs in parallel.

**Streaming** of intermediate outputs, as they're being generated, allows for
creating more responsive UX.

This module contains non-core Runnable classes.
"""
