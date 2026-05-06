# Lesson 1: AI Agent Architecture & Agent Loop
# 第一课：智能体架构与智能体循环

---

## Part 1: AI Agent Architecture Theory 智能体架构理论

### What is an AI Agent? 什么是智能体？

An AI Agent is a system that can **perceive** its environment, **reason** about what to do, and **take actions** to achieve goals. Unlike a simple chatbot that just responds to prompts, an agent has:

1. **LLM (大语言模型)** - The "brain" that reasons and generates
2. **Tools (工具)** - External capabilities the agent can use (APIs, databases, code execution)
3. **Memory (记忆)** - Short-term (conversation) and long-term (knowledge base) storage
4. **Planning (规划)** - The ability to break tasks into steps and decide what to do next

```
┌──────────────────────────────────────┐
│              AI Agent                │
│                                      │
│  ┌─────┐  ┌───────┐  ┌──────────┐  │
│  │ LLM │  │ Tools │  │  Memory  │  │
│  └──┬──┘  └───┬───┘  └────┬─────┘  │
│     │         │            │         │
│     └─────────┴────────────┘         │
│              Planning                │
└──────────────────────────────────────┘
```

### Key Insight 关键洞察

The LLM alone is **stateless** - it just maps input → output. The Agent adds **state** (memory), **actions** (tools), and **iteration** (loops).

---

## Part 2: The Agent Loop 智能体循环

The Agent Loop is the core execution pattern. Every agent, from simple to complex, follows this cycle:

### Perceive → Think → Act → Observe (感知→思考→行动→观察)

1. **Perceive (感知)**: Receive and preprocess input from the environment
2. **Think (思考)**: Use the LLM to reason about what to do
3. **Act (行动)**: Execute the chosen action (call API, store data, etc.)
4. **Observe (观察)**: Evaluate the result - was it successful? Should we continue?

```python
while not done:
    perception = perceive(environment)    # 感知
    plan = think(perception, memory)      # 思考
    result = act(plan)                    # 行动
    done = observe(result)               # 观察
```

### Why Loop? 为什么要循环？

- The first attempt may not be perfect
- Complex tasks require multiple steps
- The agent can self-correct based on feedback

---

## Part 3: Hands-on - Scaffolding with a Coding Agent 动手：用编程智能体搭建项目

### Exercise 3.1: Use a Coding Agent

Use your preferred coding agent (Cursor, GitHub Copilot, Hermes Agent) to:

1. Create the project structure
2. Generate the FastAPI boilerplate
3. Create the frontend HTML

**Prompt to try:**
> "Create a FastAPI project with a single HTML frontend that displays a knowledge graph using vis-network. Include endpoints for getting/clearing the graph and extracting triples from text."

### Reflection 思考

- How did the coding agent interpret your instructions?
- What did it get right/wrong?
- How is the coding agent itself an example of the agent loop?

---

## Part 4: Hands-on - Implementing the Agent Loop 动手：实现智能体循环

### Exercise 4.1: Read `app/agent_loop.py`

Study the implementation. Identify:
- Where is the **Perceive** step?
- Where is the **Think** step?
- Where is the **Act** step?
- Where is the **Observe** step?
- What condition causes the loop to repeat?

### Exercise 4.2: Modify the Loop

Try these modifications:
1. Change `CONFIDENCE_THRESHOLD` to 0.9 - what happens?
2. Add a counter for total LLM tokens used
3. Add a new extraction type: extract sentiment along with triples

### Exercise 4.3: Test with Different Texts

Try extracting from:
- A Wikipedia paragraph about a famous person
- A news article
- A technical description

---

## Exercises & Reflection 练习与思考

### Questions 思考题

1. What are the tradeoffs of setting MAX_ITERATIONS higher vs lower?
2. How could you add "memory" to this agent so it remembers past extractions?
3. What "tools" could you add to make the agent more capable?
4. How is this simple loop related to more complex agent architectures (ReAct, AutoGPT)?

### Preview of Next Lesson 下节预告

In Lesson 2, we'll add **Skills** to our agent - giving it the ability to:
- Search the web for additional context
- Validate triples against existing knowledge
- Export the graph in different formats

---

## Running the Demo 运行演示

```bash
cd lesson1-demo
pip install -r requirements.txt
cp .env.example .env  # Add your API key
uvicorn app.main:app --reload --port 8000
```

Open http://localhost:8000 and try extracting triples from text!
