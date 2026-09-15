# Laboratory Activity No. 7 — Recursion Tracing & Binary Search

*Course Code:* CPEPRO8L  
*Course Title:* Data Structures and Algorithms  
*Term:* First Semester, AY 2026–2027

## 1. Objectives

* Understand recursive execution, base cases, and call nesting.
* Implement and test a recursive Binary Search algorithm.
* Trace the execution stack frames during recursive function calls.
* Compare the space complexities of iterative and recursive Binary Search.

## 2. Files

| File | Description |
|---|---|
| lab7_recursive_search.py | Completed implementation of the recursive Binary Search function and required demonstration. |
| README.md | Documentation containing the objectives, methodology, execution output, stack trace, analysis, and conclusion. |

## 3. Methodology

The Recursive Binary Search algorithm is implemented using a sorted Python list. Binary Search works by repeatedly dividing the search range into two halves.

The recursive function receives four parameters:

recursive_binary_search(arr, low, high, target)

Where:

* arr — the sorted array being searched.
* low — the starting index of the current search range.
* high — the ending index of the current search range.
* target — the value being searched for.

### Base Case

The first step is to check whether the search range is empty:

if low > high: return -1

If low becomes greater than high, there are no elements left to search. The function returns -1, indicating that the target was not found.

### Finding the Middle Index

The middle position is calculated using:

mid = (low + high) // 2

The element at the middle position is then compared with the target.

### Target Found

If the middle element is equal to the target, its index is returned:

if arr[mid] == target: return mid

### Searching the Left Half

If the middle element is greater than the target, the target can only be located in the left half:

return recursive_binary_search(arr, low, mid - 1, target)

### Searching the Right Half

If the middle element is smaller than the target, the target can only be located in the right half:

return recursive_binary_search(arr, mid + 1, high, target)

Each recursive call reduces the search area approximately by half until the target is found or the search range becomes empty.

## 4. Source Code

The completed lab7_recursive_search.py file contains:

    def recursive_binary_search(arr, low, high, target):
        # Base Case: target is not in the array
        if low > high:
            return -1

        # Find the middle index
        mid = (low + high) // 2

        # Target found
        if arr[mid] == target:
            return mid

        # Search the left half
        if arr[mid] > target:
            return recursive_binary_search(arr, low, mid - 1, target)

        # Search the right half
        return recursive_binary_search(arr, mid + 1, high, target)


    if _name_ == "_main_":
        data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
        target_val = 23

        result = recursive_binary_search(
            data, 0, len(data) - 1, target_val
        )

        print(f"Element found at index: {result}")

## 5. Execution & Output

The program was executed using:

    python3 lab7_recursive_search.py

