# Laboratory Activity Report  
## Linked List Implementation: Singly Linked List CRUD Operations

---

# 1. Laboratory Information

| Field | Details |
|---|---|
| Laboratory Title | Singly Linked List CRUD Operations |
| Course Code | CPEPRO8L |
| Course Title | Data Structures and Algorithms Laboratory |
| Student Name | Erguiza, Nino Eliezer |
| Date Completed | 7/26/2026 |
| Term | First Semester, AY 2026–2027 |

---

# 2. Objectives

This laboratory activity aims to:

1. Implement a **Singly Linked List** using Python.
2. Understand how nodes store data and references to the next node.
3. Perform basic linked list operations including:
   - Insertion at the head.
   - Insertion at the tail.
   - Searching for a specific value.
   - Deleting a node by value.
   - Displaying all elements.
4. Apply proper pointer manipulation during insertion and deletion operations.
5. Trace pointer changes when deleting a middle node.
6. Verify that the completed program executes successfully without errors.

---

# 3. Source Code

| File | Description |
|---|---|
| `singly_linked_list.py` | Contains the implementation of the Singly Linked List, including node creation, insertion, deletion, searching, and display functions. |

## Key Design Details

### Singly Linked List

A Singly Linked List consists of nodes where each node contains:

- `data` - stores the value of the node.
- `next` - stores the reference to the next node.

The `head` pointer stores the first node in the list.

The final node points to `None`, indicating the end of the list.

Example structure:

```
Head
 |
 v
Node -> Node -> Node -> None
```

---

## Implemented Operations

| Method | Description |
|---|---|
| `insert_head()` | Inserts a new node at the beginning of the list. |
| `insert_tail()` | Inserts a new node at the end of the list. |
| `delete_value()` | Deletes a node containing the target value. |
| `search()` | Searches for a specific value in the list. |
| `display()` | Traverses and displays all nodes. |

---

# 4. Execution Results

## 4.1 Console Output

### Command:

```bash
python singly_linked_list.py
```

### Output:

```text
20 -> 10 -> 30 -> None
20 -> 30 -> None
Is 30 in list? True
```

The program executed successfully without syntax errors or runtime errors.

---

# 4.2 Execution Analysis

## Insertion Operation

The program executed the following commands:

```python
sll.insert_head(10)
sll.insert_head(20)
sll.insert_tail(30)
```

### Step 1: Insert 10 at Head

Initial state:

```
None
```

After creating the first node:

```
10 -> None
```

The head pointer now points to the node containing `10`.

---

### Step 2: Insert 20 at Head

A new node containing `20` is created.

Before updating head:

```
20 -> None

10 -> None
```

The new node points to the current head:

```
20 -> 10 -> None
```

The head is updated:

```
Head
 |
 v
20 -> 10 -> None
```

---

### Step 3: Insert 30 at Tail

The program traverses until the last node.

Current list:

```
20 -> 10 -> None
```

The last node (`10`) points to the new node:

```
20 -> 10 -> 30 -> None
```

Final insertion output:

```
20 -> 10 -> 30 -> None
```

This confirms that:

- Head insertion correctly places nodes at the beginning.
- Tail insertion correctly attaches a node at the end.
- Node connections are maintained using the `next` pointer.

---

# Search Operation

The program searches for:

```
30
```

Initial list:

```
20 -> 10 -> 30 -> None
```

Traversal process:

```
Check 20
20 != 30

Check 10
10 != 30

Check 30
30 == 30
```

Output:

```
Is 30 in list? True
```

The search operation successfully traversed the list and located the target value.

---

# Deletion Operation

The program deletes:

```
10
```

Before deletion:

```
Head
 |
 v
20 -> 10 -> 30 -> None
```

After deletion:

```
20 -> 30 -> None
```

The node containing `10` was removed successfully.

---

# 4.3 Screenshots

![Console Output Screenshot](Screenshot.png)

---

# 5. Report Analysis Questions

## Q1: Run the completed script and include console outputs showing insertion, search, and deletion.

The completed Singly Linked List program was executed successfully.

The program demonstrated the following operations:

### Insertion

Inserted values:

```
10, 20, and 30
```

Console output:

```
20 -> 10 -> 30 -> None
```

This verifies that:

- The first node was created successfully.
- The head insertion operation worked correctly.
- The tail insertion operation correctly connected the last node.

---

### Search

The program searched for:

```
30
```

Console output:

```
Is 30 in list? True
```

The search method successfully traversed each node and returned `True` when the target value was found.

---

### Deletion

The program deleted:

```
10
```

Before deletion:

```
20 -> 10 -> 30 -> None
```

After deletion:

```
20 -> 30 -> None
```

The result confirms that the target node was removed and the remaining nodes were correctly connected.

---

# Q2: Trace the pointers step-by-step when deleting the middle node.

Target node:

```
10
```

Initial linked list:

```
Head
 |
 v
20 -> 10 -> 30 -> None
```

The deletion function initializes:

```python
previous = self.head
current = self.head.next
```

Pointer assignment:

```
previous
   |
   v
  20
   |
   v
 current
   |
   v
  10
   |
   v
  30 -> None
```

The program checks:

```python
current.data == target
```

Comparison:

```
10 == 10
```

The target node is found.

Before changing the pointer:

```
20 -> 10 -> 30 -> None
      ^
      |
   Delete this node
```

The pointer update executes:

```python
previous.next = current.next
```

Before:

```
20.next = 10
```

After:

```
20.next = 30
```

Updated structure:

```
20 -> 30 -> None
```

The node containing `10` is removed because no node points to it anymore.

---

# 6. Complexity Analysis

| Operation | Time Complexity |
|---|---|
| Insert at Head | O(1) |
| Insert at Tail | O(n) |
| Search | O(n) |
| Delete by Value | O(n) |
| Display | O(n) |

---

# 7. Conclusion

This laboratory activity successfully demonstrated the implementation of a Singly Linked List using Python.

The program showed how nodes are connected through references and how pointer manipulation is used to perform insertion, searching, and deletion operations.

## Concepts Learned:

- Creating nodes and linking them together.
- Managing the head pointer.
- Performing CRUD operations in a linked list.
- Updating pointers during deletion.
- Traversing nodes sequentially.
- Understanding the time complexity of linked list operations.

## Skills Developed:

- Implementing data structures using Python.
- Managing node references manually.
- Debugging linked list operations.
- Analyzing pointer behavior.
- Understanding dynamic data structures.

A Singly Linked List provides flexible memory usage and efficient insertion and deletion compared to fixed-size structures. Understanding this structure provides a foundation for advanced data structures such as stacks, queues, trees, and graphs.
