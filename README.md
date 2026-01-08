
---

# 🧠 Agentic AI Research Blog Generator (CrewAI)

A multi-agent **Agentic AI system** built using **CrewAI** that collaboratively researches a topic and generates a high-quality blog post using coordinated AI agents.

This project demonstrates **agent orchestration, task sequencing, tracing, and debugging** — similar to real-world AI systems used in industry.

---

## 🚀 Project Overview

The system uses **multiple AI agents**, each with a specific responsibility:

* 🔍 **Research Agent** → Gathers in-depth information on a topic
* ✍️ **Blog Writer Agent** → Converts research into a structured blog post
* 🧩 **Crew Orchestration** → Manages task flow and execution order

The execution is **fully traceable** using **CrewAI Tracing** and **LangSmith Tracing**.

---

## 🧱 Architecture

```text
User Input
   │
   ▼
┌──────────────────────────┐
│  Research Agent          │
│  (report_task)           │
└───────────┬──────────────┘
            ▼
┌──────────────────────────┐
│  Blog Writer Agent       │
│  (blog_writing_task)     │
└───────────┬──────────────┘
            ▼
      blog.md (Output)
```

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **CrewAI** – Multi-agent orchestration
* **LiteLLM** – Unified LLM interface
* **LangChain** – Prompt & tracing ecosystem
* **LangSmith** – Web-based tracing & observability
* **YAML** – Agent & task configuration
* **uv / pip** – Dependency management

---

## 📂 Project Structure

```text
research_blog/
├── src/research_blog/
│   ├── crew.py                # Agents, tasks, crew definition
│   ├── main.py                # Entry point
│   ├── config/
│   │   ├── agents_config.yaml # Agent definitions
│   │   └── tasks_config.yaml  # Task definitions
│   └── tools/                 # (Optional) tools
│
├── blogs/
│   └── blog.md                # Generated output
│
├── .env                       # Environment variables
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## 🤖 Agents

### 1️⃣ Report Generator Agent

* Role: Research Analyst
* Responsibility:

  * Research the given topic
  * Produce structured insights and bullet points

### 2️⃣ Blog Writer Agent

* Role: Technical Blog Writer
* Responsibility:

  * Convert research into a readable blog
  * Ensure clarity, structure, and completeness

---

## 📋 Tasks

### 📝 report_task

* Input: `{topic}`, `{current_year}`
* Output: Detailed research with 20+ bullet points

### 📝 blog_writing_task

* Input: Research output
* Output: Full blog article (`blogs/blog.md`)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd research_blog
```

### 2️⃣ Create & activate virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Configuration (`.env`)

```env
# CrewAI Tracing
CREWAI_TRACING_ENABLED=true

# LangSmith Tracing
LANGCHAIN_TRACING_V2=true
LANGSMITH_TRACING=true
LANGCHAIN_PROJECT=CrewProject
LANGSMITH_ENDPOINT=https://api.smith.langchain.com

# LLM Provider (example: Groq / OpenAI)
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

```bash
crewai run
```
---
## 🙌 Author
**Husen Basha**
---
