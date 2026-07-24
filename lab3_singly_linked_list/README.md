# Laboratory Activity Report  
## Linked List Implementation: Doubly Linked List & Circular Singly Linked List

---

# 1. Laboratory Information

| Field | Details |
|---|---|
| Laboratory Title | Dynamic Array Builder & Capacity Allocation |
| Course Code | CPEPRO8L |
| Course Title | Data Structures and Algorithms Laboratory |
| Student Name | Erguiza, Nino Eliezer |
| Date Completed | 7/26/2026 |
| Term | First Semester, AY 2026–2027 |

---

# 2. Objectives

This laboratory activity aims to:

1. Implement a **Doubly Linked List** using nodes with `next` and `prev` pointers.
2. Implement a **Circular Singly Linked List** where the last node points back to the first node.
3. Understand how different linked list structures manage node connections.
4. Apply correct pointer manipulation during insertion and traversal operations.
5. Verify that the completed implementations execute successfully without errors.

---

# 3. Source Code

| File | Description |
|---|---|
| `linked_list.py` | Contains the implementation of the Doubly Linked List and Circular Singly Linked List classes, including node creation, insertion methods, and traversal functions. |

### Key Design Details:

**Doubly Linked List:**

- Each node contains two references:
  - `next` pointer for forward traversal.
  - `prev` pointer for backward traversal.
- The head node maintains the beginning of the list.
- Insertions update both forward and backward connections to preserve the structure.

Example structure:

```
None <-> Node <-> Node <-> None
```

---

**Circular Singly Linked List:**

- Each node contains only a `next` pointer.
- The last node does not point to `None`.
- Instead, the final node points back to the head node, creating a circular connection.

Example structure:

```
Node → Node → Node → (back to head)
```

---

# 4. Execution Results

## 4.1 Console Output

### Command:

```bash
python linked_list.py
```

### Output:

```text
--- Testing Doubly Linked List ---
None <-> 10 <-> 5 <-> None

--- Testing Circular Linked List ---
100 -> 200 -> 300 -> (loops to 100)
```

Program executed successfully with no syntax errors or runtime errors.

---

## 4.2 Execution Analysis

### Doubly Linked List Output

The program inserted values:

```
5 and 10
```

at the beginning of the list.

Output:

```
None <-> 10 <-> 5 <-> None
```

This confirms that:

- The new nodes were inserted correctly at the head.
- The `next` pointer maintains forward connections.
- The `prev` pointer maintains backward connections.
- The list structure remains valid from both directions.

---

### Circular Singly Linked List Output

The program inserted values:

```
100, 200, and 300
```

into the circular list.

Output:

```
100 -> 200 -> 300 -> (loops to 100)
```

This confirms that:

- Nodes were successfully added.
- The final node correctly points back to the first node.
- The circular structure was properly maintained.
- Traversal stops after returning to the starting node.

---

## 4.3 Screenshots


![alt text](<Screenshot 2026-07-24 130256.png>)

---

# 5. Report Analysis Questions

## Q1: Complete the classes and verify they execute without compile or runtime errors.

The Doubly Linked List and Circular Singly Linked List classes were successfully completed by implementing the required node structures, insertion methods, and traversal operations.

The program was executed successfully without compile-time or runtime errors.

The output verified that:

- The Doubly Linked List correctly handled node insertion and maintained both `next` and `prev` references.
- The Circular Singly Linked List correctly connected the tail node back to the head node.
- Both linked list implementations produced the expected output.

---

## Q2: Explain the termination condition in a loop traversal of a Circular Linked List to prevent infinite loops.

A Circular Linked List does not have a `None` value at the end because the final node points back to the first node.

Because of this, using a normal traversal condition:

```python
while temp:
```

would create an infinite loop since `temp` will never become `None`.

Instead, traversal must stop when the current node reaches the starting node again.

Example:

```python
temp = self.head

while True:
    print(temp.data)
    temp = temp.next

    if temp == self.head:
        break
```

The condition:

```python
temp == self.head
```

serves as the stopping condition. Once traversal returns to the original starting node, the loop terminates.

This ensures that:

- Every node is visited exactly once.
- The circular connection is preserved.
- Infinite traversal is avoided.

---

# 6. Complexity Analysis

| Operation | Time Complexity |
|---|---|
| Insert at Head (Doubly Linked List) | O(1) |
| Display Forward (Doubly Linked List) | O(n) |
| Insert at Tail (Circular Linked List) | O(n) |
| Display Circular List | O(n) |

---

# 7. Conclusion

This laboratory activity successfully demonstrated the implementation and behavior of Doubly Linked Lists and Circular Singly Linked Lists.

The completed programs showed how different linked list structures manage node connections using pointers. The Doubly Linked List demonstrated bidirectional traversal through `next` and `prev` references, while the Circular Singly Linked List demonstrated how a node can connect back to the beginning of the structure.

### Concepts Learned:

- How nodes are connected using pointers.
- Differences between doubly linked and circular linked structures.
- Proper pointer updating during insertion operations.
- The importance of correct traversal termination conditions.

### Skills Developed:

- Implementing linked list data structures from scratch.
- Managing node references manually.
- Debugging pointer-related logic errors.
- Analyzing time complexity of linked list operations.

Understanding linked list structures is important because they provide flexible memory usage and efficient insertion operations compared to contiguous structures such as arrays. These concepts serve as a foundation for more advanced data structures and algorithms.