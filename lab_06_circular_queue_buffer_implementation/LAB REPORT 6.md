# Laboratory Activity No. 6 — Circular Queue Buffer Implementation

**Course Code:** CPEPRO8L
**Course Title:** Data Structures and Algorithms
**Term:** First Semester, AY 2026–2027

---

## 1. Objectives

1. Implement a fixed-capacity Circular Queue from scratch.
2. Understand index wrapping mathematical calculations (`(tail + 1) % capacity`).
3. Solve buffer overflow and underflow conditions.

---

## 2. Files

| File                     | Description                                                                                                                       |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `lab6_circular_queue.py` | Completed implementation of the `CircularQueue` class, including `enqueue`, `dequeue`, `display`, and the required demonstration. |
| `README.md`              | Documentation containing the objectives, methodology, execution output, queue trace, analysis, and conclusion.                    |

---

## 3. Methodology

The `CircularQueue` is implemented using a fixed-size Python list. It uses three important variables:

* **`head`** — stores the index of the first element in the queue.
* **`tail`** — stores the index where the next element will be inserted.
* **`size`** — stores the current number of elements in the queue.

The queue follows the **First-In, First-Out (FIFO)** principle, meaning the first element inserted is the first element removed.

### `enqueue(item)`

The `enqueue()` method first checks whether the queue is full. If `size == capacity`, an overflow warning is displayed and the method returns `False`.

Otherwise, the item is inserted at the current `tail` position. The `size` is increased by one, and the `tail` is moved to the next position using:

```python
self.tail = (self.tail + 1) % self.capacity
```

### `dequeue()`

The `dequeue()` method first checks whether the queue is empty. If `size == 0`, an underflow warning is displayed and the method returns `None`.

Otherwise, the element at the current `head` position is retrieved. The position is then cleared by setting it to `None`, the `size` is decreased, and the `head` is advanced using:

```python
self.head = (self.head + 1) % self.capacity
```

### `display()`

The `display()` method prints the underlying queue array together with the current `head` and `tail` positions. This makes it easier to observe how the circular queue wraps around the fixed-size array.

The use of modulo allows the `head` and `tail` indices to return to index `0` after reaching the final position of the array. Therefore, previously freed positions can be reused without shifting existing elements.

---

## 4. Execution & Output

The program was executed using:

```text
python3 lab6_circular_queue.py
```

The required sample operations produced:

```text
Dequeued: 1
Queue array: [None, 2, 3, 4, None] | Head: 1 | Tail: 4
```

A separate 10-operation demonstration was also performed using a queue with a capacity of five:

```text
--- 10-operation enqueue/dequeue trace (capacity = 5) ---

Step 1: enqueue(10)
Queue array: [10, None, None, None, None] | Head: 0 | Tail: 1

Step 2: enqueue(20)
Queue array: [10, 20, None, None, None] | Head: 0 | Tail: 2

Step 3: enqueue(30)
Queue array: [10, 20, 30, None, None] | Head: 0 | Tail: 3

Step 4: dequeue() -> 10
Queue array: [None, 20, 30, None, None] | Head: 1 | Tail: 3

Step 5: enqueue(40)
Queue array: [None, 20, 30, 40, None] | Head: 1 | Tail: 4

Step 6: enqueue(50)
Queue array: [None, 20, 30, 40, 50] | Head: 1 | Tail: 0

Step 7: enqueue(60)
Queue array: [60, 20, 30, 40, 50] | Head: 1 | Tail: 1

Step 8: enqueue(70)
Queue overflow: Cannot enqueue.
Queue array: [60, 20, 30, 40, 50] | Head: 1 | Tail: 1

Step 9: dequeue() -> 20
Queue array: [60, None, 30, 40, 50] | Head: 2 | Tail: 1

Step 10: dequeue() -> 30
Queue array: [60, None, None, 40, 50] | Head: 3 | Tail: 1
```

---

## 5. Report Analysis Questions

### 5.1 Queue States During a Series of 10 Enqueues and Dequeues

A `CircularQueue(5)` was tested using the following sequence:

```text
enqueue(10)
enqueue(20)
enqueue(30)
dequeue()
enqueue(40)
enqueue(50)
enqueue(60)
enqueue(70)
dequeue()
dequeue()
```

The queue states after each operation are shown below.

