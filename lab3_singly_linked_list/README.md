# Laboratory Activity No. 3
## Singly Linked List

**Course Code:** CPEPRO8L  
**Course Title:** Data Structures and Algorithms  
**Term:** First Semester, AY 2026–2027

---

# Student Information

- **Name:** *ERGUIZA, NINO ELIEZER*
- **Date Submitted:** *JULY 30, 2026*

---

# Objectives

This laboratory activity aims to:

1. Construct custom `Node` and `SinglyLinkedList` classes.
2. Implement insertion at the head and tail of the list.
3. Implement search and deletion operations.
4. Understand how pointers are updated while maintaining the linked list structure.

---

# Introduction

A **Singly Linked List (SLL)** is a dynamic data structure in which each node stores data and a reference (`next`) to the following node. Unlike arrays, linked list elements are not stored in contiguous memory locations. This allows efficient insertion and deletion of nodes without shifting other elements. However, traversal is required to access or modify nodes, making some operations linear in time complexity.


# Methodology

The program performs the following operations:

### 1. Insert at the Head
- Create a new node.
- Point the new node to the current head.
- Update the head pointer.

### 2. Insert at the Tail
- Create a new node.
- Traverse to the last node.
- Link the last node to the new node.

### 3. Delete a Node
- Search for the target value.
- Update the previous node's `next` pointer.
- Remove the target node.

### 4. Search
- Traverse the list.
- Return `True` if the value exists.
- Return `False` otherwise.

---

# Program Execution

The completed program executed successfully without compile-time or runtime errors.

## Console Output

```text
20 -> 10 -> 30 -> None
20 -> 30 -> None
Is 30 in list? True
```

## Screenshot

Save your console output inside the `screenshots` folder.

```text
screenshots/
└── console-output.png
```

Display it in GitHub using:

```markdown
![Program Output](screenshots/console-output.png)
```

---

# Output Analysis

### Initial List

The program inserts:

- 10 at the head
- 20 at the head
- 30 at the tail

Result:

```text
20 -> 10 -> 30 -> None
```

This confirms that:

- Head insertion correctly places the newest node at the beginning.
- Tail insertion correctly appends the new node to the end.

---

### After Deleting 10

The node containing **10** is removed.

Updated list:

```text
20 -> 30 -> None
```

This verifies that:

- The target node was successfully located.
- The previous node was correctly linked to the next node.
- No nodes were lost after deletion.

---

### Search Operation

Searching for **30** returns:

```text
Is 30 in list? True
```

This confirms that the search function successfully traversed the list and found the requested value.

---

# Pointer Trace During Deletion

Before deletion:

```text
Head
 ↓
20 ───► 10 ───► 30 ───► None
```

Pointers during deletion:

- `previous` points to **20**
- `current` points to **10** (target)

```text
previous.next = current.next
```

After updating the pointer:

```text
Head
 ↓
20 ─────────► 30 ───► None
```

The node containing **10** is no longer referenced and is removed from the list.

---

# Time Complexity

| Operation | Time Complexity |
|-----------|-----------------|
| Insert at Head | **O(1)** |
| Insert at Tail | **O(n)** |
| Delete by Value | **O(n)** |
| Search | **O(n)** |
| Display | **O(n)** |

---

# Report Analysis Questions

## 1. Run the completed script and include console outputs showing insertion, search, and deletion.

The completed program executed successfully without any compile-time or runtime errors.

Console Output:

```text
20 -> 10 -> 30 -> None
20 -> 30 -> None
Is 30 in list? True
```

The output confirms that:

- Nodes were inserted correctly at the head and tail.
- The node containing **10** was successfully deleted.
- The search function correctly found the value **30**.

---

## 2. Trace the pointers step-by-step when deleting the middle node.

Before deletion:

```text
Head
 ↓
20 ─► 10 ─► 30 ─► None
```

Step 1:
- `previous` points to **20**
- `current` points to **10**

```text
previous = 20
current = 10
```

Step 2:

Update the link:

```python
previous.next = current.next
```

Since `current.next` points to **30**, node **20** now points directly to **30**.

After deletion:

```text
Head
 ↓
20 ─► 30 ─► None
```

The node containing **10** is disconnected from the list and is automatically reclaimed by Python's garbage collector because no references remain.

---

# Conclusion

This laboratory successfully demonstrated the implementation of a Singly Linked List using custom `Node` and `SinglyLinkedList` classes. The insertion, deletion, search, and display operations were implemented correctly and executed without errors. The activity also illustrated how node pointers are updated during deletion to preserve the structure of the list. Understanding these pointer manipulations is essential for implementing efficient linked list operations and forms a foundation for more advanced data structures.

---

# Author

**Name:** *ERGUIZA, NINO ELIEZER*  
**Course:** CPEPRO8L – Data Structures and Algorithms  
**Academic Year:** First Semester, AY 2026–2027