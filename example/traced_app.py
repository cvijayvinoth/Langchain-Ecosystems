"""
traced_app.py - a small LangChain app whose runs show up in LangSmith.

There is NO tracing code in this file. Tracing is switched on purely by
environment variables (put them in a .env file or export them in your shell):

    OPENAI_API_KEY=sk-ant-...
    LANGSMITH_TRACING=true
    LANGSMITH_API_KEY=lsv2_...
    LANGSMITH_PROJECT=claude-tracing-demo

Install:
    pip install langchain-anthropic python-dotenv

Run:
    python traced_app.py
"""

import os
import sys
import time

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(override=True)  # must run before the first model call so the env vars are visible

def preflight() -> None:
    """Fail loudly if tracing is silently off. Reads env vars only; sends nothing."""
    problems = []

    if os.getenv("LANGSMITH_TRACING", os.getenv("LANGCHAIN_TRACING_V2", "")).lower() != "true":
        problems.append("LANGSMITH_TRACING is not 'true'")
    if not (os.getenv("LANGSMITH_API_KEY") or os.getenv("LANGCHAIN_API_KEY")):
        problems.append("LANGSMITH_API_KEY is missing")
    if not (os.getenv("LANGSMITH_PROJECT") or os.getenv("LANGCHAIN_PROJECT")):
        problems.append("LANGSMITH_PROJECT is missing (runs would land in 'default')")
    if not os.getenv("OPENAI_API_KEY"):
        problems.append("OPENAI_API_KEY is missing")

    if problems:
        print("Tracing pre-flight FAILED:")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)

    project = os.getenv("LANGSMITH_PROJECT") or os.getenv("LANGCHAIN_PROJECT")
    print(f"Tracing pre-flight OK -> runs will appear in LangSmith project '{project}'\n")


# Three prompts chosen to differ in input size and output size, so the
# token/latency columns in LangSmith tell different stories.
PROMPTS = {
    "short_fact": "In one sentence, what is the capital of Australia?",
    "long_output": (
        "Explain how a hash map works internally: hashing, collisions, resizing, "
        "and time complexity. Include a short Python example."
    ),
    "long_input": (
        "Summarise the following in two sentences:\n\n"
        + (
            "LangSmith records every run of a LangChain application, including the "
            "exact prompt sent to the model, the response, latency, token counts and "
            "errors. Teams use it to debug bad answers, compare prompts, and watch "
            "cost over time. "
        )
        * 40
    ),
}


def main() -> None:
    preflight()

    llm = ChatOpenAI(model="gpt-4o-mini", max_tokens=600)

    for name, prompt in PROMPTS.items():
        start = time.perf_counter()
        response = llm.invoke(prompt)
        elapsed = time.perf_counter() - start

        usage = response.usage_metadata or {}
        print(f"=== {name} ===")
        print(response.content)
        print(
            f"\n[local view] {elapsed:.2f}s | "
            f"in={usage.get('input_tokens')} out={usage.get('output_tokens')} "
            f"total={usage.get('total_tokens')}\n"
        )

    print("Done. Open smith.langchain.com -> Tracing -> your project to see the runs.")


if __name__ == "__main__":
    main()