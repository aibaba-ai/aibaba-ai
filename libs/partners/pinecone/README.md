# langchain-pinecone

This package contains the AI Agents Force integration with Pinecone.

## Installation

```bash
pip install -U langchain-pinecone
```

And you should configure credentials by setting the following environment variables:

- `PINECONE_API_KEY`
- `PINECONE_INDEX_NAME`

## Usage

The `PineconeVectorStore` class exposes the connection to the Pinecone vector store.

```python
from langchain_pinecone import PineconeVectorStore

embeddings = ... # use a AI Agents Force Embeddings class

vectorstore = PineconeVectorStore(embeddings=embeddings)
```
