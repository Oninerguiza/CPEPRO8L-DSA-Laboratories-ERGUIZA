# Dijkstra routing results (source = Gate)

## Finalisation order (hand-trace of the heap)

| Step | Vertex finalised | Distance | Tentative distances improved |
| ---: | --- | ---: | --- |
| 1 | Gate | 0 | Admin=2, Library=7 |
| 2 | Admin | 2 | Canteen=10, Library=5 |
| 3 | Library | 5 | Canteen=7, Lab=10 |
| 4 | Canteen | 7 | Gym=10 |
| 5 | Gym | 10 | Dorm=16 |
| 6 | Lab | 10 | Dorm=14 |
| 7 | Dorm | 14 | Chapel=16 |
| 8 | Chapel | 16 | - |

## Routing table

| Target | Distance | Predecessor | Shortest path | Hand-check sum |
| --- | ---: | --- | --- | --- |
| Admin | 2 | Gate | Gate → Admin | 2 = 2 |
| Annex | unreachable | - | no path | - |
| Canteen | 7 | Library | Gate → Admin → Library → Canteen | 2 + 3 + 2 = 7 |
| Chapel | 16 | Dorm | Gate → Admin → Library → Lab → Dorm → Chapel | 2 + 3 + 5 + 4 + 2 = 16 |
| Dorm | 14 | Lab | Gate → Admin → Library → Lab → Dorm | 2 + 3 + 5 + 4 = 14 |
| Gate | 0 | - | Gate | 0 |
| Gym | 10 | Canteen | Gate → Admin → Library → Canteen → Gym | 2 + 3 + 2 + 3 = 10 |
| Lab | 10 | Library | Gate → Admin → Library → Lab | 2 + 3 + 5 = 10 |
| Library | 5 | Admin | Gate → Admin → Library | 2 + 3 = 5 |

## BFS tree vs weighted shortest-path tree (same source)

| Vertex | BFS parent | BFS hops | Dijkstra predecessor | Dijkstra cost | Same parent? |
| --- | --- | ---: | --- | ---: | --- |
| Admin | Gate | 1 | Gate | 2 | yes |
| Annex | - | - | - | unreachable | - |
| Canteen | Admin | 2 | Library | 7 | **NO** |
| Chapel | Dorm | 4 | Dorm | 16 | yes |
| Dorm | Lab | 3 | Lab | 14 | yes |
| Gym | Canteen | 3 | Canteen | 10 | yes |
| Lab | Library | 2 | Library | 10 | yes |
| Library | Gate | 1 | Admin | 5 | **NO** |

## Rejected case: negative weight

`dijkstra(A-B:4, B-C:-3, A-C:2, source A)` -> **ValueError: Dijkstra's algorithm requires nonnegative edge weights**

Greedy finalisation would fix C at distance 2 (direct edge) before B is processed, but A→B→C really costs 4 + (−3) = 1. The popped distance is no longer guaranteed optimal.
