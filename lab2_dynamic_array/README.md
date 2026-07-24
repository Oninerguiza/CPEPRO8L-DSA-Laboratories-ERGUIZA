# Laboratory Activity Report  
## Dynamic Array Implementation Using Python

---

# 1. Laboratory Information

| Field | Details |
|---|---|
| Laboratory Title | Dynamic Array Implementation |
| Course Code | CPEPRO8L |
| Course Title | Data Structures and Algorithms Laboratory |
| Student Name | Erguiza, Nino Eliezer |
| Date Completed | 7/26/2026 |
| Term | First Semester, AY 2026–2027 |

---

# 2. Objectives

This laboratory activity aims to:

1. Implement a **Dynamic Array** data structure using Python.
2. Understand how dynamic arrays manage memory allocation and resizing.
3. Apply array operations such as:
   - Appending elements.
   - Accessing elements through indexes.
   - Tracking current size and capacity.
4. Analyze how capacity changes when the array becomes full.
5. Observe the resizing process and element copying during expansion.
6. Verify that the completed implementation executes successfully without errors.

---

# 3. Source Code

| File | Description |
|---|---|
| `dynamic_array.py` | Contains the implementation of a Dynamic Array using Python's `ctypes` module, including initialization, append operation, resizing, and element access. |

---

# Key Design Details

## Dynamic Array Structure

A Dynamic Array is an array structure that automatically increases its capacity when the current storage becomes full.

The implementation maintains:

| Attribute | Description |
|---|---|
| `size` | Number of elements currently stored in the array |
| `capacity` | Maximum number of elements that can be stored before resizing |
| `array` | Internal memory storage |

Initial condition:

```
Size = 0
Capacity = 1
```

Example:

```
Capacity: 4

Index:
0   1   2   3
|   |   |   |
10 20 30 40
```

---

## Implemented Operations

| Method | Description |
|---|---|
| `append()` | Adds a new element to the end of the array. |
| `__len__()` | Returns the current number of elements. |
| `__getitem__()` | Allows access to elements using indexes. |
| `_resize()` | Creates a larger array and copies existing elements. |
| `_make_array()` | Creates a low-level array using `ctypes`. |

---

# 4. Execution Results

## 4.1 Console Output

### Command:

```bash
python dynamic_array.py
```

### Output:

```text
Appending 0 | Size: 1 | Capacity: 1 | Element at index 0: 0
Resizing from 1 to 2
Appending 1 | Size: 2 | Capacity: 2 | Element at index 1: 1
Resizing from 2 to 4
Appending 2 | Size: 3 | Capacity: 4 | Element at index 2: 2
Appending 3 | Size: 4 | Capacity: 4 | Element at index 3: 3
Resizing from 4 to 8
Appending 4 | Size: 5 | Capacity: 8 | Element at index 4: 4
Appending 5 | Size: 6 | Capacity: 8 | Element at index 5: 5
Appending 6 | Size: 7 | Capacity: 8 | Element at index 6: 6
Appending 7 | Size: 8 | Capacity: 8 | Element at index 7: 7
Resizing from 8 to 16
Appending 8 | Size: 9 | Capacity: 16 | Element at index 8: 8
Appending 9 | Size: 10 | Capacity: 16 | Element at index 9: 9
```

The program executed successfully without syntax errors or runtime errors.

---

# 4.2 Execution Analysis

## Append Operation

The program inserts values:

```
0 to 9
```

into the dynamic array.

Each insertion increases the current size by one.

Example:

Before append:

```
Size: 2
Capacity: 2
```

The array is full, so inserting another element requires resizing.

The capacity doubles:

```
Capacity: 2 → 4
```

The existing elements are copied into the new larger array.

---

# Capacity Resize Trace

The dynamic array uses a doubling strategy where:

```
New Capacity = Current Capacity × 2
```

The resizing events occurred at the following points:

| Append Operation | Size Before Resize | Old Capacity | New Capacity |
|---|---|---|---|
| Append 1 | 1 | 1 | 2 |
| Append 2 | 2 | 2 | 4 |
| Append 4 | 4 | 4 | 8 |
| Append 8 | 8 | 8 | 16 |

---

# 4.3 Capacity Growth Visualization

The capacity changes followed this pattern:

```
Initial:

Capacity = 1


After appending elements:

1
|
2
|
4
|
8
|
16
```

The capacity doubles whenever the array reaches its maximum storage limit.

---

# 4.4 Screenshots

![Console Output Screenshot](Screenshot.png)

---

# 5. Report Analysis Questions

## Q1: Run the script and record the exact sizes where capacity resizes occur.

The script was executed by appending values from `0` to `9`.

The dynamic array resized whenever:

```
size == capacity
```

The exact resize points were:

| Current Size Before Append | Resize Occurrence | Capacity Change |
|---|---|---|
| 1 | Before adding element 1 | 1 → 2 |
| 2 | Before adding element 2 | 2 → 4 |
| 4 | Before adding element 4 | 4 → 8 |
| 8 | Before adding element 8 | 8 → 16 |

Therefore, resizing occurred when the array sizes reached:

```
1, 2, 4, and 8
```

The final array state after inserting 10 elements was:

```
Size: 10
Capacity: 16
```

The unused capacity allows additional elements to be inserted without immediate resizing.

---

# 6. Complexity Analysis

| Operation | Time Complexity |
|---|---|
| Access by Index | O(1) |
| Append (Normal Case) | O(1) |
| Append (During Resize) | O(n) |
| Resize Operation | O(n) |

Where:

- `n` represents the number of existing elements copied during resizing.

---

# 7. Conclusion

This laboratory activity successfully demonstrated the implementation of a Dynamic Array using Python.

The program showed how dynamic arrays automatically increase their storage capacity when the current array becomes full. By doubling the capacity during resizing, the structure can efficiently handle a growing number of elements.

## Concepts Learned:

- Difference between fixed arrays and dynamic arrays.
- How size and capacity are managed separately.
- How resizing creates a larger storage area.
- How existing elements are copied during expansion.
- How index-based access works in arrays.

## Skills Developed:

- Implementing dynamic data structures.
- Managing memory allocation concepts.
- Understanding resizing algorithms.
- Analyzing operation efficiency.
- Evaluating time complexity.

Dynamic Arrays are important data structures because they provide the benefits of array indexing while allowing flexible growth. They are commonly used in programming languages and serve as the foundation for structures such as lists, vectors, and array-based collections.