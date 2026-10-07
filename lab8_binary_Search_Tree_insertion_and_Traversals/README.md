# Laboratory Activity No. 8: Binary Search Tree Insertion and Traversals

*Course Code:* CPEPRO8L
*Course Title:* Data Structures and Algorithms
*Term:* First Semester, AY 2026-2027

## 1. Objectives

The objectives of this laboratory activity are to:

1. Implement dynamic tree nodes with left and right child references.
2. Build insertion and lookup functions in a Binary Search Tree (BST).
3. Implement Inorder, Preorder, and Postorder recursive tree traversals.
4. Understand how values are organized according to the BST property.
5. Demonstrate recursive searching and traversal of a binary tree.
6. Analyze the outputs produced by the different tree traversal methods.

## 2. Files

| File | Description |
|------|-------------|
| lab8_bst.py | Completed Python implementation of the Binary Search Tree, insertion, search, and recursive traversals. |
| README.md | Documentation containing the objectives, methodology, execution output, analysis, and conclusion. |

## 3. How to Run

The program can be executed from a terminal using:

python lab8_bst.py

If Python 3 is specifically required on the system, use:

python3 lab8_bst.py

## 4. Methodology

A Binary Search Tree is a hierarchical data structure composed of nodes. Each node contains a key and two references:

- A *left* reference pointing to the left child.
- A *right* reference pointing to the right child.

The BST follows an ordering rule. For each node:

- Values smaller than the node's key are placed in the left subtree.
- Values greater than the node's key are placed in the right subtree.

This property allows the tree to organize data efficiently and makes operations such as searching and traversal easier to implement.

The program uses a TreeNode class to represent individual nodes and a BST class to manage the tree.

### TreeNode

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

The key stores the value of the node, while left and right initially contain None because the node does not have children when it is first created.

### BST

The BST class maintains a reference to the root of the tree:

class BST:
    def __init__(self):
        self.root = None

When the tree is empty, root is None.

## 5. BST Insertion

The insertion operation places a new value in its appropriate position while maintaining the BST property.

1. The algorithm starts at the root.
2. If the new key is smaller than the current node's key, the algorithm moves to the left subtree.
3. If the new key is greater than or equal to the current node's key, the algorithm moves to the right subtree.
4. This process continues recursively until an empty child position is found.

For the test data:

50, 30, 70, 20, 40, 60, 80

the values are inserted one at a time.

- The first value, 50, becomes the root.
- The value 30 is smaller than 50, so it is placed on the left.
- The value 70 is greater than 50, so it is placed on the right.
- The remaining values are positioned by comparing them with the appropriate nodes.

The final tree becomes:

        50
       /  \
     30    70
    /  \  /  \
   20  40 60  80

## 6. Test Tree

Elements inserted in this order:

50, 30, 70, 20, 40, 60, 80

Resulting Binary Search Tree:

        50
       /  \
     30    70
    /  \  /  \
   20  40 60  80

- The root node is 50.
- Its left subtree contains: 20, 30, 40
- Its right subtree contains: 60, 70, 80

This structure satisfies the Binary Search Tree property at every node.

## 7. Tree Traversals

The program implements three standard recursive traversal techniques.

### Inorder Traversal

Inorder traversal follows:

Left → Node → Right

The algorithm first visits the left subtree, then the current node, and finally the right subtree.

For this tree, the output is:

20 30 40 50 60 70 80

This is particularly useful for BSTs because it produces the keys in sorted order.

### Preorder Traversal

Preorder traversal follows:

Node → Left → Right

The current node is processed first, followed by its left subtree and then its right subtree.

The output is:

50 30 20 40 70 60 80

Preorder traversal is useful when the root should be processed before its children.

### Postorder Traversal

Postorder traversal follows:

Left → Right → Node

The left and right subtrees are processed before the current node.

The output is:

20 40 30 60 80 70 50

Postorder traversal is commonly useful when child nodes need to be processed before their parent.

## 8. Search Operation

The program also demonstrates searching for values in the Binary Search Tree.

For example:

Search 60: True
Search 99: False

When searching for 60:

1. The algorithm starts at the root.
2. Since 60 is greater than 50, the search moves to the right subtree.
3. The next node is 70. Since 60 is smaller than 70, the search moves to the left subtree.
4. The next node is 60, which matches the target.

Therefore:

Search 60: True

When searching for 99, the algorithm follows the appropriate right-side paths but eventually reaches an empty position without finding 99.

Therefore:

Search 99: False

The search demonstrates how the BST property allows the algorithm to eliminate unnecessary portions of the tree.

## 9. Execution and Output

The program was executed using:

python lab8_bst.py

The expected output is:

Inorder Traversal:
20 30 40 50 60 70 80

Preorder Traversal:
50 30 20 40 70 60 80

Postorder Traversal:
20 40 30 60 80 70 50

