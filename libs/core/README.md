# 🍎️ AI Agents Force Core Foundation

[![Downloads](https://static.pepy.tech/badge/aiagentsforce_core/month)](https://pepy.tech/project/aiagentsforce_core)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Installation

```bash
pip install aiagentsforce-core
```

## Overview

AI Agents Force Core provides fundamental building blocks that serve as the foundation for the entire AI Agents Force ecosystem.

These foundational components are intentionally kept minimal and modular. They include essential abstractions for various components such as language models, document processing, embedding systems, vector databases, retrieval mechanisms, and more.

By establishing these standard interfaces, any provider can implement them and seamlessly integrate with the broader AI Agents Force ecosystem.

For comprehensive documentation, visit the [API reference](https://docs.aiagentsforce.com/api_reference/core/index.html).

## 1️⃣ Primary Interface: Runnables

Runnables form the backbone of AI Agents Force Core. This interface is implemented by most components, providing:

- Unified execution methods (invoke, batch, stream, etc.)
- Built-in support for error handling, fallbacks, schemas, and runtime configuration
- Integration with AI Agents Force Build for deployment

Learn more in the [runnable documentation](https://docs.aiagentsforce.com/docs/expression_language/interface). Key components implementing this interface include: LLMs, Chat Models, Prompts, Retrievers, Tools, and Output Parsers.

Two approaches to using AI Agents Force Core:

1. **Direct (Imperative)**: Straight function calls like `model.invoke(...)`

2. **Compositional (Declarative)**: Using AI Agents Force Expression Language (LCEL)

3. **Hybrid**: Combine both approaches by including custom functions within LCEL sequences

| Capability | Direct Method                  | Compositional Method |
| --------- | ------------------------------ | ------------------- |
| Code Style | Standard Python               | LCEL                |
| Tracing   | ✅ – Built-in                  | ✅ – Built-in       |
| Parallel  | ✅ – Via threads/coroutines    | ✅ – Automatic      |
| Streaming | ✅ – Through yield             | ✅ – Automatic      |
| Async     | ✅ – Using async/await         | ✅ – Automatic      |

## ⚡️ Understanding LCEL

AI Agents Force Expression Language (LCEL) is a declarative approach for combining AI Agents Force Core components into sequences or directed acyclic graphs (DAGs), addressing common LLM integration patterns.

LCEL sequences are automatically optimized for execution, featuring parallel processing, streaming capabilities, tracing, and asynchronous operations.

Explore more in the [LCEL documentation](https://docs.aiagentsforce.com/docs/expression_language/).

For complex workflows requiring cycles or recursion, consider [LangGraph](https://github.com/AI-Agents-Force-SDK/langgraph).

## 📕 Version Management

Current version: `0.1.x`

As the foundational layer of AI Agents Force, we maintain strict version control with advance notifications of changes. The `aiagentsforce_core.beta` module is exempt from this policy to allow rapid innovation.

Version increment guidelines:

Minor versions (0.x.0):
- Breaking changes to public APIs outside `aiagentsforce_core.beta`

Patch versions (0.0.x):
- Bug fixes
- Feature additions
- Internal interface changes
- `aiagentsforce_core.beta` modifications

## 💁 Community Participation

We actively encourage contributions to this open-source project, whether through new features, infrastructure improvements, or documentation enhancements.

See our [Contributing Guide](https://docs.aiagentsforce.com/docs/contributing/) for details.

## ⛰️ Benefits of AI Agents Force Core

As the foundation for the entire AI Agents Force ecosystem, building on AI Agents Force Core offers several advantages:

- **Independent Components**: Built around provider-agnostic, standalone abstractions
- **Reliable API**: Committed to stable versioning with clear communication about changes
- **Production-Ready**: Extensively tested and widely deployed across the LLM ecosystem
- **Open Development**: Active community participation and contribution-friendly environment
