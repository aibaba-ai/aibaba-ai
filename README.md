# 🔗 Aibaba AI

This repository is based on [langchain](https://github.com/langchain-ai/langchain) by [Harrison Chase].

## Quick Install

With pip:

```bash
pip install aibaba_ai
```

With conda:

```bash
conda install aibaba_ai -c conda-forge
```

## 🤔 What is Aibaba AI?

**Aibaba AI** is a powerful framework that streamlines the development of LLM-powered applications.

Aibaba AI provides end-to-end support throughout your application's lifecycle, making it easier to:

## 🧱 What can you build with Aibaba AI?

**❓ Advanced Question-Answering Systems with RAG**

- [Documentation](https://docs.aibaba.world/tutorials/rag/)
- End-to-end Example: [Chat Aibaba AI](https://chat.langchain.com) and [repo](https://github.com/aibaba-ai/chat-langchain)

**🧱 Extracting structured output**

- [Documentation](https://docs.aibaba.world/tutorials/extraction/)
- End-to-end Example: [Aibaba AI Extract](https://github.com/aibaba-ai/aibaba-ai-extract/)


## 🚀 How does Aibaba AI help?

Aibaba AI offers two key benefits:

1. **Components**: A rich collection of modular building blocks and tools for language model integration. These components are designed to be flexible - you can use them independently or as part of the broader Aibaba AI ecosystem.

2. **Streamlined Development & Deployment**: A comprehensive platform that simplifies both building and deploying LLM-powered applications. The framework provides an intuitive interface for packaging AI agents into Docker images and managing production deployments.

## Components

Our components are organized into these core **modules**:

**📃 Model I/O**

This includes [prompt management](https://docs.aibaba.world/concepts/prompt_templates/)
and a generic interface for [chat models](https://docs.aibaba.world/concepts/chat_models/), including a consistent interface for [tool-calling](https://docs.aibaba.world/concepts/tool_calling/) and [structured output](https://docs.aibaba.world/concepts/structured_outputs/) across model providers.

**📚 Retrieval**

Retrieval Augmented Generation involves [loading data](https://docs.aibaba.world/concepts/document_loaders/) from a variety of sources, [preparing it](https://docs.aibaba.world/concepts/text_splitters/), then [searching over (a.k.a. retrieving from)](https://docs.aibaba.world/concepts/retrievers/) it for use in the generation step.

**🤖 Agents**

Agents are autonomous LLM-powered systems that can independently solve complex tasks. They follow a dynamic loop where they:
1. Analyze the current situation
2. Choose appropriate actions
3. Execute those actions
4. Evaluate the results
5. Repeat until the goal is achieved


## 📖 Building and Deploying AI Agents

![Diagram outlining the process of building AI agent and using it within Aibaba AI orchestration platform.](https://github.com/aibaba-ai/aibaba-ai/blob/main/docs/static/svg/build-and-use-ai-agent-flow.svg "Build and use AI Agent")

### 1. Build and Verify AI Agent Locally

Use the aibaba_ai library to create and test your AI agent in your local development environment. The library provides comprehensive tools including prebuilt templates, NLP capabilities, and integration utilities.

**Key Steps:**
- Define the agent's functionality, purpose, and environment
- Implement logic, train models, and integrate external services
- Test agent responses locally

**Benefits:**
- Rapid iteration and debugging without cloud costs
- Familiar development environment
- Local optimization capabilities

### 2. Build Docker Image

Package your verified AI agent into a Docker container for consistent deployment across environments.

**Key Steps:**
- Create a Dockerfile with your agent's environment configuration
- Include all dependencies and settings

**Benefits:**
- **Automated Configuration:** Aibaba AI handles Dockerfile generation and dependency management
- **Smart Defaults:** Pre-configured settings optimized for AI agent deployment
- **Simplified Building:** Built-in commands to streamline the Docker build process
- **Version Compatibility:** Automatic handling of compatible package versions
- **Best Practices:** Docker configurations following industry standards
- **Resource Optimization:** Intelligent layer caching and image size optimization
- **Integration Ready:** Pre-configured for Aibaba AI platform integration

### 3. Cloud Deployment and Platform Integration

Deploy your Docker image to your preferred cloud provider and integrate it with the Aibaba AI platform.

**Key Steps:**
- Push Docker image to a container registry (Docker Hub, AWS ECR, etc.)
- Configure cloud service (Kubernetes, AWS ECS, etc.)
- Integrate with Aibaba AI platform via API endpoints

**Benefits:**
- **Cloud Scalability:** Leverage cloud infrastructure
- **Centralized Management:** Monitor and manage through our platform
- **Global Accessibility:** Serve users worldwide

## 💁 Contributing

As an open-source project in a rapidly developing field, we are extremely open to contributions, whether it be in the form of a new feature, improved infrastructure, or better documentation.

## 🌟 Contributors

[![Aibaba AI contributors](https://contrib.rocks/image?repo=aibaba-ai/aibaba-ai&max=2000)](https://github.com/aibaba-ai/aibaba-ai/graphs/contributors)
