"""Dijkstra's single-source shortest paths using heapq.

Valid only for NONNEGATIVE weights: once a vertex is popped with the smallest tentative
distance, no later path can improve it - a negative edge could break that guarantee, so
negative weights are rejected up front with ValueError.
"""

import heapq
import math


def dijkstra(graph, source, trace=None):
    """Return (dist, pred). dist[v] = math.inf for unreachable vertices.

    Lazy-deletion heap of (distance, label, vertex): stale entries are skipped when popped.
    A strict '<' is used for relaxation, so with equal-cost alternatives the first path
    found (smallest label order) is kept - deterministic.
    Time O((V + E) log V), space O(V + E)."""
    if source not in graph:
        raise KeyError(f"unknown source vertex {source!r}")
    if graph.has_negative_weight():
        raise ValueError("Dijkstra's algorithm requires nonnegative edge weights")
    dist = {v: math.inf for v in graph.vertices()}
    pred = {v: None for v in graph.vertices()}
    dist[source] = 0
    heap = [(0, str(source), source)]
    done = set()
    while heap:
        d, _, v = heapq.heappop(heap)
        if v in done:
            continue  # stale heap entry
        done.add(v)
        updates = []
        for nbr, w in graph.neighbors(v):
            if nbr in done:
                continue
            nd = d + w
            if nd < dist[nbr]:
                dist[nbr] = nd
                pred[nbr] = v
                heapq.heappush(heap, (nd, str(nbr), nbr))
                updates.append((nbr, nd))
        if trace is not None:
            trace.append({"finalized": v, "distance": d, "updates": updates})
    return dist, pred


def reconstruct_path(pred, dist, source, target):
    """Path source->target as a list of vertices, or None when target is unreachable."""
    if dist.get(target, math.inf) == math.inf:
        return None
    path, v = [], target
    while v is not None:
        path.append(v)
        v = pred[v]
    path.reverse()
    assert path[0] == source
    return path


def path_cost(graph, path):
    """Sum the edge weights along a path (independent check of a reconstructed route)."""
    total = 0
    for a, b in zip(path, path[1:]):
        total += dict(graph.neighbors(a))[b]
    return total
