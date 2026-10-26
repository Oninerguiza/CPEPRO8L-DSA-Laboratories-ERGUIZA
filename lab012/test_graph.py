"""Automated tests with an expected/observed table.

Run:  python test_graph.py            (unittest output)
      python test_graph.py --report   (also writes test_report.md)

The assigned graph is loaded from campus_edges.csv; swap in your instructor's data by
replacing that file (columns u,v,weight; an empty v declares an isolated vertex).
"""

import math
import sys
import unittest

from dijkstra import dijkstra, path_cost, reconstruct_path
from graph import Graph
from traversals import bfs, dfs, dfs_recursive, path_from_parent

INF = math.inf


def campus():
    g, rows = Graph.from_edge_table("campus_edges.csv")
    return g, rows


def raises(exc, func):
    try:
        func()
    except exc:
        return exc.__name__
    except Exception as other:  # wrong exception type
        return type(other).__name__
    return "no error"


def small(edges, directed=False, extra_vertices=()):
    g = Graph(directed=directed)
    for v in extra_vertices:
        g.add_vertex(v)
    for u, v, w in edges:
        g.add_edge(u, v, w)
    return g


def dijkstra_dists(g, s):
    return dijkstra(g, s)[0]


def path(g, s, t):
    d, p = dijkstra(g, s)
    return reconstruct_path(p, d, s, t)


def bfs_vs_dijkstra_differences():
    g, _ = campus()
    _, bpar, _ = bfs(g, "Gate")
    _, dpred = dijkstra(g, "Gate")
    return sorted(v for v in g.vertices() if v != "Gate" and v in bpar and bpar[v] != dpred[v])


def neg_dijkstra():
    return raises(ValueError, lambda: dijkstra(small([("A", "B", -1)]), "A"))


def neg_graph_is_storable():
    g = small([("A", "B", -1)])
    return g.has_negative_weight()


G, ROWS = campus()
DIAMOND = small([("S", "A", 1), ("S", "B", 1), ("A", "T", 1), ("B", "T", 1)])
TRI = small([("A", "B", 1), ("B", "C", 1), ("C", "A", 1)])

