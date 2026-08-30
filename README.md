# AI Learning Assistant

An AI-powered learning and career research assistant built using **LangChain**, **Google Gemini**, and the **Model Context Protocol (MCP)**.

The application helps users learn about different topics and dynamically uses external MCP tools when needed. It includes input guardrails, a custom system prompt, multiple MCP server integrations, and a Human-in-the-Loop (HITL) workflow for providing additional learning resources such as structured roadmaps and relevant YouTube videos.

---

## Features

- 🤖 AI-powered learning assistant using Google Gemini
- 🔗 LangChain agent integration for LLM and tool-calling logic
- 🧩 Multiple MCP server integration (Playwright MCP + YouTube MCP)
- 🎥 YouTube MCP for finding relevant learning videos
- 🌐 Playwright MCP for browser-based interactions
- 🛡️ Input guardrails for safer, cleaner user input
- 🧠 Custom system prompt for controlling AI behavior and tool usage
- 👤 Human-in-the-Loop (HITL) interaction after every AI response
- 🗺️ Structured learning roadmap generation
- 📚 YouTube learning resource recommendations
- 💻 Simple, lightweight command-line interface (no unnecessary UI complexity)

---

## Project Architecture

```
User Input
    │
    ▼
Guardrails
    │
    ▼
Gemini AI Agent
    │
    ├───────────────┐
    ▼               ▼
YouTube MCP     Playwright MCP
    │               │
    └───────┬───────┘
            ▼
      AI Response
            │
            ▼
Human-in-the-Loop
            │
     ┌──────┼───────┐
     ▼      ▼       ▼
  Roadmap Videos    Both
```

The AI agent receives the user's (guardrail-checked) query, decides — based on the custom system prompt — whether an MCP tool is needed, and generates an initial response. The user is then given the option, through the Human-in-the-Loop step, to request further learning resources before the final response is presented.

---

## Human-in-the-Loop Options

After receiving the initial AI response, the user can choose additional learning resources:

**Option 1: Structured Roadmap**
The assistant generates a structured learning roadmap based on the user's query.

**Option 2: Relevant YouTube Videos**
The assistant uses the YouTube MCP tools to find relevant educational videos.

**Option 3: Both**
The user receives both a structured learning roadmap and relevant YouTube learning resources.

**Option 4: No Additional Resources**
The assistant continues without generating any additional resources.

---

## Project Structure

```
ai-learning-assistant/
│
├── main.py
├── mcp_client.py
├── guardrails.py
├── system_prompt.py
├── hitl.py
│
├── requirements.txt
├── .env
├── .gitignore
│
└── README.md
```

### `main.py`
The main entry point of the application. It handles:
- User input
- Guardrail validation
- AI agent execution
- MCP tool integration
- Human-in-the-Loop workflow

### `mcp_client.py`
Responsible for connecting to and loading the available MCP servers and their tools using `langchain-mcp-adapters`.

### `guardrails.py`
Validates user input before it reaches the AI model. The guardrails handle:
- Empty input
- Very long input
- Basic prompt injection attempts
- Restricted input patterns

### `system_prompt.py`
Contains the custom system prompt used to control the behavior of the AI Learning Assistant. It defines:
- How the assistant should respond
- When MCP tools should be used
- When YouTube MCP should be used
- When Playwright MCP should be used
- Response formatting and behavior

### `hitl.py`
Handles the Human-in-the-Loop interaction. Users can choose whether they want:
- A structured roadmap
- Relevant YouTube videos
- Both
- No additional resources

---

## MCP Servers Used

### YouTube MCP
Used for finding relevant educational YouTube videos based on the user's learning query.

**Examples:**
- "Suggest me a YouTube tutorial for LangChain"
- "Find me a good video to learn Python"

### Playwright MCP
The official Microsoft Playwright MCP server, used for browser-based tasks and web interactions when external navigation is required. The AI agent is instructed, through the system prompt, to use browser tools only when necessary.

---

## Installation

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
```

Move into the project folder:

```bash
cd ai-learning-assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

**Activate on Windows:**

```bash
venv\Scripts\activate
```

**Activate on macOS/Linux:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the `.env` File

Create a file named `.env` in the project root and add your API key:

```
GOOGLE_API_KEY=your_google_gemini_api_key
```

Replace `your_google_gemini_api_key` with your actual Gemini API key.

> **Important:** Do not share or commit your `.env` file, as it contains your private API credentials. Both `.env` and `venv/` are excluded via `.gitignore`.

### 5. Node.js Requirement

This project uses ready-made MCP servers launched via `npx`, so **Node.js must be installed** on your system beforehand. No custom MCP servers are built for this project — both Playwright MCP and YouTube MCP are official/ready-made servers run directly through `npx`.

---

## Running the Project

After installing the dependencies and configuring your API key, run:

```bash
python main.py
```

The application will load the MCP tools and start the AI Learning Assistant.

**Example:**

```
Loading MCP tools...
Loaded MCP tools.

AI Learning Assistant

Type exit to quit

You:
```

---

## Example Usage

### General Question

```
You: What is Machine Learning?
```

The assistant answers the question directly, without invoking any MCP tool.

### Video Request

```
You: Suggest me a good YouTube tutorial for MCP
```

The assistant recognizes the intent and uses the YouTube MCP tools to find relevant learning resources.

### Additional Resources

After receiving an answer, the user can select:

```
1. Structured Roadmap
2. Relevant YouTube Videos
3. Both Roadmap and YouTube Videos
4. No, thanks
```

---

## Technologies Used

- Python
- LangChain
- Google Gemini (via `langchain-google-genai`)
- Model Context Protocol (MCP)
- YouTube MCP Server
- Playwright MCP Server (official Microsoft server, `@playwright/mcp`)
- Node.js / NPX

---

## Design Principles

This project was intentionally kept simple and focused rather than built as a large multi-agent system:

- No FastAPI, no LangGraph, no HTML/CSS/JavaScript
- No custom MCP servers — only ready-made servers run via `npx`
- No unnecessary configuration files (e.g., no separate MCP JSON config file, since the Python MCP client configures servers directly)
- Command-line interface first, with a UI layer considered only as a future improvement
- Exactly two MCP servers, chosen deliberately for relevance to the assistant's purpose, rather than adding extra servers for the sake of it

---

## Future Improvements

Possible future improvements include:

- Streamlit or web-based user interface
- Conversation memory
- More MCP server integrations
- Advanced guardrails
- Personalized learning recommendations
- Progress tracking
- User authentication
- Persistent chat history

---

## Author

**Ronak De**