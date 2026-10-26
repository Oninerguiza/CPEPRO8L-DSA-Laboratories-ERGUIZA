"""Generate the evidence files: edge_table.md, campus_graph.png, hand_traces.md, routing_results.md.

Run:  python run_demo.py
"""

import math

from dijkstra import dijkstra, path_cost, reconstruct_path
from graph import Graph
from traversals import bfs, dfs

START_VERTICES = ["Gate", "Chapel"]  # BFS/DFS start vertices
SOURCE = "Gate"                      # Dijkstra source (assigned source vertex)

# Fixed drawing coordinates for the campus diagram (purely cosmetic)
POS = {"Gate": (0, 2), "Admin": (2, 3.2), "Library": (3, 1.4), "Canteen": (5, 3.2),
       "Lab": (5, 0.4), "Gym": (7, 2), "Dorm": (9, 0.8), "Chapel": (10.5, 2), "Annex": (0.5, -0.2)}


def draw(g, path="campus_graph.png"):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(11, 5.5))
    for u, v, w in g.edges():
        (x1, y1), (x2, y2) = POS[u], POS[v]
        ax.plot([x1, x2], [y1, y2], color="#888", zorder=1)
        ax.text((x1 + x2) / 2, (y1 + y2) / 2, str(w), fontsize=11, ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none"), zorder=2)
    for v, (x, y) in POS.items():
        ax.scatter([x], [y], s=1700, color="#cfe3ff" if g.degree_summary()[v] else "#eee",
                   edgecolor="#335", zorder=3)
        ax.text(x, y, v, ha="center", va="center", fontsize=9, zorder=4)
    ax.set_title("Campus routing graph (undirected, weights in minutes of walking)")
    ax.set_xlim(-0.8, 11.3)
    ax.set_ylim(-0.9, 4.0)
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(path, dpi=130)


def trace_table(trace, label):
    lines = [f"| Step | Selected vertex | {label} after step | Visited set | Traversal order so far |",
             "| ---: | --- | --- | --- | --- |"]
    for i, t in enumerate(trace, 1):
        struct = "[" + ", ".join(t["structure"]) + "]" if t["structure"] else "[ ]"
        lines.append(f"| {i} | {t['selected']} | {struct} | {{{', '.join(t['visited'])}}} | "
                     f"{' → '.join(t['order'])} |")
    return "\n".join(lines)


def main():
    g, rows = Graph.from_edge_table("campus_edges.csv")
    problems = g.verify_against(rows)
    assert not problems, problems

    with open("edge_table.md", "w") as f:
        f.write(f"# Edge table ({len(g.vertices())} vertices, {len(g.edges())} edges, undirected, weighted)\n\n")
        f.write(g.edge_table_markdown() + "\n")
    draw(g)

    # ---- hand traces ----
    out = ["# Traversal traces", "",
           "Neighbour rule: ascending alphabetical order. BFS marks vertices visited when enqueued; "
           "DFS (explicit stack) marks them when popped; the top of the stack is the LAST item listed. A vertex can appear on the stack more than once; an already-visited copy is simply skipped when popped.", ""]
    for s in START_VERTICES:
        t = []
        order, _, hops = bfs(g, s, trace=t)
        out += [f"## BFS from {s}", "", "Initial queue: [" + s + "]", "", trace_table(t, "Queue"), "",
                f"**BFS order:** {' → '.join(order)}", ""]
        t = []
        order, _ = dfs(g, s, trace=t)
        out += [f"## DFS from {s}", "", "Initial stack: [" + s + "]", "", trace_table(t, "Stack"), "",
                f"**DFS order:** {' → '.join(order)}", ""]
    out.append("Annex is never reached from either start vertex (it has no edges).")
    with open("hand_traces.md", "w") as f:
        f.write("\n".join(out) + "\n")

    # ---- routing results ----
    trace = []
    dist, pred = dijkstra(g, SOURCE, trace=trace)
    res = [f"# Dijkstra routing results (source = {SOURCE})", "",
           "## Finalisation order (hand-trace of the heap)", "",
           "| Step | Vertex finalised | Distance | Tentative distances improved |", "| ---: | --- | ---: | --- |"]
    for i, t in enumerate(trace, 1):
        upd = ", ".join(f"{v}={d}" for v, d in t["updates"]) or "-"
        res.append(f"| {i} | {t['finalized']} | {t['distance']} | {upd} |")
    res += ["", "## Routing table", "",
            "| Target | Distance | Predecessor | Shortest path | Hand-check sum |", "| --- | ---: | --- | --- | --- |"]
    for v in g.vertices():
        p = reconstruct_path(pred, dist, SOURCE, v)
        if p is None:
            res.append(f"| {v} | unreachable | - | no path | - |")
        else:
            wts = [dict(g.neighbors(a))[b] for a, b in zip(p, p[1:])]
            check = " + ".join(map(str, wts)) + f" = {path_cost(g, p)}" if wts else "0"
            res.append(f"| {v} | {dist[v]} | {pred[v] or '-'} | {' → '.join(p)} | {check} |")

    _, bpar, hops = bfs(g, SOURCE)
    res += ["", "## BFS tree vs weighted shortest-path tree (same source)", "",
            "| Vertex | BFS parent | BFS hops | Dijkstra predecessor | Dijkstra cost | Same parent? |",
            "| --- | --- | ---: | --- | ---: | --- |"]
    for v in g.vertices():
        if v == SOURCE:
            continue
        if v in bpar:
            same = "yes" if bpar[v] == pred[v] else "**NO**"
            res.append(f"| {v} | {bpar[v]} | {hops[v]} | {pred[v]} | {dist[v]} | {same} |")
        else:
            res.append(f"| {v} | - | - | - | unreachable | - |")
    res += ["", "## Rejected case: negative weight", ""]
    bad = Graph(directed=True)
    bad.add_edge("A", "B", 4)
    bad.add_edge("B", "C", -3)
    bad.add_edge("A", "C", 2)
    try:
        dijkstra(bad, "A")
    except ValueError as e:
        res.append(f"`dijkstra(A-B:4, B-C:-3, A-C:2, source A)` -> **ValueError: {e}**")
        res.append("")
        res.append("Greedy finalisation would fix C at distance 2 (direct edge) before B is processed, "
                   "but A→B→C really costs 4 + (−3) = 1. The popped distance is no longer guaranteed optimal.")
    with open("routing_results.md", "w") as f:
        f.write("\n".join(res) + "\n")
    print("generated edge_table.md, campus_graph.png, hand_traces.md, routing_results.md")


if __name__ == "__main__":
    main()
