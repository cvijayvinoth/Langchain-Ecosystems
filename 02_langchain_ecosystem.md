# LangChain Ecosystem

The LangChain ecosystem consists of several interconnected packages designed for different stages of LLM application development.

```
                    ┌─────────────────────────┐
                    │       LangGraph         │ (Stateful Agents)
                    └───────────┬─────────────┘
                                │
┌───────────────────────────────▼───────────────────────────────┐
│                           LangChain                           │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │                     langchain-core                      │  │
│  └────────────────────────────┬────────────────────────────┘  │
│                               │                               │
│  ┌────────────────────────────▼────────────────────────────┐  │
│  │                  langchain-community                    │  │
│  └─────────────────────────────────────────────────────────┘  │
└───────────────────────────────┬───────────────────────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │        LangSmith        │ (Tracing & Observability)
                    └─────────────────────────┘
```

## Ecosystem Packages

### 1. `langchain-core`
Contains the core abstractions, base interfaces, and the **LangChain Expression Language (LCEL)** primitives. It maintains minimal dependencies to ensure lightweight performance.

### 2. `langchain-community`
Contains community-contributed integrations across third-party tools, databases, and services (e.g., Chroma, OpenAI, Hugging Face, Pinecone).

### 3. Partner Packages (e.g., `langchain-openai`, `langchain-anthropic`)
Dedicated packages maintained jointly with provider teams to guarantee stability and performance for specific platforms.

### 4. `langgraph`
An extension framework for building stateful, multi-actor LLM applications and agentic workflows using graph architectures.

### 5. `langsmith`
A developer platform for debugging, testing, evaluating, and monitoring LLM applications integrated directly into LangChain execution flows.

---
[Return to README](./README.md)
