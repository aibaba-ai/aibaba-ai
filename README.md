# 🔗 AI Agents Force

This repository is based on [langchain](https://github.com/langchain-ai/langchain) by [Harrison Chase].

## Quick Install

With pip:

```bash
pip install aiagentsforce
```

With conda:

```bash
conda install aiagentsforce -c conda-forge
```

## 🤔 What is AI Agents Force?

**AI Agents Force** is a powerful framework that streamlines the development of LLM-powered applications.

AI Agents Force provides end-to-end support throughout your application's lifecycle, making it easier to:

## 🧱 What can you build with AI Agents Force?

**❓ Advanced Question-Answering Systems with RAG**

- [Documentation](https://docs.aiagentsforce.com//tutorials/rag/)
- End-to-end Example: [Chat AI Agents Force](https://chat.langchain.com) and [repo](https://github.com/AI-Agents-Force-SDK/chat-langchain)

**🧱 Extracting structured output**

- [Documentation](https://docs.aiagentsforce.com//tutorials/extraction/)
- End-to-end Example: [AI Agents Force Extract](https://github.com/AI-Agents-Force-SDK/langchain-extract/)


## 🚀 How does AI Agents Force help?

AI Agents Force offers two key benefits:

1. **Components**: A rich collection of modular building blocks and tools for language model integration. These components are designed to be flexible - you can use them independently or as part of the broader AI Agents Force ecosystem.

2. **Streamlined Development & Deployment**: A comprehensive platform that simplifies both building and deploying LLM-powered applications. The framework provides an intuitive interface for packaging AI agents into Docker images and managing production deployments.

## Components

Our components are organized into these core **modules**:

**📃 Model I/O**

This includes [prompt management](https://docs.aiagentsforce.com//concepts/prompt_templates/)
and a generic interface for [chat models](https://docs.aiagentsforce.com//concepts/chat_models/), including a consistent interface for [tool-calling](https://docs.aiagentsforce.com//concepts/tool_calling/) and [structured output](https://docs.aiagentsforce.com//concepts/structured_outputs/) across model providers.

**📚 Retrieval**

Retrieval Augmented Generation involves [loading data](https://docs.aiagentsforce.com//concepts/document_loaders/) from a variety of sources, [preparing it](https://docs.aiagentsforce.com//concepts/text_splitters/), then [searching over (a.k.a. retrieving from)](https://docs.aiagentsforce.com//concepts/retrievers/) it for use in the generation step.

**🤖 Agents**

Agents are autonomous LLM-powered systems that can independently solve complex tasks. They follow a dynamic loop where they:
1. Analyze the current situation
2. Choose appropriate actions
3. Execute those actions
4. Evaluate the results
5. Repeat until the goal is achieved

[LangGraph](https://langchain-ai.github.io/langgraph/) provides a powerful framework to create both [custom](https://langchain-ai.github.io/langgraph/tutorials/) and [pre-built](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/) AI agents using AI Agents Force components.

## 📖 Documentation

Please see [here](https://dev.aiagentsforce.com) for full documentation, which includes:

- [Introduction](https://docs.aiagentsforce.com//introduction/): Overview of the framework and the structure of the docs.
- [Tutorials](https://docs.aiagentsforce.com//tutorials/): If you're looking to build something specific or are more of a hands-on learner, check out our tutorials. This is the best place to get started.
- [How-to guides](https://docs.aiagentsforce.com//how_to/): Answers to “How do I….?” type questions. These guides are goal-oriented and concrete; they're meant to help you complete a specific task.
- [Conceptual guide](https://docs.aiagentsforce.com//concepts/): Conceptual explanations of the key parts of the framework.
- [API Reference](https://docs.aiagentsforce.com/api_reference/): Thorough documentation of every class and method.

## 💁 Contributing

As an open-source project in a rapidly developing field, we are extremely open to contributions, whether it be in the form of a new feature, improved infrastructure, or better documentation.

## 🌟 Contributors

[![AI Agents Force contributors](https://contrib.rocks/image?repo=AI-Agents-Force-SDK/aiagentsforce&max=2000)](https://github.com/AI-Agents-Force-SDK/aiagentsforce/graphs/contributors)
