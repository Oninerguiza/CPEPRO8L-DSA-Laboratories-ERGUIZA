# Expected vs observed test results

| ID | Test | Expected | Observed | Status |
| --- | --- | --- | --- | --- |
| G1 | Campus graph: vertex count | `9` | `9` | PASS |
| G2 | Campus graph: undirected edge count | `11` | `11` | PASS |
| G3 | Every source vertex/edge present in structure | `[]` | `[]` | PASS |
| G4 | Undirected edge stored both ways (Gate-Admin = 2) | `(2, 2)` | `(2, 2)` | PASS |
| G5 | Directed edge stored one way only | `([('B', 1)], [])` | `([('B', 1)], [])` | PASS |
| G6 | Duplicate edge rejected | `ValueError` | `ValueError` | PASS |
| G7 | Non-numeric weight rejected | `ValueError` | `ValueError` | PASS |
| B1 | BFS from Gate | `['Gate', 'Admin', 'Library', 'Canteen', 'Lab', 'Gym', 'Dorm', 'Chapel']` | `['Gate', 'Admin', 'Library', 'Canteen', 'Lab', 'Gym', 'Dorm', 'Chapel']` | PASS |
| B2 | BFS from Chapel | `['Chapel', 'Dorm', 'Gym', 'Lab', 'Canteen', 'Library', 'Admin', 'Gate']` | `['Chapel', 'Dorm', 'Gym', 'Lab', 'Canteen', 'Library', 'Admin', 'Gate']` | PASS |
| D1 | DFS from Gate | `['Gate', 'Admin', 'Canteen', 'Gym', 'Dorm', 'Chapel', 'Lab', 'Library']` | `['Gate', 'Admin', 'Canteen', 'Gym', 'Dorm', 'Chapel', 'Lab', 'Library']` | PASS |
| D2 | DFS from Chapel | `['Chapel', 'Dorm', 'Gym', 'Canteen', 'Admin', 'Gate', 'Library', 'Lab']` | `['Chapel', 'Dorm', 'Gym', 'Canteen', 'Admin', 'Gate', 'Library', 'Lab']` | PASS |
| D3 | Stack DFS equals recursive DFS (both starts) | `True` | `True` | PASS |
| D4 | BFS/DFS never reach isolated vertex Annex | `(False, False)` | `(False, False)` | PASS |
| X1 | Isolated vertex as start: traversal is just itself | `['Annex']` | `['Annex']` | PASS |
| X2 | Cycle (triangle): BFS visits each vertex once | `['A', 'B', 'C']` | `['A', 'B', 'C']` | PASS |
| X3 | Cycle (triangle): DFS terminates, visits each once | `['A', 'B', 'C']` | `['A', 'B', 'C']` | PASS |
| X4 | Unknown start vertex rejected | `KeyError` | `KeyError` | PASS |
| H1 | BFS minimises edges: Gate->Library is 1 hop | `1` | `1` | PASS |
| S1 | Dijkstra distances from Gate | `{'Admin': 2, 'Library': 5, 'Canteen': 7, 'Lab': 10, 'Gym': 10, 'Dorm': 14, 'Chapel': 16, 'Annex': inf}` | `{'Admin': 2, 'Annex': inf, 'Canteen': 7, 'Chapel': 16, 'Dorm': 14, 'Gym': 10, 'Lab': 10, 'Library': 5}` | PASS |
| S2 | Path Gate->Chapel | `['Gate', 'Admin', 'Library', 'Lab', 'Dorm', 'Chapel']` | `['Gate', 'Admin', 'Library', 'Lab', 'Dorm', 'Chapel']` | PASS |
| S3 | Path Gate->Gym | `['Gate', 'Admin', 'Library', 'Canteen', 'Gym']` | `['Gate', 'Admin', 'Library', 'Canteen', 'Gym']` | PASS |
| S4 | Hand sum of Gate->Chapel path (2+3+5+4+2) | `16` | `16` | PASS |
| S5 | Hand sum of Gate->Gym path (2+3+2+3) | `10` | `10` | PASS |
| S6 | Unreachable target Annex: no path, distance inf | `(None, inf)` | `(None, inf)` | PASS |
| S7 | Source = target: zero-cost one-vertex path | `(['Gate'], 0)` | `(['Gate'], 0)` | PASS |
| S8 | Equal-cost alternatives: both routes cost 2, A-route kept deterministically | `(2, ['S', 'A', 'T'])` | `(2, ['S', 'A', 'T'])` | PASS |
| S9 | Cycle graph: shortest A->C is the direct edge | `(1, ['A', 'C'])` | `(1, ['A', 'C'])` | PASS |
| S10 | Directed graph: B cannot reach A | `inf` | `inf` | PASS |
| S11 | Zero-weight edge allowed | `0` | `0` | PASS |
| N1 | Negative weight is storable in Graph | `True` | `True` | PASS |
| N2 | Dijkstra rejects negative weight | `ValueError` | `ValueError` | PASS |
| N3 | Dijkstra rejects unknown source | `KeyError` | `KeyError` | PASS |
| C1 | BFS tree vs Dijkstra tree differ at exactly these vertices | `['Canteen', 'Library']` | `['Canteen', 'Library']` | PASS |
| C2 | BFS path to Gym is NOT the cheapest (cost 13 vs 10) | `(13, 10)` | `(13, 10)` | PASS |

**34 / 34 passed**
