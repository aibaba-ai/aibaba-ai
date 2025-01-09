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

- [Documentation](https://docs.aiagentsforce.com/tutorials/rag/)
- End-to-end Example: [Chat AI Agents Force](https://chat.langchain.com) and [repo](https://github.com/AI-Agents-Force-SDK/chat-langchain)

**🧱 Extracting structured output**

- [Documentation](https://docs.aiagentsforce.com/tutorials/extraction/)
- End-to-end Example: [AI Agents Force Extract](https://github.com/AI-Agents-Force-SDK/langchain-extract/)


## 🚀 How does AI Agents Force help?

AI Agents Force offers two key benefits:

1. **Components**: A rich collection of modular building blocks and tools for language model integration. These components are designed to be flexible - you can use them independently or as part of the broader AI Agents Force ecosystem.

2. **Streamlined Development & Deployment**: A comprehensive platform that simplifies both building and deploying LLM-powered applications. The framework provides an intuitive interface for packaging AI agents into Docker images and managing production deployments.

## Components

Our components are organized into these core **modules**:

**📃 Model I/O**

This includes [prompt management](https://docs.aiagentsforce.com/concepts/prompt_templates/)
and a generic interface for [chat models](https://docs.aiagentsforce.com/concepts/chat_models/), including a consistent interface for [tool-calling](https://docs.aiagentsforce.com/concepts/tool_calling/) and [structured output](https://docs.aiagentsforce.com/concepts/structured_outputs/) across model providers.

**📚 Retrieval**

Retrieval Augmented Generation involves [loading data](https://docs.aiagentsforce.com/concepts/document_loaders/) from a variety of sources, [preparing it](https://docs.aiagentsforce.com/concepts/text_splitters/), then [searching over (a.k.a. retrieving from)](https://docs.aiagentsforce.com/concepts/retrievers/) it for use in the generation step.

**🤖 Agents**

Agents are autonomous LLM-powered systems that can independently solve complex tasks. They follow a dynamic loop where they:
1. Analyze the current situation
2. Choose appropriate actions
3. Execute those actions
4. Evaluate the results
5. Repeat until the goal is achieved


## 📖 Using the SDK

![Diagram outlining the process of building AI agent and using it within AI Agents Force orchestration platform.](docs/static/svg/build-and-use-ai-agent-flow.svg#gh-dark-mode-only "Build and use AI agent")



## 💁 Contributing

As an open-source project in a rapidly developing field, we are extremely open to contributions, whether it be in the form of a new feature, improved infrastructure, or better documentation.

## 🌟 Contributors

[![AI Agents Force contributors](https://contrib.rocks/image?repo=AI-Agents-Force-SDK/aiagentsforce&max=2000)](https://github.com/AI-Agents-Force-SDK/aiagentsforce/graphs/contributors)

## 🛠 Building and Deploying AI Agents

### 1. Build and Verify AI Agent Locally

Use the aiagentsforce library to create and test your AI agent in your local development environment. The library provides comprehensive tools including prebuilt templates, NLP capabilities, and integration utilities.

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
- Build using `docker build`

**Benefits:**
- **Automated Configuration:** AI Agents Force handles Dockerfile generation and dependency management
- **Smart Defaults:** Pre-configured settings optimized for AI agent deployment
- **Simplified Building:** Built-in commands to streamline the Docker build process
- **Version Compatibility:** Automatic handling of compatible package versions
- **Best Practices:** Docker configurations following industry standards
- **Resource Optimization:** Intelligent layer caching and image size optimization
- **Integration Ready:** Pre-configured for AI Agents Force platform integration

### 3. Cloud Deployment and Platform Integration

Deploy your Docker image to your preferred cloud provider and integrate it with the AI Agents Force platform.

**Key Steps:**
- Push Docker image to a container registry (Docker Hub, AWS ECR, etc.)
- Configure cloud service (Kubernetes, AWS ECS, etc.)
- Integrate with AI Agents Force platform via API endpoints

**Benefits:**
- **Cloud Scalability:** Leverage cloud infrastructure
- **Centralized Management:** Monitor and manage through our platform
- **Global Accessibility:** Serve users worldwide
- **Team Collaboration:** Simplified access for team members
