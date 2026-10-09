# Embeddings

Text Embeddings convert string content into fixed-dimensional numerical vectors. These vectors capture the semantic meaning of text—enabling mathematical similarity comparisons.

## Vector Space Mechanics
Texts with similar semantic context are positioned closer together in high-dimensional vector space, typically measured using metrics like Cosine Similarity, Dot Product, or Euclidean Distance.

## Common Embedding Models
* **OpenAI**: `OpenAIEmbeddings` (`text-embedding-3-small`, `text-embedding-3-large`)
* **HuggingFace**: `HuggingFaceEmbeddings` (e.g., `BAAI/bge-small-en-v1.5`)
* **Cohere**: `CohereEmbeddings`

## Code Example
```python
from langchain_openai import OpenAIEmbeddings

embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")

# Embedding individual query string
query_vector = embeddings_model.embed_query("What is vector retrieval?")

# Embedding batch documents
doc_vectors = embeddings_model.embed_documents([
    "Document entry 1 content.",
    "Document entry 2 content."
])

print(f"Vector Dimensions: {len(query_vector)}")
```

---
[Return to README](./README.md)
