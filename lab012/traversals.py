"""BFS (queue) and DFS (explicit stack) with deterministic neighbour order.

Neighbours are processed in ascending label order (see graph.py).
Both functions accept an optional `trace` list; each step appends a dict
describing the structure state so a hand trace can be compared with the program.
"""

from collections import deque


def bfs(graph, start, trace=None):
    """Breadth-first search. Returns (order, parent, hops).

    parent[v] is the vertex that discovered v (BFS tree); hops[v] is the number of
    EDGES from start to v, which BFS minimises. Vertices are marked visited when
    ENQUEUED so nothing enters the queue twice.
    Time O(V + E), space O(V)."""
    if start not in graph:
        raise KeyError(f"unknown start vertex {start!r}")
    visited = {start}
    parent = {start: None}
    hops = {start: 0}
    queue = deque([start])
    order = []
    while queue:
        v = queue.popleft()
        order.append(v)
        for nbr, _ in graph.neighbors(v):
            if nbr not in visited:
                visited.add(nbr)
                parent[nbr] = v
                hops[nbr] = hops[v] + 1
                queue.append(nbr)
        if trace is not None:
            trace.append({"selected": v, "structure": list(queue),
                          "visited": sorted(visited, key=str), "order": list(order)})
    return order, parent, hops


def dfs(graph, start, trace=None):
    """Depth-first search with an explicit stack. Returns (order, parent).

    A vertex is marked visited when it is POPPED, and its unvisited neighbours are
    pushed in reverse label order, so the smallest label is explored first - this gives
    exactly the same order as the recursive version below.
    Time O(V + E), space O(V)."""
    if start not in graph:
        raise KeyError(f"unknown start vertex {start!r}")
    visited = set()
    parent = {start: None}
    stack = [(start, None)]
    order = []
    while stack:
        v, via = stack.pop()
        if v in visited:
            continue
        visited.add(v)
        parent[v] = via
        order.append(v)
        for nbr, _ in reversed(graph.neighbors(v)):
            if nbr not in visited:
                stack.append((nbr, v))
        if trace is not None:
            trace.append({"selected": v, "structure": [s for s, _ in stack],
                          "visited": sorted(visited, key=str), "order": list(order)})
    return order, parent


def dfs_recursive(graph, start):
    """Recursive DFS, used to cross-check the stack version. Returns the visit order."""
    if start not in graph:
        raise KeyError(f"unknown start vertex {start!r}")
    visited, order = set(), []

    def visit(v):
        visited.add(v)
        order.append(v)
        for nbr, _ in graph.neighbors(v):
            if nbr not in visited:
                visit(nbr)

    visit(start)
    return order


def path_from_parent(parent, start, target):
    """Rebuild the start->target path from a parent map, or None if unreachable."""
    if target not in parent:
        return None
    path, v = [], target
    while v is not None:
        path.append(v)
        v = parent[v]
    path.reverse()
    return path if path[0] == start else None
