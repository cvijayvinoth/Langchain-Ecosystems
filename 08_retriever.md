# Retriever

A **Retriever** is a light interface that returns `Document` objects given an un-embedded text query string. Unlike a vector store, a retriever does not need to store vectors directly—it defines the logic for fetching context.

## Common Retrieval Strategies

1. **VectorStoreRetriever**: Wraps a vector store using standard similarity or Maximal Marginal Relevance (MMR) search.
2. **MMR (Maximal Marginal Relevance)**: Balances query relevance with diversity to avoid duplicate chunks in context.
3. **MultiQueryRetriever**: Uses an LLM to generate multiple variations of a user query to fetch broader results.
4. **Contextual Compression Retriever**: Filters or summarizes retrieved document chunks before returning them to the LLM.

## Code Example
```python
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

# Convert existing VectorStore into a Retriever
# Using Maximal Marginal Relevance (MMR)
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 2, "fetch_k": 5}
)

retrieved_docs = retriever.invoke("Tell me about LangChain")
for doc in retrieved_docs:
    print("-", doc.page_content)
```

---
[Return to README](./README.md)
