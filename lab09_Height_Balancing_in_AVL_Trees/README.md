# Laboratory Activity No. 9: AVL Tree Insertion and Rotations

*Course Title:* Data Structures and Algorithms
*Language:* Python 3

## 1. Introduction

In the worst case (inserting sorted data), a normal BST turns into a linked list and search becomes O(n). An AVL Tree fixes this by balancing itself. It keeps the height difference between the left and right subtree (the *balance factor*) at most 1 for every node. When an insertion breaks this rule, the tree fixes itself using left and right rotations.

## 2. Objectives

1. Calculate height metrics and balance factors dynamically.
2. Implement Single and Double Rotations (LL, RR, LR, RL cases).
3. Demonstrate self-balancing tree insertions.

## 3. Files

| File | Description |
|------|-------------|
| lab9_avl.py | Completed AVL tree with insertion, rotations, and test runs. |
| README.md | Documentation, output, and analysis. |

## 4. How to Run

python lab9_avl.py

## 5. How the Code Works

### AVLNode
Each node stores a key, left, right, and a height. A new node starts with height 1.

### Height and Balance Factor

balance = height(left) - height(right)

| Balance | Meaning |
|---------|---------|
| -1, 0, 1 | Balanced |
| greater than 1 | Left heavy |
| less than -1 | Right heavy |

### Rotations

- rotate_right(y): the left child x of y becomes the new root. y becomes the right child of x, and the old right child of x (called T2) becomes the left child of y.
- rotate_left(x): the mirror of the above. The right child y becomes the new root.

Both functions update the heights of the two moved nodes (the lower one first) and return the new root of the subtree.

### Insertion

1. Do a normal BST insert (duplicates are ignored).
2. Update the height of the current node.
3. Compute the balance factor.
4. If it is outside [-1, 1], pick one of the four cases:

| Case | Condition | Fix |
|------|-----------|-----|
| LL | balance > 1 and key < left.key | Right rotation |
| RR | balance < -1 and key > right.key | Left rotation |
| LR | balance > 1 and key > left.key | Left rotation on left child, then right rotation |
| RL | balance < -1 and key < right.key | Right rotation on right child, then left rotation |

## 6. Execution and Output

Test 1: Insert 10, 20, 30
After inserting 10, preorder: 10 
After inserting 20, preorder: 10 20 
After inserting 30, preorder: 20 10 30 
Root: 20 | Balance: 0

Test 2: Insert 10, 20, 30, 40, 50, 25
Preorder:  30 20 10 25 40 50 
Inorder:   10 20 25 30 40 50 
Root: 30 | Height: 3 | Balance: 0

The inorder output is still sorted, so the BST property is kept after all the rotations.

### Test 2 Trace

| Insert | What happens | Case |
|--------|--------------|------|
| 10, 20 | No problem | None |
| 30 | Node 10 has balance -2 | RR, left rotate at 10 |
| 40 | No problem | None |
| 50 | Node 30 has balance -2 | RR, left rotate at 30 |
| 25 | Node 20 has balance -2, and 25 < 40 | RL, right rotate at 40, then left rotate at 20 |

## 7. Report Analysis Questions

### 7.1 AVL insertion and rotation routines with a right rotation sequence diagram

The routines are implemented in lab9_avl.py (rotate_right, rotate_left, and insert).

*Right rotation (LL case).* Example: inserting 30, 20, 10.

Before (node 30 has balance +2):

      y(30)
      /
    x(20)
    /
  10

After rotate_right(30):

      x(20)
      /   \
    10    y(30)

Sequence diagram of what rotate_right(y) does step by step:

mermaid
sequenceDiagram
    participant Y as y (30)
    participant X as x (20)
    participant T2 as T2 (x.right)
    Note over Y,X: y is unbalanced and x is y.left
    Y->>X: 1. x = y.left
    X->>T2: 2. t2 = x.right
    X->>Y: 3. x.right = y (y goes down to the right)
    Y->>T2: 4. y.left = t2 (T2 is moved to y)
    Note over Y: 5. update height of y
    Note over X: 6. update height of x
    X-->>Y: 7. return x as the new subtree root

### 7.2 Insert 10, 20, 30 and trace the automatic left rotation

*Step 1: insert 10.* The tree is empty, so 10 becomes the root.

10

*Step 2: insert 20.* 20 > 10, so it goes to the right. Heights: node 20 = 1, node 10 = 2. Balance of 10 = 0 - 1 = -1, which is still fine.

10
  \
   20

*Step 3: insert 30.* 30 > 10, then 30 > 20, so it goes to the right of 20.

10
  \
   20
     \
      30

Heights: node 30 = 1, node 20 = 2, node 10 = 3.
Balance of node 10 = 0 - 2 = *-2*, so the tree is unbalanced.

The key 30 is greater than root.right.key (20), so this is the *RR case*. The fix is rotate_left(10):

1. y = x.right which is 20
2. t2 = y.left which is None
3. y.left = x so 10 becomes the left child of 20
4. x.right = t2 so 10's right child becomes None
5. Update heights: node 10 = 1, node 20 = 2
6. Return 20 as the new root

*Result:*

    20
   /  \
  10   30

The balance of 20 is 0, and the inorder is still 10 20 30.

## 8. Complexity

| Operation | Time |
|-----------|------|
| Search | O(log n) |
| Insert | O(log n) |
| Rotation | O(1) |

An AVL tree always keeps its height at O(log n), so even the worst case is O(log n), unlike a normal BST which can reach O(n).

## 9. Conclusion

In this activity I implemented an AVL tree in Python. I learned how the balance factor tells us when a subtree is too heavy on one side, and how the four cases (LL, RR, LR, RL) each need a different rotation. Inserting 10, 20, 30 would make a plain BST a straight line, but the AVL tree rotated it into a balanced tree with 20 as the root. The inorder output stayed sorted after every rotation, which shows that rotations fix the shape without breaking the BST rule.

## 10. Repository Structure

lab9-avl/
├── lab9_avl.py
└── README.md