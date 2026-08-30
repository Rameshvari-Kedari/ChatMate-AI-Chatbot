# agent.py

import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent

from tools import tools


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY is not found. "
        "Please add it to your .env file."
    )


# ============================================================
# CREATE LLM
# ============================================================

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="openai/gpt-oss-120b",
    temperature=0
)


# ============================================================
# CREATE AGENT
# ============================================================

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
You are ChatMate, a helpful AI assistant.

You have access to several tools.

TOOL RULES:

1. CALCULATOR
Use the calculator tool for mathematical calculations.

The calculator requires:
expression

Example:
calculator(expression="25 * 10")

2. WEB SEARCH
Use web_search for:
- latest information
- current events
- recent news
- today's information
- information from the internet

IMPORTANT:
The web_search tool requires exactly one input:

query

Example:
web_search(query="current Nepal flood news")

Never use cursor, id, or any other argument for web_search.

3. CURRENT TIME
Use get_current_time when the user asks for the current date or time.

4. TEMPERATURE
Use the temperature conversion tools when the user asks for Celsius/Fahrenheit conversion.

5. DISTANCE
Use the kilometer/mile conversion tools for distance conversion.

6. TEXT ANALYZER
Use analyze_text when the user asks for word count, character count,
or sentence count.

If a tool is not necessary, answer normally.

Always use the appropriate tool when it is clearly required.
"""
)


# ============================================================
# TEST AGENT
# ============================================================

if __name__ == "__main__":

    print("\nChatMate Agent Test")
    print("-" * 40)

    question = input("You: ")

    try:

        response = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            }
        )

        answer = response["messages"][-1].content

        print("\nChatMate:", answer)

    except Exception as e:

        print("\nError:", e)