Search 60: True
Search 99: False

### Output Summary

| Operation | Result |
|-----------|--------|
| Inorder Traversal | 20 30 40 50 60 70 80 |
| Preorder Traversal | 50 30 20 40 70 60 80 |
| Postorder Traversal | 20 40 30 60 80 70 50 |
| Search 60 | True |
| Search 99 | False |

## 10. Report Analysis Questions

### 10.1 Preorder and Postorder Outputs for the Test Tree

The three traversal methods and their outputs are summarized below:

| Traversal | Order | Output |
|-----------|-------|--------|
| Inorder | Left, Node, Right | 20 30 40 50 60 70 80 |
| Preorder | Node, Left, Right | 50 30 20 40 70 60 80 |
| Postorder | Left, Right, Node | 20 40 30 60 80 70 50 |

The required Preorder output is:

50 30 20 40 70 60 80

The required Postorder output is:

20 40 30 60 80 70 50

### 10.2 Why Does Inorder Traversal of a BST Give Sorted Order?

A BST follows one important rule at every node: values in the left subtree are smaller than the node, while values in the right subtree are larger than the node.

Inorder traversal visits nodes using the following order:

Left → Node → Right

Therefore, all smaller keys are printed before the current node, and all larger keys are printed after the current node.

For example, at the root 50, the entire left subtree is processed first:

20 30 40

Then the root is processed:

50

Finally, the right subtree is processed:

60 70 80

This produces:

20 30 40 50 60 70 80

The same rule is applied recursively to every subtree. As a result, the keys of a valid BST are produced from smallest to largest.

Therefore, inorder traversal of a Binary Search Tree produces the elements in sorted ascending order.

## 11. Recursive Traversal and Base Case

The traversal functions use recursion to process each subtree.

For example, an inorder traversal can be represented as:

inorder(50)
    ↓
inorder(30)
    ↓
inorder(20)

When the traversal reaches a node with no child, the recursive function encounters None and stops that branch.

A typical base condition is:

if node is not None:

If the node is None, the function returns without performing another recursive call. This prevents the traversal from continuing indefinitely.

## 12. Complexity Analysis

The time complexity of searching and inserting in a BST depends on the height of the tree.

For a balanced BST, the height is approximately O(log n). For a highly unbalanced tree, the height can become O(n).

| Operation | Average/Balanced Case | Worst Case |
|-----------|----------------------|------------|
| Search | O(log n) | O(n) |
| Insertion | O(log n) | O(n) |
| Inorder Traversal | O(n) | O(n) |
| Preorder Traversal | O(n) | O(n) |
| Postorder Traversal | O(n) | O(n) |

The traversal operations always visit every node, so their time complexity is O(n) regardless of whether the tree is balanced.

The recursive traversal functions also require call-stack space based on the tree height:

Auxiliary Space = O(h)

where h is the height of the tree.

- For a balanced tree: O(h) = O(log n)
- For a skewed tree: O(h) = O(n)

## 13. Advantages of a Binary Search Tree

Binary Search Trees provide several advantages:

- They maintain data in an organized hierarchical structure.
- Searching can be faster than a linear search when the tree is balanced.
- Insertion can be efficient because the algorithm only follows one path through the tree.
- Inorder traversal produces sorted data.
- Recursive implementations naturally match the structure of the tree.
- The tree can dynamically grow as new elements are inserted.

However, an ordinary BST can become unbalanced if elements are inserted in an unfavorable order. In the worst case, the tree can resemble a linked list, causing search and insertion operations to degrade to O(n).

## 14. Conclusion

This laboratory activity demonstrated the implementation of a Binary Search Tree using Python. The program successfully created dynamic tree nodes, inserted values according to the BST property, searched for values, and implemented Inorder, Preorder, and Postorder recursive traversals.

Using the test values:

50, 30, 70, 20, 40, 60, 80

the resulting tree was:

        50
       /  \
     30    70
    /  \  /  \
   20  40 60  80

The traversal results were:

Inorder:
20 30 40 50 60 70 80

Preorder:
50 30 20 40 70 60 80

Postorder:
20 40 30 60 80 70 50

The search operation also successfully identified whether values existed in the tree:

Search 60: True
Search 99: False

The activity demonstrated that inorder traversal produces sorted output because a BST stores smaller values in the left subtree and larger values in the right subtree. By visiting the tree using the Left → Node → Right order, the elements are naturally encountered from smallest to largest.

Overall, the laboratory provided practical experience with Binary Search Tree construction, recursive insertion, searching, and tree traversal techniques. It also demonstrated how the structure and height of a BST affect the efficiency of its operations.

## 15. Repository Structure

The GitHub repository should contain the following files:

lab8-bst/
├── lab8_bst.py
└── README.md

The lab8_bst.py file contains the completed source code, while README.md provides the documentation, execution results, analysis questions, and conclusion required for the laboratory submission.