The program uses the following sorted array:

    [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

The target value is:

    23

The expected output is:

    Element found at index: 5

The result is 5 because the value 23 is located at index 5.

## 6. Report Analysis Questions

### 6.1 Execution Stack Trace When Searching for 56

To demonstrate recursive execution, the target value was changed from 23 to 56.

The search begins with:

    recursive_binary_search(arr, 0, 9, 56)

The first middle index is calculated as:

    mid = (0 + 9) // 2
    mid = 4

The value at index 4 is:

    arr[4] = 16

Since 16 < 56, the target must be in the right half of the array. The function makes another recursive call:

    recursive_binary_search(arr, 5, 9, 56)

The new middle index is:

    mid = (5 + 9) // 2
    mid = 7

The value at index 7 is:

    arr[7] = 56

Since the middle element is equal to the target, the function returns 7.

### Stack Trace Table

| Call | low | high | mid | arr[mid] | Action |
|---|---:|---:|---:|---:|---|
| 1 | 0 | 9 | 4 | 16 | Search right half |
| 2 | 5 | 9 | 7 | 56 | Target found |

### Execution Stack Diagram

                    TOP OF STACK
    ┌──────────────────────────────────────────────┐
    │ Call 2                                       │
    │ recursive_binary_search(arr, 5, 9, 56)      │
    │                                              │
    │ low = 5                                      │
    │ high = 9                                     │
    │ mid = 7                                      │
    │ arr[7] = 56                                  │
    │                                              │
    │ Target found → return 7                     │
    └──────────────────────────────────────────────┘
                        ↑
                        │
                        │ recursive call
                        │
    ┌──────────────────────────────────────────────┐
    │ Call 1                                       │
    │ recursive_binary_search(arr, 0, 9, 56)      │
    │                                              │
    │ low = 0                                      │
    │ high = 9                                     │
    │ mid = 4                                      │
    │ arr[4] = 16                                  │
    │                                              │
    │ 16 < 56 → search right half                 │
    └──────────────────────────────────────────────┘
                     BOTTOM OF STACK

The complete call sequence is:

    recursive_binary_search(arr, 0, 9, 56)
                        ↓
    recursive_binary_search(arr, 5, 9, 56)
                        ↓
                      return 7

The final output for a search for 56 would be:

    Element found at index: 7

### 6.2 Why Missing Base Cases Lead to Stack Overflow Errors

A base case is the condition that tells a recursive function when to stop calling itself.

In this implementation, the base case is:

    if low > high:
        return -1

This condition handles the situation where the target does not exist in the array. Once the search range becomes empty, the function stops making recursive calls and returns -1.

Without a base case, a recursive function may continue calling itself indefinitely. Every recursive call creates a new stack frame containing the function's parameters and local information.

For example:

    Call 1
      ↓
    Call 2
      ↓
    Call 3
      ↓
    Call 4
      ↓
    ...
      ↓
    Call N

The stack would continue growing as more function calls are added.

Eventually, the program reaches Python's maximum recursion depth. This results in an error similar to:

    RecursionError: maximum recursion depth exceeded

Therefore, a base case is necessary to ensure that recursive execution eventually terminates and does not continuously consume stack memory.

## 7. Recursive Binary Search Trace

The following table summarizes the search process when looking for 56:

| Step | Low | High | Mid | Middle Value | Decision |
|---|---:|---:|---:|---:|---|
| 1 | 0 | 9 | 4 | 16 | Search right half |
| 2 | 5 | 9 | 7 | 56 | Target found |

The search only requires two recursive calls because Binary Search eliminates approximately half of the remaining elements during each step.

## 8. Complexity Analysis

Binary Search has a time complexity of O(log n) because the search range is divided approximately in half after every comparison.

| Implementation | Time Complexity | Space Complexity |
|---|---|---|
| Iterative Binary Search | O(log n) | O(1) |
| Recursive Binary Search | O(log n) | O(log n) |

### Iterative Binary Search

An iterative implementation uses a loop instead of recursive function calls. It only requires a constant number of additional variables.

Therefore, its auxiliary space complexity is:

O(1)

### Recursive Binary Search

The recursive implementation creates a new stack frame for every recursive call. Since the search range is divided by approximately two each time, the maximum number of nested calls is:

O(log n)

Therefore, the auxiliary space complexity of recursive Binary Search is:

O(log n)

The recursive version is less space-efficient than the iterative version because of the memory required by the call stack.

## 9. Advantages of Recursive Binary Search

The recursive approach has several advantages:

* The implementation closely represents the divide-and-conquer nature of Binary Search.
* The code can be concise and easy to understand once recursion is understood.
* Each recursive call works on a smaller portion of the original problem.
* It provides practical experience with function call stacks and recursive execution.

However, it also uses additional stack memory compared with the iterative implementation.

## 10. Overflow and Underflow Considerations

Unlike a queue or stack implementation, Binary Search does not have traditional data-structure overflow and underflow conditions.

Instead, the important terminating condition is the empty search range:

    if low > high:
        return -1

This condition prevents the algorithm from continuing to search when there are no valid indices remaining.

For example, if the target is not present, the recursive calls eventually produce a situation where:

    low > high

At that point, the function returns -1.

## 11. Conclusion

This laboratory activity demonstrated the implementation and execution of Recursive Binary Search using Python. The algorithm successfully searches a sorted array by repeatedly dividing the search range into two smaller sections.

The execution trace for the target value 56 demonstrated how recursive calls create nested stack frames. The first call searched indices 0 through 9, found 16 at the middle position, and continued searching the right half. The second call searched indices 5 through 9 and found 56 at index 7.

The activity also demonstrated the importance of the base case. Without a base case, recursive calls may continue indefinitely, causing the call stack to exceed Python's recursion limit and resulting in a RecursionError.

Finally, the complexity comparison showed that both iterative and recursive Binary Search have O(log n) time complexity. However, iterative Binary Search requires O(1) auxiliary space, while recursive Binary Search requires O(log n) space because of the recursive call stack.