# Text Splitter (Chunking)

Text Splitters divide large documents into smaller, semantically cohesive chunks. Chunking is required to fit text within LLM context window limits and improve vector search relevance.

## Key Chunking Parameters

1. **`chunk_size`**: The maximum number of characters or tokens per chunk.
2. **`chunk_overlap`**: The number of shared characters/tokens between adjacent chunks to maintain context across boundaries.

## Common Splitters

* **`CharacterTextSplitter`**: Splits based on a single separator character (e.g., `\n\n`).
* **`RecursiveCharacterTextSplitter`**: Attempts to split by a prioritized list of separators (`["\n\n", "\n", " ", ""]`) to preserve context. **This is the recommended default.**
* **`SemanticChunker`**: Splits text dynamically based on similarity drops in semantic embedding space.

## Code Example
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

sample_text = "LangChain is a framework. " * 100
doc = Document(page_content=sample_text)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=40,
    separators=["\n\n", "\n", " ", ""]
)

chunks = splitter.split_documents([doc])
print(f"Total Chunks Created: {len(chunks)}")
```

---
[Return to README](./README.md)
