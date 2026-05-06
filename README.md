# 🧠 Knowledge Graph Assistant - Lesson 1

> AI Agent Architecture & Agent Loop Basics | 智能体架构与智能体循环基础

## Overview 项目概述

This is the Lesson 1 demo project for the AI Agents course. Students build a knowledge graph web app that extracts structured triples (subject, relation, object) from natural language text using an AI agent loop.

## What You'll Learn 学习目标

- **AI Agent Architecture**: LLM, Tools, Memory, Planning
- **Agent Loop Pattern**: Perceive → Think → Act → Observe
- **Practical Skills**: FastAPI, OpenAI API, vis-network visualization

## Setup 环境配置

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure API key
cp .env.example .env
# Edit .env and add your OpenAI API key

# 3. Run the server
uvicorn app.main:app --reload --port 8000
```

Open http://localhost:8000 in your browser.

## Project Structure 项目结构

```
lesson1-demo/
├── app/
│   ├── main.py          # FastAPI server
│   ├── agent_loop.py    # Agent loop implementation (核心：智能体循环)
│   └── graph_store.py   # In-memory graph storage
├── static/
│   └── index.html       # Frontend with vis-network
├── docs/
│   └── lesson1-guide.md # Detailed lesson guide
├── requirements.txt
├── .env.example
└── README.md
```

## Key Concept: Agent Loop 核心概念：智能体循环

```
┌─────────────────────────────────┐
│         Agent Loop              │
│                                 │
│  Perceive → Think → Act → Observe
│      ↑                      │   │
│      └──────────────────────┘   │
│         (retry if needed)       │
└─────────────────────────────────┘
```

See `app/agent_loop.py` for the implementation.

## Course Roadmap 课程路线图

| Lesson | Topic | Feature Added |
|--------|-------|---------------|
| **1** | Agent Architecture | Basic agent loop + extraction |
| 2 | Skills | Tool use + web search |
| 3 | MCP Protocol | Standard tool protocol |
| 4 | Subagents | Multi-agent collaboration |
| 5 | Hermes/OpenClaw | Production deployment |
