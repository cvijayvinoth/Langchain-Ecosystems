# Data Ingestion (Document Loaders)

Data Ingestion is the process of loading raw, unstructured, or structured data from various sources and converting it into standardized LangChain `Document` objects.

## The Document Abstraction
A `Document` object consists of two core attributes:
* `page_content`: The raw text content (`str`).
* `metadata`: A dictionary containing contextual information (e.g., source file name, page number, creation date).

## Common Document Loaders

| Loader Type | Class Name | Target Source |
| :--- | :--- | :--- |
| **Text** | `TextLoader` | Plain text files (`.txt`) |
| **PDF** | `PyPDFLoader` / `UnstructuredPDFLoader` | PDF documents |
| **Web** | `WebBaseLoader` | HTML web pages |
| **Directory** | `DirectoryLoader` | Bulk ingestion across folder paths |

## Code Example
```python
from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader

# Ingest PDF
pdf_loader = PyPDFLoader("sample.pdf")
pdf_docs = pdf_loader.load()

# Ingest Web Page
web_loader = WebBaseLoader("https://docs.langchain.com")
web_docs = web_loader.load()

print(f"Loaded {len(pdf_docs)} PDF pages.")
print(f"First Page Snippet: {pdf_docs[0].page_content[:100]}")
```

---
[Return to README](./README.md)
