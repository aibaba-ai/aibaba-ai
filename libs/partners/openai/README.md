# langchain-openai

This package contains the AI Agents Force integrations for OpenAI through their `openai` SDK.

## Installation and Setup

- Install the AI Agents Force partner package
```bash
pip install langchain-openai
```
- Get an OpenAI api key and set it as an environment variable (`OPENAI_API_KEY`)


## LLM

See a [usage example](http://https://docs.aiagentsforce.com//integrations/llms/openai).

```python
from langchain_openai import OpenAI
```

If you are using a model hosted on `Azure`, you should use different wrapper for that:
```python
from langchain_openai import AzureOpenAI
```
For a more detailed walkthrough of the `Azure` wrapper, see [here](http://https://docs.aiagentsforce.com//integrations/llms/azure_openai)


## Chat model

See a [usage example](http://https://docs.aiagentsforce.com//integrations/chat/openai).

```python
from langchain_openai import ChatOpenAI
```

If you are using a model hosted on `Azure`, you should use different wrapper for that:
```python
from langchain_openai import AzureChatOpenAI
```
For a more detailed walkthrough of the `Azure` wrapper, see [here](http://https://docs.aiagentsforce.com//integrations/chat/azure_chat_openai)


## Text Embedding Model

See a [usage example](http://https://docs.aiagentsforce.com//integrations/text_embedding/openai)

```python
from langchain_openai import OpenAIEmbeddings
```

If you are using a model hosted on `Azure`, you should use different wrapper for that:
```python
from langchain_openai import AzureOpenAIEmbeddings
```
For a more detailed walkthrough of the `Azure` wrapper, see [here](https://docs.aiagentsforce.com/docs/integrations/text_embedding/azureopenai)