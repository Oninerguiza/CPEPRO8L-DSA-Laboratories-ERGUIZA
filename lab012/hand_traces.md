# Traversal traces

Neighbour rule: ascending alphabetical order. BFS marks vertices visited when enqueued; DFS (explicit stack) marks them when popped; the top of the stack is the LAST item listed. A vertex can appear on the stack more than once; an already-visited copy is simply skipped when popped.

## BFS from Gate

Initial queue: [Gate]

| Step | Selected vertex | Queue after step | Visited set | Traversal order so far |
| ---: | --- | --- | --- | --- |
| 1 | Gate | [Admin, Library] | {Admin, Gate, Library} | Gate |
| 2 | Admin | [Library, Canteen] | {Admin, Canteen, Gate, Library} | Gate → Admin |
| 3 | Library | [Canteen, Lab] | {Admin, Canteen, Gate, Lab, Library} | Gate → Admin → Library |
| 4 | Canteen | [Lab, Gym] | {Admin, Canteen, Gate, Gym, Lab, Library} | Gate → Admin → Library → Canteen |
| 5 | Lab | [Gym, Dorm] | {Admin, Canteen, Dorm, Gate, Gym, Lab, Library} | Gate → Admin → Library → Canteen → Lab |
| 6 | Gym | [Dorm] | {Admin, Canteen, Dorm, Gate, Gym, Lab, Library} | Gate → Admin → Library → Canteen → Lab → Gym |
| 7 | Dorm | [Chapel] | {Admin, Canteen, Chapel, Dorm, Gate, Gym, Lab, Library} | Gate → Admin → Library → Canteen → Lab → Gym → Dorm |
| 8 | Chapel | [ ] | {Admin, Canteen, Chapel, Dorm, Gate, Gym, Lab, Library} | Gate → Admin → Library → Canteen → Lab → Gym → Dorm → Chapel |

**BFS order:** Gate → Admin → Library → Canteen → Lab → Gym → Dorm → Chapel

## DFS from Gate

Initial stack: [Gate]

| Step | Selected vertex | Stack after step | Visited set | Traversal order so far |
| ---: | --- | --- | --- | --- |
| 1 | Gate | [Library, Admin] | {Gate} | Gate |
| 2 | Admin | [Library, Library, Canteen] | {Admin, Gate} | Gate → Admin |
| 3 | Canteen | [Library, Library, Library, Gym] | {Admin, Canteen, Gate} | Gate → Admin → Canteen |
| 4 | Gym | [Library, Library, Library, Lab, Dorm] | {Admin, Canteen, Gate, Gym} | Gate → Admin → Canteen → Gym |
| 5 | Dorm | [Library, Library, Library, Lab, Lab, Chapel] | {Admin, Canteen, Dorm, Gate, Gym} | Gate → Admin → Canteen → Gym → Dorm |
| 6 | Chapel | [Library, Library, Library, Lab, Lab] | {Admin, Canteen, Chapel, Dorm, Gate, Gym} | Gate → Admin → Canteen → Gym → Dorm → Chapel |
| 7 | Lab | [Library, Library, Library, Lab, Library] | {Admin, Canteen, Chapel, Dorm, Gate, Gym, Lab} | Gate → Admin → Canteen → Gym → Dorm → Chapel → Lab |
| 8 | Library | [Library, Library, Library, Lab] | {Admin, Canteen, Chapel, Dorm, Gate, Gym, Lab, Library} | Gate → Admin → Canteen → Gym → Dorm → Chapel → Lab → Library |

**DFS order:** Gate → Admin → Canteen → Gym → Dorm → Chapel → Lab → Library

## BFS from Chapel

Initial queue: [Chapel]

| Step | Selected vertex | Queue after step | Visited set | Traversal order so far |
| ---: | --- | --- | --- | --- |
| 1 | Chapel | [Dorm] | {Chapel, Dorm} | Chapel |
| 2 | Dorm | [Gym, Lab] | {Chapel, Dorm, Gym, Lab} | Chapel → Dorm |
| 3 | Gym | [Lab, Canteen] | {Canteen, Chapel, Dorm, Gym, Lab} | Chapel → Dorm → Gym |
| 4 | Lab | [Canteen, Library] | {Canteen, Chapel, Dorm, Gym, Lab, Library} | Chapel → Dorm → Gym → Lab |
| 5 | Canteen | [Library, Admin] | {Admin, Canteen, Chapel, Dorm, Gym, Lab, Library} | Chapel → Dorm → Gym → Lab → Canteen |
| 6 | Library | [Admin, Gate] | {Admin, Canteen, Chapel, Dorm, Gate, Gym, Lab, Library} | Chapel → Dorm → Gym → Lab → Canteen → Library |
| 7 | Admin | [Gate] | {Admin, Canteen, Chapel, Dorm, Gate, Gym, Lab, Library} | Chapel → Dorm → Gym → Lab → Canteen → Library → Admin |
| 8 | Gate | [ ] | {Admin, Canteen, Chapel, Dorm, Gate, Gym, Lab, Library} | Chapel → Dorm → Gym → Lab → Canteen → Library → Admin → Gate |

**BFS order:** Chapel → Dorm → Gym → Lab → Canteen → Library → Admin → Gate

## DFS from Chapel

Initial stack: [Chapel]

| Step | Selected vertex | Stack after step | Visited set | Traversal order so far |
| ---: | --- | --- | --- | --- |
| 1 | Chapel | [Dorm] | {Chapel} | Chapel |
| 2 | Dorm | [Lab, Gym] | {Chapel, Dorm} | Chapel → Dorm |
| 3 | Gym | [Lab, Lab, Canteen] | {Chapel, Dorm, Gym} | Chapel → Dorm → Gym |
| 4 | Canteen | [Lab, Lab, Library, Admin] | {Canteen, Chapel, Dorm, Gym} | Chapel → Dorm → Gym → Canteen |
| 5 | Admin | [Lab, Lab, Library, Library, Gate] | {Admin, Canteen, Chapel, Dorm, Gym} | Chapel → Dorm → Gym → Canteen → Admin |
| 6 | Gate | [Lab, Lab, Library, Library, Library] | {Admin, Canteen, Chapel, Dorm, Gate, Gym} | Chapel → Dorm → Gym → Canteen → Admin → Gate |
| 7 | Library | [Lab, Lab, Library, Library, Lab] | {Admin, Canteen, Chapel, Dorm, Gate, Gym, Library} | Chapel → Dorm → Gym → Canteen → Admin → Gate → Library |
| 8 | Lab | [Lab, Lab, Library, Library] | {Admin, Canteen, Chapel, Dorm, Gate, Gym, Lab, Library} | Chapel → Dorm → Gym → Canteen → Admin → Gate → Library → Lab |

**DFS order:** Chapel → Dorm → Gym → Canteen → Admin → Gate → Library → Lab

Annex is never reached from either start vertex (it has no edges).
