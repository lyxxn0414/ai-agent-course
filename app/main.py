"""
Main FastAPI Server - 主服务器
Knowledge Graph Assistant - Lesson 1 Demo
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from app.agent_loop import run_agent_loop
from app.graph_store import graph_store

app = FastAPI(title="Knowledge Graph Assistant", version="0.1.0")

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")


class ExtractRequest(BaseModel):
    text: str


@app.get("/")
async def index():
    """Serve the frontend"""
    return FileResponse("static/index.html")


@app.get("/api/graph")
async def get_graph():
    """Return all nodes and edges (返回所有节点和边)"""
    return graph_store.get_graph()


@app.post("/api/extract")
async def extract_triples(req: ExtractRequest):
    """Extract triples from text using the agent loop (使用智能体循环从文本中抽取三元组)"""
    result = run_agent_loop(req.text)
    return result


@app.delete("/api/graph")
async def clear_graph():
    """Clear the graph (清空图)"""
    graph_store.clear()
    return {"status": "cleared"}
