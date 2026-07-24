# Laboratory Activity No. 4
## Doubly Linked List & Circular Linked List

**Course Code:** CPEPRO8L  
**Course Title:** Data Structures and Algorithms  
**Term:** First Semester, AY 2026–2027

---

# Student Information

- **Name:** *Your Name*
- **Date Submitted:** *Submission Date*

---

# Objectives

This laboratory activity aims to:

1. Implement a Doubly Linked List (DLL) using `next` and `prev` pointers.
2. Build a Circular Singly Linked List (CLL) where the last node links back to the head.
3. Understand the differences in traversal between linear and circular linked lists.
4. Verify that both linked list implementations execute correctly without runtime errors.




## Doubly Linked List

- Create a new node.
- Insert the node at the beginning of the list.
- Update both the `next` and `prev` pointers.
- Display the list from head to tail.

## Circular Singly Linked List

- Create a new node.
- Traverse to the last node.
- Link the last node to the new node.
- Link the new node back to the head.
- Display the list by stopping once the traversal returns to the head.

---

# Program Execution

The program was executed successfully without any compile-time or runtime errors.

## Console Output

```text
--- Testing Doubly Linked List ---
None <-> 10 <-> 5 <-> None

--- Testing Circular Linked List ---
100 -> 200 -> 300 -> (loops to 100)
```

## Screenshot

> Place your console screenshot inside the `screenshots` folder.

```text
screenshots/
└── console-output.png
```

Then display it in GitHub using:

```markdown
![Program Output](screenshots/console-output.png)
```

---

# Output Analysis

### Doubly Linked List

After inserting **5** and then **10** at the head, the list became:

```
None <-> 10 <-> 5 <-> None
```

This confirms that:

- `insert_head()` correctly places new nodes at the beginning.
- The `next` and `prev` pointers were updated correctly.
- The list begins and ends with `None`, confirming a linear doubly linked list.

---

### Circular Singly Linked List

After inserting **100**, **200**, and **300**, the output became:

```
100 -> 200 -> 300 -> (loops to 100)
```

This confirms that:

- New nodes were inserted at the tail.
- The final node correctly points back to the head node.
- The circular connection was successfully established.

---

# Time Complexity

| Operation | Time Complexity |
|-----------|-----------------|
| DLL `insert_head()` | **O(1)** |
| DLL `display_forward()` | **O(n)** |
| CLL `insert_tail()` | **O(n)** |
| CLL `display()` | **O(n)** |

---

# Report Analysis Questions

## 1. Complete the classes and verify they execute without compile or runtime errors.

The program executed successfully without any compile-time or runtime errors. Both the Doubly Linked List and Circular Singly Linked List behaved as expected.

The console output confirmed that:

- The Doubly Linked List inserted nodes correctly at the head.
- The Circular Singly Linked List inserted nodes correctly at the tail.
- The circular link from the last node back to the head was successfully created.

---

## 2. Explain the termination condition in a loop traversal of a Circular Linked List to prevent infinite loops.

Unlike a linear linked list, a Circular Linked List does not end with a `None` pointer because the last node points back to the head. Therefore, traversal cannot stop by checking for `None`.

Instead, traversal starts from the head and continues until the current node returns to the head again. This condition ensures that every node is visited exactly once and prevents the program from entering an infinite loop.

Example logic:

```python
temp = self.head

while True:
    print(temp.data)
    temp = temp.next

    if temp == self.head:
        break
```

This loop terminates immediately after returning to the starting node.

---

# Conclusion

This laboratory successfully demonstrated the implementation of both a Doubly Linked List and a Circular Singly Linked List. The program correctly updated node connections using `next` and `prev` pointers for the doubly linked list and maintained a circular connection in the circular linked list. The execution results verified that both implementations functioned correctly without errors. Additionally, the activity highlighted the importance of using the head node as the stopping condition when traversing a Circular Linked List to prevent infinite loops.

---

# Author

**Name:** *Your Name*  
**Course:** CPEPRO8L – Data Structures and Algorithms  
**Academic Year:** First Semester, AY 2026–2027