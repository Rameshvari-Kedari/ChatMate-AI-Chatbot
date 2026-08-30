# 🤖 ChatMate — Simple AI Chatbot

ChatMate is a simple GenAI chatbot built with Python, LangChain, Groq, and Streamlit.

The project demonstrates how an AI agent can use different tools to perform tasks instead of relying only on the language model.

## 🚀 Features

* 💬 AI chatbot
* 🤖 Groq LLM
* 🔍 Web search
* 🧮 Calculator
* 🌡️ Temperature conversion
* 📏 Unit conversion
* 🔤 Text analysis
* 🛠️ Custom LangChain tools
* 🧠 AI agent with tool calling
* 🎨 Streamlit interface

## ❌ Not Used

This project intentionally does not use:

* RAG
* Vector databases
* Embeddings
* Long-term memory
* Multi-agent systems
* Complex databases

The goal is to understand the fundamentals of GenAI agents and tool calling first.

## 🏗️ Project Structure

```text
ChatMate/
│
├── app.py              # Streamlit application
├── agent.py            # LLM and AI agent
├── tools.py            # Custom and external tools
├── requirements.txt    # Python dependencies
├── .env                # API keys
├── .gitignore          # Files ignored by Git
└── README.md           # Project documentation
```

## 🔄 Architecture

```text
User
  ↓
Streamlit
  ↓
AI Agent
  ↓
Groq LLM
  ↓
Tool Selection
  ↓
┌──────────────┬────────────┬──────────────┐
│ Web Search   │ Calculator │ Converters   │
└──────────────┴────────────┴──────────────┘
  ↓
Tool Result
  ↓
Groq LLM
  ↓
Final Response
  ↓
User
```

## 🛠️ Technologies

* Python
* LangChain
* Groq
* Streamlit
* Python-dotenv
* DuckDuckGo Search

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Open the project

```bash
cd ChatMate
```

### 3. Create virtual environment

```bash
python -m venv .venv
```

### 4. Activate virtual environment

Windows:

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure API key

Create a `.env` file:

```text
GROQ_API_KEY=your_groq_api_key
```

### 7. Run the application

```bash
streamlit run app.py
```

## 💡 Example Questions

```text
What is artificial intelligence?

What is 25 * 45?

Search for the latest AI news.

Convert 37 Celsius to Fahrenheit.

Convert 10 kilometers to miles.

Count the words in this sentence.
```

## 🎯 Learning Objectives

This project helps demonstrate:

1. LLM invocation
2. LangChain
3. Custom tools
4. Tool calling
5. AI agents
6. Multiple tools
7. Agent execution
8. Streamlit integration

## 📌 Future Improvements

Possible future versions can add:

* Conversation memory
* RAG
* Vector database
* Authentication
* More tools
* Database integration
* Deployment

These features are intentionally excluded from the first version to keep the project simple and understandable.