| Step | Operation     | Result               | Queue Array                      | Head | Tail | Size |
| ---- | ------------- | -------------------- | -------------------------------- | ---: | ---: | ---: |
| 0    | Initial       | —                    | `[None, None, None, None, None]` |    0 |    0 |    0 |
| 1    | `enqueue(10)` | Inserted             | `[10, None, None, None, None]`   |    0 |    1 |    1 |
| 2    | `enqueue(20)` | Inserted             | `[10, 20, None, None, None]`     |    0 |    2 |    2 |
| 3    | `enqueue(30)` | Inserted             | `[10, 20, 30, None, None]`       |    0 |    3 |    3 |
| 4    | `dequeue()`   | Returns `10`         | `[None, 20, 30, None, None]`     |    1 |    3 |    2 |
| 5    | `enqueue(40)` | Inserted             | `[None, 20, 30, 40, None]`       |    1 |    4 |    3 |
| 6    | `enqueue(50)` | Inserted; tail wraps | `[None, 20, 30, 40, 50]`         |    1 |    0 |    4 |
| 7    | `enqueue(60)` | Inserted; queue full | `[60, 20, 30, 40, 50]`           |    1 |    1 |    5 |
| 8    | `enqueue(70)` | Rejected — overflow  | `[60, 20, 30, 40, 50]`           |    1 |    1 |    5 |
| 9    | `dequeue()`   | Returns `20`         | `[60, None, 30, 40, 50]`         |    2 |    1 |    4 |
| 10   | `dequeue()`   | Returns `30`         | `[60, None, None, 40, 50]`       |    3 |    1 |    3 |

### Key Observations

At **step 4**, the value `10` is removed from index `0`. This makes index `0` available for future use.

At **step 6**, `50` is inserted at index `4`. Since the queue has a capacity of five, the tail then wraps from index `4` back to index `0`.

At **step 7**, `60` is inserted at index `0`, demonstrating the main advantage of a Circular Queue: a previously freed position can be reused.

After step 7, the queue contains five elements, so `size == capacity`. The queue is therefore full, even though `head` and `tail` have the same value (`1`).

At **step 8**, an attempt is made to insert `70`. Because the queue is full, the operation is rejected and an overflow warning is printed. The queue remains unchanged.

At **steps 9 and 10**, the values `20` and `30` are removed according to the FIFO principle. Their positions are cleared and the `head` moves forward.

---

### 5.2 Purpose of the `%` Modulo Operator in Index Calculations

The `%` operator is used to make the `head` and `tail` indices wrap around the fixed-size array.

The queue uses the following calculations:

```python
self.tail = (self.tail + 1) % self.capacity
self.head = (self.head + 1) % self.capacity
```

For a queue with a capacity of `5`, the valid array indices are:

```text
0, 1, 2, 3, 4
```

When an index reaches the end of the array, modulo causes it to return to `0`.

For example:

```text
(4 + 1) % 5
= 5 % 5
= 0
```

Therefore, when `tail` is at index `4` and an item is successfully inserted, the next tail position becomes index `0`.

This behavior can be represented as:

```text
0 → 1 → 2 → 3 → 4 → 0 → 1 → ...
```

Without the modulo operator, the tail would continue increasing:

```text
0 → 1 → 2 → 3 → 4 → 5 → 6 → ...
```

An index of `5` would be outside the valid range of a five-element array and would cause an `IndexError`.

The modulo operator therefore allows the queue to reuse positions that have been freed by previous dequeue operations. It is the key operation that gives the data structure its **circular** behavior.

---

## 6. Overflow and Underflow Handling

### Overflow

Overflow occurs when an item is added while the queue is already full.

The implementation checks:

```python
if self.is_full():
    print("Queue overflow: Cannot enqueue.")
    return False
```

The `is_full()` method returns `True` when:

```python
self.size == self.capacity
```

When this condition is met, the item is not inserted and the existing queue contents remain unchanged.

### Underflow

Underflow occurs when a dequeue operation is attempted while the queue is empty.

The implementation checks:

```python
if self.is_empty():
    print("Queue underflow: Cannot dequeue.")
    return None
```

The `is_empty()` method returns `True` when:

```python
self.size == 0
```

This prevents the program from attempting to remove an element from an empty queue.

---

## 7. Complexity Analysis

Both `enqueue()` and `dequeue()` operate in constant time.

| Operation    | Time Complexity                            |
| ------------ | ------------------------------------------ |
| `enqueue()`  | O(1)                                       |
| `dequeue()`  | O(1)                                       |
| `is_full()`  | O(1)                                       |
| `is_empty()` | O(1)                                       |
| `display()`  | O(1) for the fixed-capacity implementation |

The Circular Queue does not shift elements when an item is removed. Instead, it advances the `head` index and reuses available positions through circular indexing.

The space complexity is **O(n)**, where `n` is the queue capacity, because the implementation stores elements in a fixed-size array.

---

## 8. Conclusion

The Circular Queue implementation successfully demonstrates the FIFO principle using a fixed-capacity array. The `head`, `tail`, and `size` variables work together to keep track of the queue's current state.

The modulo operator is essential because it allows the `head` and `tail` indices to wrap around to the beginning of the array. This makes it possible to reuse positions that were freed by dequeue operations without shifting the remaining elements.

The 10-operation test confirmed that the queue correctly handles insertion, removal, circular wrapping, overflow, and FIFO ordering. The implementation also achieves O(1) enqueue and dequeue operations, making the Circular Queue an efficient data structure for fixed-size buffers.
