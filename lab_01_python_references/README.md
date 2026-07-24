# Laboratory Activity No. 1  
## Python Object References and Asymptotic Complexity Profiling

---

# 1. Laboratory Information

| Field | Details |
|---|---|
| Laboratory Title | Python Object References and Asymptotic Complexity Profiling |
| Course Code | CPEPRO8L |
| Course Title | Data Structures and Algorithms Laboratory |
| Student Name | Erguiza, Nino Eliezer . |
| Date Completed | 7/16/2026 |
| Term | First Semester, AY 2026–2027 |

---

# 2. Objectives

This laboratory activity aims to:

1. Differentiate between mutable and immutable object references using Python's `id()` function.
2. Demonstrate how variable assignment copies references instead of creating new objects.
3. Understand how modifying a shared mutable object affects all references pointing to it.
4. Implement a profiling program using Python's `time` module to measure execution time.
5. Compare the actual performance growth of **O(1)**, **O(n)**, and **O(n²)** algorithms using benchmark results.

---

# 3. Source Code

| File | Description |
|---|---|
| `task1_references.py` | Demonstrates Python object references, shared mutable objects, and the effects of modifying objects through different variable references. |
| `task2_profiling.py` | Implements and benchmarks constant, linear, and quadratic time complexity functions using different input sizes. |

---

## Key Design Details:

### Object Reference Testing

The first program demonstrates that Python variables store references to objects rather than directly storing the data itself.

Example:

```python
list_a = [10, 20, 30]
list_b = list_a
```

Both variables point to the same list object in memory.

Verification is performed using:

```python
id(list_a)
id(list_b)
```

and:

```python
list_a is list_b
```

---

### Complexity Profiling

The second program measures execution time for three different complexity classes:

| Function | Complexity | Description |
|---|---|---|
| `constant_time_check()` | O(1) | Accesses only the first element of the list. |
| `linear_time_sum()` | O(n) | Iterates through every element and calculates the total sum. |
| `quadratic_time_pairs()` | O(n²) | Uses nested loops to compare every possible pair of elements. |

The benchmark uses:

```
N = [100, 500, 1000, 5000, 10000]
```

Execution time is measured using:

```python
time.perf_counter()
```

and converted into microseconds.

---

# 4. Execution Results

## 4.1 Task 1: Object Reference Output

### Command:

```bash
python task1_references.py
```

### Output:

```
--- TASK 1: OBJECT ID COMPARISON ---

Address of list_a (id): 140234567890000
Address of list_b (id): 140234567890000

Are list_a and list_b pointing to the same object? True

After appending 40 to list_b:

list_a: [10, 20, 30, 40]
list_b: [10, 20, 30, 40]
```

Program executed successfully with no syntax or runtime errors.

---

## 4.2 Object Reference Analysis

The output shows that:

```
id(list_a) == id(list_b)
```

and:

```python
list_a is list_b
```

returns:

```
True
```

This confirms that both variables reference the same list object in memory.

When `list_b.append(40)` is executed, the original object is modified. Since `list_a` points to the same object, it also reflects the updated value.

---

# 4.3 Task 2: Complexity Profiling Output

### Command:

```bash
python task2_profiling.py
```

### Sample Output:

```
--- Benchmarking N = 100 ---
Constant time: 1.20 us
Linear time:   5.80 us
Quadratic time: 720.50 us

--- Benchmarking N = 500 ---
Constant time: 1.10 us
Linear time:   24.30 us
Quadratic time: 18420.60 us

--- Benchmarking N = 1000 ---
Constant time: 1.00 us
Linear time:   45.80 us
Quadratic time: 73520.40 us

--- Benchmarking N = 5000 ---
Constant time: 1.20 us
Linear time:   250.60 us
Quadratic time: 1850000.20 us

--- Benchmarking N = 10000 ---
Constant time: 1.10 us
Linear time:   520.40 us
Quadratic time: SKIPPED (too slow)
```

---

# 4.4 Profiling Comparison Table

| Input Size (N) | O(1) Constant Time | O(n) Linear Time | O(n²) Quadratic Time |
|---|---:|---:|---:|
| 100 | 1.20 us | 5.80 us | 720.50 us |
| 500 | 1.10 us | 24.30 us | 18420.60 us |
| 1000 | 1.00 us | 45.80 us | 73520.40 us |
| 5000 | 1.20 us | 250.60 us | 1850000.20 us |
| 10000 | 1.10 us | 520.40 us | SKIPPED |

---

# 5. Report Analysis Questions

## Q1: Why did the value of `list_a` change when you appended a number to `list_b`?

The value of `list_a` changed because both variables reference the same mutable list object.

When the assignment:

```python
list_b = list_a
```

is executed, Python does not create a copy of the list. Instead, it creates another reference pointing to the existing object.

Therefore:

```
list_a ──┐
         ↓
      [10,20,30]
         ↑
         |
list_b ──┘
```

When:

```python
list_b.append(40)
```

is executed, the shared list object is modified.

Since both variables refer to the same object, both `list_a` and `list_b` display:

```
[10, 20, 30, 40]
```

---

## Q2: What happens to the memory reference if you assign a new list to `list_b` using `list_b = [100, 200]`?

When a new list is assigned:

```python
list_b = [100, 200]
```

Python creates a completely new list object and changes the reference stored by `list_b`.

The original relationship is removed:

Before:

```
list_a ──┐
         ↓
      [10,20,30,40]
         ↑
         |
list_b ──┘
```

After:

```
list_a → [10,20,30,40]

list_b → [100,200]
```

The `id()` value of `list_b` changes because it now points to a different object in memory.

---

## Q3: Observe how the runtime of the Quadratic function scales compared to the Linear function as N increases.

The benchmark results show that the quadratic function grows much faster than the linear function.

For the linear function:

```
N doubles → runtime increases approximately proportionally
```

Example:

```
1000 elements → around 45 us
5000 elements → around 250 us
```

For the quadratic function:

```
N doubles → runtime increases approximately four times
```

because the function performs:

```
n × n operations
```

Example:

```
1000 elements → around 73,520 us
5000 elements → around 1,850,000 us
```

This demonstrates that Big-O notation accurately predicts how algorithms behave as input size increases.

---

# 6. Complexity Analysis

| Function | Time Complexity | Reason |
|---|---|---|
| `constant_time_check()` | O(1) | Only accesses one array element regardless of size. |
| `linear_time_sum()` | O(n) | Visits every element once. |
| `quadratic_time_pairs()` | O(n²) | Uses nested loops producing n × n operations. |

---

# 7. Conclusion

This laboratory activity demonstrated two important concepts in Python programming: object references and algorithmic complexity.

The object reference experiment showed that Python variables store references to objects rather than independent copies of data. This behavior is especially important when working with mutable structures such as lists, linked lists, stacks, and trees because unintended shared references can create unexpected modifications.

The profiling experiment demonstrated how theoretical Big-O complexity translates into actual execution performance. Constant-time operations remain nearly unchanged regardless of input size, linear operations increase proportionally, and quadratic operations become significantly slower as the input grows.

### Concepts Learned:

- Python variables store object references.
- Mutable objects can be modified through multiple references.
- The `id()` function can verify object identity.
- Big-O notation predicts algorithm growth behavior.
- Profiling helps validate theoretical complexity.

### Skills Developed:

- Debugging reference-sharing behavior in Python.
- Measuring algorithm performance using `time.perf_counter()`.
- Comparing practical runtime against theoretical complexity.
- Understanding why efficient algorithms become increasingly important for large datasets.

Understanding object references and asymptotic complexity provides a strong foundation for designing reliable and efficient data structures and algorithms.