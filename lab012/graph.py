"""Adjacency-list graph model (directed or undirected, weighted or unweighted).

Neighbour-ordering rule (used by every algorithm in this project):
    neighbours are always visited in ASCENDING label order (alphabetical).
This makes BFS, DFS and Dijkstra fully deterministic.
"""

import csv
import math


class Graph:
    def __init__(self, directed=False, weighted=True):
        self.directed = directed
        self.weighted = weighted
        self._adj = {}  # vertex -> {neighbour: weight}

    # ---- construction -------------------------------------------------
    def add_vertex(self, v):
        self._adj.setdefault(v, {})

    def add_edge(self, u, v, weight=1):
        if not self.weighted:
            weight = 1
        if isinstance(weight, bool) or not isinstance(weight, (int, float)) or math.isnan(weight):
            raise ValueError(f"invalid weight {weight!r} on edge {u}-{v}")
        if u in self._adj and v in self._adj[u]:
            raise ValueError(f"duplicate edge {u}->{v}")
        self.add_vertex(u)
        self.add_vertex(v)
        self._adj[u][v] = weight
        if not self.directed:
            self._adj[v][u] = weight

    # ---- queries ------------------------------------------------------
    def __contains__(self, v):
        return v in self._adj

    def vertices(self):
        return sorted(self._adj, key=str)

    def neighbors(self, v):
        """[(neighbour, weight), ...] in ascending label order."""
        return sorted(self._adj[v].items(), key=lambda item: str(item[0]))

    def edges(self):
        """Each edge once: (u, v, weight). Undirected edges are listed with u < v."""
        out = []
        for u in self.vertices():
            for v, w in self.neighbors(u):
                if self.directed or str(u) <= str(v):
                    out.append((u, v, w))
        return out

    def has_negative_weight(self):
        return any(w < 0 for _, _, w in self.edges())

    def degree_summary(self):
        return {v: len(self._adj[v]) for v in self.vertices()}

    # ---- loading and validation ---------------------------------------
    @classmethod
    def from_edge_table(cls, path, directed=False, weighted=True):
        """Load a CSV with header u,v,weight.

        A row with an empty v declares an isolated vertex (e.g. "Annex,,").
        Returns (graph, rows) where rows is the parsed source data.
        """
        g = cls(directed=directed, weighted=weighted)
        rows = []
        with open(path, newline="") as f:
            for rec in csv.DictReader(f):
                u, v = rec["u"].strip(), (rec["v"] or "").strip()
                w = rec.get("weight", "")
                w = float(w) if w not in ("", None) else 1
                if w == int(w):
                    w = int(w)
                rows.append((u, v, w))
                if v == "":
                    g.add_vertex(u)
                else:
                    g.add_edge(u, v, w)
        return g, rows

    def verify_against(self, rows):
        """Check that every vertex and edge of the source rows is in the structure.

        Returns a list of problems (empty list = verified)."""
        problems = []
        expected_vertices, expected_edges = set(), set()
        for u, v, w in rows:
            expected_vertices.add(u)
            if v == "":
                continue
            expected_vertices.add(v)
            expected_edges.add((u, v, w if self.weighted else 1))
        for u, v, w in expected_edges:
            if u not in self or v not in self._adj[u] or self._adj[u][v] != w:
                problems.append(f"missing/incorrect edge {u}->{v} ({w})")
            if not self.directed and (v not in self or u not in self._adj[v]):
                problems.append(f"missing reverse edge {v}->{u}")
        for v in expected_vertices:
            if v not in self:
                problems.append(f"missing vertex {v}")
        if set(self.vertices()) != expected_vertices:
            problems.append("structure has vertices not present in source data")
        if len(self.edges()) != len(expected_edges):
            problems.append(f"edge count {len(self.edges())} != source {len(expected_edges)}")
        return problems

    def edge_table_markdown(self):
        arrow = "->" if self.directed else "--"
        lines = ["| # | Edge | Weight |", "| ---: | --- | ---: |"]
        for i, (u, v, w) in enumerate(self.edges(), 1):
            lines.append(f"| {i} | {u} {arrow} {v} | {w} |")
        isolated = [v for v, d in self.degree_summary().items() if d == 0]
        if isolated:
            lines.append(f"\nIsolated vertices (no edges): {', '.join(map(str, isolated))}")
        return "\n".join(lines)
