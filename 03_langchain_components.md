# LangChain Components

LangChain provides standard abstractions across various core modules.

## Core Primitives

### 1. Model I/O
Manages interaction with LLMs, prompt formatting, and output parsing.
* **LLMs vs. Chat Models**: `LLMs` process string inputs and return string completions. `ChatModels` accept structured messages (`SystemMessage`, `HumanMessage`, `AIMessage`) and return an `AIMessage`.
* **Prompt Templates**: Translate user inputs into dynamic prompt strings or message structures.
* **Output Parsers**: Extract structured formats (e.g., JSON, Pydantic objects) directly from raw model strings.

### 2. Memory
Preserves conversational state across multiple turns.
* **BaseChatMemory**: Abstract interface for storing history.
* Common strategies include buffer windowing, summary memory, and vector-backed historical retrieval.

### 3. Example Implementation
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_template("Explain {topic} in simple terms.")
model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

# Composing via LCEL
chain = prompt | model | parser
response = chain.invoke({"topic": "vectors"})
print(response)
```

---
[Return to README](./README.md)