# (id, description, expected, observed-callable)
CASES = [
    ("G1", "Campus graph: vertex count", 9, lambda: len(G.vertices())),
    ("G2", "Campus graph: undirected edge count", 11, lambda: len(G.edges())),
    ("G3", "Every source vertex/edge present in structure", [], lambda: G.verify_against(ROWS)),
    ("G4", "Undirected edge stored both ways (Gate-Admin = 2)",
     (2, 2), lambda: (dict(G.neighbors("Gate"))["Admin"], dict(G.neighbors("Admin"))["Gate"])),
    ("G5", "Directed edge stored one way only",
     ([("B", 1)], []), lambda: (small([("A", "B", 1)], True).neighbors("A"),
                                small([("A", "B", 1)], True).neighbors("B"))),
    ("G6", "Duplicate edge rejected", "ValueError",
     lambda: raises(ValueError, lambda: small([("A", "B", 1), ("A", "B", 2)], True))),
    ("G7", "Non-numeric weight rejected", "ValueError",
     lambda: raises(ValueError, lambda: small([("A", "B", "heavy")]))),
    ("B1", "BFS from Gate", ["Gate", "Admin", "Library", "Canteen", "Lab", "Gym", "Dorm", "Chapel"],
     lambda: bfs(G, "Gate")[0]),
    ("B2", "BFS from Chapel", ["Chapel", "Dorm", "Gym", "Lab", "Canteen", "Library", "Admin", "Gate"],
     lambda: bfs(G, "Chapel")[0]),
    ("D1", "DFS from Gate", ["Gate", "Admin", "Canteen", "Gym", "Dorm", "Chapel", "Lab", "Library"],
     lambda: dfs(G, "Gate")[0]),
    ("D2", "DFS from Chapel", ["Chapel", "Dorm", "Gym", "Canteen", "Admin", "Gate", "Library", "Lab"],
     lambda: dfs(G, "Chapel")[0]),
    ("D3", "Stack DFS equals recursive DFS (both starts)", True,
     lambda: all(dfs(G, s)[0] == dfs_recursive(G, s) for s in ("Gate", "Chapel", "Lab"))),
    ("D4", "BFS/DFS never reach isolated vertex Annex", (False, False),
     lambda: ("Annex" in bfs(G, "Gate")[0], "Annex" in dfs(G, "Gate")[0])),
    ("X1", "Isolated vertex as start: traversal is just itself", ["Annex"], lambda: bfs(G, "Annex")[0]),
    ("X2", "Cycle (triangle): BFS visits each vertex once", ["A", "B", "C"], lambda: bfs(TRI, "A")[0]),
    ("X3", "Cycle (triangle): DFS terminates, visits each once", ["A", "B", "C"], lambda: dfs(TRI, "A")[0]),
    ("X4", "Unknown start vertex rejected", "KeyError", lambda: raises(KeyError, lambda: bfs(G, "Nowhere"))),
    ("H1", "BFS minimises edges: Gate->Library is 1 hop", 1, lambda: bfs(G, "Gate")[2]["Library"]),
    ("S1", "Dijkstra distances from Gate",
     {"Admin": 2, "Library": 5, "Canteen": 7, "Lab": 10, "Gym": 10, "Dorm": 14, "Chapel": 16, "Annex": INF},
     lambda: {v: d for v, d in dijkstra_dists(G, "Gate").items() if v != "Gate"}),
    ("S2", "Path Gate->Chapel", ["Gate", "Admin", "Library", "Lab", "Dorm", "Chapel"],
     lambda: path(G, "Gate", "Chapel")),
    ("S3", "Path Gate->Gym", ["Gate", "Admin", "Library", "Canteen", "Gym"], lambda: path(G, "Gate", "Gym")),
    ("S4", "Hand sum of Gate->Chapel path (2+3+5+4+2)", 16,
     lambda: path_cost(G, path(G, "Gate", "Chapel"))),
    ("S5", "Hand sum of Gate->Gym path (2+3+2+3)", 10, lambda: path_cost(G, path(G, "Gate", "Gym"))),
    ("S6", "Unreachable target Annex: no path, distance inf", (None, INF),
     lambda: (path(G, "Gate", "Annex"), dijkstra_dists(G, "Gate")["Annex"])),
    ("S7", "Source = target: zero-cost one-vertex path", (["Gate"], 0),
     lambda: (path(G, "Gate", "Gate"), dijkstra_dists(G, "Gate")["Gate"])),
    ("S8", "Equal-cost alternatives: both routes cost 2, A-route kept deterministically",
     (2, ["S", "A", "T"]), lambda: (dijkstra_dists(DIAMOND, "S")["T"], path(DIAMOND, "S", "T"))),
    ("S9", "Cycle graph: shortest A->C is the direct edge", (1, ["A", "C"]),
     lambda: (dijkstra_dists(TRI, "A")["C"], path(TRI, "A", "C"))),
    ("S10", "Directed graph: B cannot reach A", INF,
     lambda: dijkstra_dists(small([("A", "B", 1)], True), "B")["A"]),
    ("S11", "Zero-weight edge allowed", 0, lambda: dijkstra_dists(small([("A", "B", 0)]), "A")["B"]),
    ("N1", "Negative weight is storable in Graph", True, neg_graph_is_storable),
    ("N2", "Dijkstra rejects negative weight", "ValueError", neg_dijkstra),
    ("N3", "Dijkstra rejects unknown source", "KeyError", lambda: raises(KeyError, lambda: dijkstra(G, "Nowhere"))),
    ("C1", "BFS tree vs Dijkstra tree differ at exactly these vertices", ["Canteen", "Library"],
     bfs_vs_dijkstra_differences),
    ("C2", "BFS path to Gym is NOT the cheapest (cost 13 vs 10)", (13, 10),
     lambda: (path_cost(G, path_from_parent(bfs(G, "Gate")[1], "Gate", "Gym")),
              dijkstra_dists(G, "Gate")["Gym"])),
]


class GraphTests(unittest.TestCase):
    pass


def _make(case):
    cid, desc, expected, observed = case

    def test(self):
        self.assertEqual(observed(), expected, f"{cid}: {desc}")
    return test


for _case in CASES:
    setattr(GraphTests, f"test_{_case[0]}", _make(_case))


def fmt(x):
    return "inf" if x == INF else str(x).replace("inf", "inf")


def write_report(path="test_report.md"):
    lines = ["# Expected vs observed test results", "",
             "| ID | Test | Expected | Observed | Status |", "| --- | --- | --- | --- | --- |"]
    passed = 0
    for cid, desc, expected, observed in CASES:
        got = observed()
        ok = got == expected
        passed += ok
        esc = lambda s: str(s).replace("|", "\\|")
        lines.append(f"| {cid} | {esc(desc)} | `{esc(fmt(expected))}` | `{esc(fmt(got))}` | {'PASS' if ok else 'FAIL'} |")
    lines += ["", f"**{passed} / {len(CASES)} passed**"]
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")
    return passed == len(CASES)


if __name__ == "__main__":
    if "--report" in sys.argv:
        sys.argv.remove("--report")
        write_report()
    unittest.main(verbosity=1)
