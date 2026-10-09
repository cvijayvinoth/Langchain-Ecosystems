# LangSmith

**LangSmith** is an enterprise platform for building, testing, evaluating, and monitoring LLM applications. It integrates directly with LangChain to provide visibility into component executions.

## Primary Capabilities

1. **Tracing**: Visually inspect the exact inputs, prompts, outputs, latency, and token usage for every link in a chain.
2. **Debugging**: Replay step-by-step chain runs locally to identify failure modes or latency bottlenecks.
3. **Dataset & Evaluation**: Collect user queries to build testing benchmarks and run automated evaluation pipelines.
4. **Monitoring**: Track token consumption, failure rates, and execution costs in production.

## Enabling LangSmith Tracing

Tracing can be activated globally without changing chain code by defining these environment variables:

```bash
export LANGCHAIN_TRACING_V2="true"
export LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
export LANGCHAIN_API_KEY="your_langsmith_api_key"
export LANGCHAIN_PROJECT="my-langchain-assignment"
```

## Trace Execution View
Once enabled, executing any LCEL chain sends trace payloads to LangSmith asynchronously:

```python
# Tracing runs automatically when invoked
response = rag_chain.invoke("Explain LangSmith tracing")
# Inspect the resulting trace graph at https://smith.langchain.com
```

---
[Return to README](./README.md)
