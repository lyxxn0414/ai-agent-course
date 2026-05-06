"""
Graph Store - 图存储模块
A simple in-memory knowledge graph storage.
Stores nodes and edges (triples: subject → relation → object).
"""

from dataclasses import dataclass, field


@dataclass
class GraphStore:
    """In-memory graph storage (内存图存储)"""
    nodes: dict[str, dict] = field(default_factory=dict)  # id -> {id, label}
    edges: list[dict] = field(default_factory=list)        # [{from, to, label}]

    def add_triple(self, subject: str, relation: str, obj: str) -> None:
        """Add a knowledge triple to the graph (添加知识三元组)"""
        # Ensure both nodes exist
        for entity in (subject, obj):
            if entity not in self.nodes:
                self.nodes[entity] = {"id": entity, "label": entity}
        # Add edge
        self.edges.append({"from": subject, "to": obj, "label": relation})

    def get_graph(self) -> dict:
        """Return full graph as nodes + edges"""
        return {
            "nodes": list(self.nodes.values()),
            "edges": self.edges,
        }

    def clear(self) -> None:
        """Clear all data (清空图数据)"""
        self.nodes.clear()
        self.edges.clear()


# Singleton instance (全局单例)
graph_store = GraphStore()
