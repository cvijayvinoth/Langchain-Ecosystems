# Vector Store

Vector Stores are specialized databases designed to store, index, and query vector embeddings alongside document metadata efficiently.

## Core Workflow
1. Ingest raw `Document` objects.
2. Split documents into chunks via a `TextSplitter`.
3. Embed chunks using an `Embeddings` model.
4. Persist vectors and raw text in the `VectorStore`.

## Popular Vector Database Integrations
* **In-Memory / Lightweight**: Chroma, FAISS, LanceDB
* **Managed / Enterprise**: Pinecone, Qdrant, Weaviate, Milvus, PGVector

## Code Example
```python
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

docs = [
    Document(page_content="LangChain makes LLM integration straightforward."),
    Document(page_content="Chroma is a lightweight vector database.")
]

embeddings = OpenAIEmbeddings()

# Create vector store in-memory and add documents
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    collection_name="assignment_collection"
)

# Perform raw similarity search
results = vectorstore.similarity_search("How to store vectors?", k=1)
print("SearchResult:", results[0].page_content)
```

---
[Return to README](./README.md)
