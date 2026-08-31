# 🤖 ChatMate — AI Chatbot with Tool Calling

ChatMate is a simple, end-to-end Generative AI chatbot built with **Python, LangChain, Groq, and Streamlit**.

The project demonstrates how a Large Language Model can interact with external tools through **AI agent tool calling** to perform tasks such as mathematical calculations, web searches, unit conversions, and text analysis.

The primary goal of this project is to understand the practical fundamentals of **LLM-based AI agents and tool calling** without introducing unnecessary complexity.

---

## 🚀 Features

- 💬 Interactive chatbot interface using Streamlit
- 🤖 Groq-powered Large Language Model
- 🧠 AI agent with tool calling
- 🧮 Mathematical calculations
- 🔍 Web search for current information
- 🌡️ Celsius ↔ Fahrenheit conversion
- 📏 Kilometers ↔ Miles conversion
- 🕐 Current date and time
- 📝 Basic text analysis
- 🛡️ Environment-based API key management
- 📦 Modular project structure

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | Agent and tool framework |
| Groq | Large Language Model provider |
| Streamlit | Web-based chatbot interface |
| DDGS | Web search |
| Pydantic | Tool input validation |
| python-dotenv | Environment variable management |
| Git | Version control |

---

## 🏗️ Project Architecture

```text
                    👤 User
                       │
                       ▼
              ┌─────────────────┐
              │    Streamlit    │
              │     app.py      │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │    AI Agent     │
              │    agent.py     │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │    Groq LLM     │
              └────────┬────────┘
                       │
                 Tool Selection
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
      Calculator   Web Search   Converters
          │            │            │
          └────────────┼────────────┘
                       │
                       ▼
                  Tool Result
                       │
                       ▼
                    AI Agent
                       │
                       ▼
                 Final Response
                       │
                       ▼
                  Streamlit UI