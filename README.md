# LangChain Core Concepts Assignment

Welcome to the **LangChain Core Concepts Assignment** repository. This assignment explores the fundamental building blocks of the LangChain ecosystem, spanning document ingestion, vector storage, retrieval-augmented generation (RAG), and tracing with LangSmith.

---

## 📋 Table of Contents

1. [Introduction to LangChain](./01_introduction_to_langchain.md)
2. [LangChain Ecosystem](./02_langchain_ecosystem.md)
3. [LangChain Components](./03_langchain_components.md)
4. [Data Ingestion](./04_data_ingestion.md)
5. [Text Splitter](./05_text_splitter.md)
6. [Embeddings](./06_embeddings.md)
7. [Vector Store](./07_vector_store.md)
8. [Retriever](./08_retriever.md)
9. [Chain](./09_chain.md)
10. [LangSmith](./10_langsmith.md)

---

## 🎯 Assignment Purpose & Objectives

The primary goal of this repository is to demonstrate a thorough understanding of building LLM-powered applications using LangChain. 

Key learning outcomes include:
* Understanding the modular architecture of LangChain and its core abstractions.
* Mastering the pipeline for Retrieval-Augmented Generation (RAG): Ingestion -> Chunking -> Embedding -> Vector Storage -> Retrieval.
* Orchestrating component workflows using the LangChain Expression Language (LCEL).
* Monitoring, testing, and debugging LLM pipelines using LangSmith.

---

## ⚙️ Setup and Prerequisites

### Prerequisites
* **Python**: 3.10 or higher
* API Keys:
  * `OPENAI_API_KEY` (or alternative LLM/Embedding provider keys)
  * `LANGCHAIN_API_KEY` (for tracking and debugging via LangSmith)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/langchain-assignment.git
   cd langchain-assignment
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Core Dependencies**
   ```bash
   pip install langchain langchain-community langchain-openai chromadb langsmith
   ```

4. **Environment Variables Configuration**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
   LANGCHAIN_API_KEY=your_langsmith_api_key_here
   LANGCHAIN_PROJECT="assignment-project"
   ```

---

## 📁 Repository Structure & Topic Guide

| File | Core Subject | Description |
| :--- | :--- | :--- |
| [`01_introduction_to_langchain.md`](./01_introduction_to_langchain.md) | Basics & Value | Overview of LangChain, key benefits, and primary use cases. |
| [`02_langchain_ecosystem.md`](./02_langchain_ecosystem.md) | Architecture | Breakdown of `langchain-core`, `community`, `langgraph`, and `langsmith`. |
| [`03_langchain_components.md`](./03_langchain_components.md) | Modules | Key primitives: Models, Prompts, Output Parsers, and Memory. |
| [`04_data_ingestion.md`](./04_data_ingestion.md) | Document Loaders | Ingesting structured and unstructured data (PDF, Web, Text). |
| [`05_text_splitter.md`](./05_text_splitter.md) | Chunking | Dividing text effectively using chunk size, overlap, and recursive strategy. |
| [`06_embeddings.md`](./06_embeddings.md) | Vector Repr. | Transforming text into high-dimensional vector space. |
| [`07_vector_store.md`](./07_vector_store.md) | Persistence | Storing, indexing, and querying vector embeddings efficiently. |
| [`08_retriever.md`](./08_retriever.md) | Querying | Retrieval mechanisms including Similarity, MMR, and Multi-Query. |
| [`09_chain.md`](./09_chain.md) | LCEL & Flow | Constructing pipelines with standard LCEL and Runnable interfaces. |
| [`10_langsmith.md`](./10_langsmith.md) | Observability | Tracing, debugging, evaluating, and monitoring chain executions. |
