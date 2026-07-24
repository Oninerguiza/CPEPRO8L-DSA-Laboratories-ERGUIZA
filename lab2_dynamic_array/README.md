# Laboratory Activity No. 2  
## Dynamic Array Builder & Capacity Allocation

---

## 1. Laboratory Information

| Field | Details |
|---|---|
| Laboratory Title | Dynamic Array Builder & Capacity Allocation |
| Course Code | CPEPRO8L |
| Course Title | Data Structures and Algorithms Laboratory |
| Student Name | Otiong, Cristan Jay N. |
| Date Completed | 7/16/2026 |
| Term | First Semester, AY 2026–2027 |

---

# 2. Objectives

- Implement a custom dynamic array class from scratch using Python's `ctypes` module.
- Understand capacity scaling, memory doubling, and the cost of element copying.
- Observe how index access works in **O(1)** constant time complexity.

---

# 3. Source Code

| File | Description |
|---|---|
| `lab2_dynamic_array.py` | Custom `DynamicArray` class implementing `__getitem__`, `append`, `_resize`, and `_make_array`, including a driver program that appends 10 elements while displaying capacity growth. |

### Key Design Details:

**Backing Store:**  
The dynamic array uses a raw `ctypes.py_object` array instead of Python's built-in list. This exposes the manual memory allocation process normally hidden by high-level containers.

**Growth Strategy:**  
The capacity follows a doubling strategy:

```
1 → 2 → 4 → 8 → 16
```

When `size == capacity`, the `_resize()` function is called and creates a new array with double the previous capacity.

**Bounds Checking:**  
The `__getitem__()` method validates indexes using `self.size`, ensuring that only initialized elements can be accessed. The unused capacity slots remain inaccessible.

**Memory Handling:**  
During resizing, all existing elements are copied from the old memory block into the new larger contiguous memory block.

---

# 4. Execution Results

## 4.1 Console Output

### Command:

```bash
python lab2_dynamic_array.py
```

### Output:

```
Appending 0 | Size: 1 | Capacity: 1 | Element at index 0: 0
[RESIZE] capacity 1 -> 2
Appending 1 | Size: 2 | Capacity: 2 | Element at index 1: 1
[RESIZE] capacity 2 -> 4
Appending 2 | Size: 3 | Capacity: 4 | Element at index 2: 2
Appending 3 | Size: 4 | Capacity: 4 | Element at index 3: 3
[RESIZE] capacity 4 -> 8
Appending 4 | Size: 5 | Capacity: 8 | Element at index 4: 4
Appending 5 | Size: 6 | Capacity: 8 | Element at index 5: 5
Appending 6 | Size: 7 | Capacity: 8 | Element at index 6: 6
Appending 7 | Size: 8 | Capacity: 8 | Element at index 7: 7
[RESIZE] capacity 8 -> 16
Appending 8 | Size: 9 | Capacity: 16 | Element at index 8: 8
Appending 9 | Size: 10 | Capacity: 16 | Element at index 9: 9
```

Program executed successfully with no syntax errors or runtime errors.

---

## 4.2 Capacity Resize Trace Table

| Append # (i) | Size Before Append | Capacity Before Append | Resize Triggered? | New Capacity |
|---|---:|---:|---|---:|
| 0 | 0 | 1 | No | 1 |
| 1 | 1 | 1 | Yes | 2 |
| 2 | 2 | 2 | Yes | 4 |
| 3 | 3 | 4 | No | 4 |
| 4 | 4 | 4 | Yes | 8 |
| 5 | 5 | 8 | No | 8 |
| 6 | 6 | 8 | No | 8 |
| 7 | 7 | 8 | No | 8 |
| 8 | 8 | 8 | Yes | 16 |
| 9 | 9 | 16 | No | 16 |

The capacity resizes occurred exactly at logical sizes:

```
1, 2, 4, and 8
```

This confirms the capacity-doubling strategy where resizing occurs only when the allocated memory becomes completely full.

---

## 4.3 Screenshots

(Add screenshot of the terminal output here)

Example:

```
![Console Output Screenshot](screenshots/output.png)
```

---

# 5. Analysis

## Q1: Run the script and record the exact sizes where capacity resizes occur.

The dynamic array resized when the current number of stored elements reached the available capacity.

The resize points were:

```
Size = 1
Size = 2
Size = 4
Size = 8
```

This happened because the initial capacity was set to `1`. Whenever an append operation was performed while:

```
size == capacity
```

the `_resize()` method doubled the capacity before inserting the new element.

The growth sequence was:

```
1 → 2 → 4 → 8 → 16
```

Because the capacity increases exponentially, resizing becomes less frequent as the number of stored elements grows. For 10 append operations, the array only needed four resize operations instead of reallocating memory on every insertion.

---

## Q2: Explain why the dynamic array copies elements during resize. What is the time complexity of a single resize operation?

A dynamic array stores elements inside a contiguous block of memory. Since this memory block has a fixed size, it cannot simply expand when additional elements are required.

When the capacity is exceeded, the program must:

1. Allocate a new larger memory block.
2. Copy every existing element from the old array.
3. Replace the old memory reference with the new array.

The copying process is necessary because the elements must remain available after moving to the new memory location.

For example:

Before resizing:

```
[0][1][2][3]
```

After resizing:

```
[0][1][2][3][ ][ ][ ][ ]
```

The original elements must be transferred into the new larger storage area.

The time complexity of a single resize operation is:

```
O(n)
```

where `n` represents the number of existing elements that must be copied.

Although resizing requires linear time, it does not happen during every append operation. Since capacity doubles after every resize, the total cost of multiple resizing operations is distributed across many insertions. This gives the append operation an amortized complexity of:

```
O(1)
```

on average.

---

# 6. Conclusion

This laboratory activity demonstrated how dynamic arrays operate internally and how memory management affects performance. By implementing a custom `DynamicArray` using Python's `ctypes` module, the process of capacity allocation, memory copying, and resizing became observable.

### Concepts Learned:

- Difference between logical size and physical capacity.
- How dynamic arrays use contiguous memory allocation.
- Why resizing requires creating a new memory block and copying elements.
- How capacity doubling improves performance through amortized analysis.
- Why direct index access has constant-time complexity:

```
Access by index: O(1)
```

### Skills Developed:

- Implementing a dynamic array structure from scratch.
- Using Python's `ctypes` module for low-level memory allocation.
- Creating custom container behavior using Python dunder methods.
- Understanding performance trade-offs in data structure design.

### Importance of the Topic:

Dynamic arrays are widely used in modern programming languages, including Python lists, C++ vectors, and Java ArrayLists. Understanding how they manage memory helps explain why some operations are efficient while others require additional processing.

Operations such as accessing an element by index are fast because of contiguous memory, while operations that require shifting or reallocating data may become more expensive.

This activity provides a foundation for analyzing and selecting appropriate data structures based on their performance characteristics.