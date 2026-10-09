# Chain (LangChain Expression Language - LCEL)

Chains combine components (Models, Prompts, Output Parsers, Retrievers) into end-to-end execution pipelines using **LangChain Expression Language (LCEL)**.

## The Pipe Operator (`|`)
LCEL uses the pipe operator (`|`) to compose standard `Runnable` primitives, seamlessly passing outputs from left to right.

## Core Benefits of LCEL
* **Streaming Support**: Stream tokens directly as they are generated.
* **Async Capabilities**: Built-in support for native asynchronous execution (`ainvoke`).
* **Parallel Execution**: Execute independent operations concurrently using `RunnableParallel`.

## End-to-End RAG Chain Example
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

prompt_template = """Answer the question based ONLY on the following context:
{context}

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(prompt_template)
model = ChatOpenAI(model="gpt-4o-mini")

# Build Complete RAG Chain
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

response = rag_chain.invoke("What is Chroma?")
print(response)
```

---
[Return to README](./README.md)
