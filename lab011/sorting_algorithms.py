"""Six hand-written sorting algorithms with comparison/movement counters.

Every function sorts a *copy* of the input and returns it, so the caller's
data is never modified. An optional SortStats object collects:

* comparisons - element-vs-element key comparisons
* movements   - writes of elements into list positions (a swap counts as 2)

No built-in sorting (sorted(), list.sort(), heapq) is used.
"""

from dataclasses import dataclass


@dataclass
class SortStats:
    comparisons: int = 0
    movements: int = 0


def bubble_sort(data, stats=None):
    """Bubble Sort with early exit. Stable, in place (O(1) extra), O(n^2) worst/avg, O(n) best."""
    arr = list(data)
    n = len(arr)
    comps = moves = 0
    for end in range(n - 1, 0, -1):
        swapped = False
        for i in range(end):
            comps += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                moves += 2
                swapped = True
        if not swapped:  # a full pass with no swap means sorted
            break
    if stats:
        stats.comparisons += comps
        stats.movements += moves
    return arr


def selection_sort(data, stats=None):
    """Selection Sort. Not stable, in place, always O(n^2) comparisons, at most n-1 swaps."""
    arr = list(data)
    n = len(arr)
    comps = moves = 0
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            comps += 1
            if arr[j] < arr[smallest]:
                smallest = j
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            moves += 2
    if stats:
        stats.comparisons += comps
        stats.movements += moves
    return arr


def insertion_sort(data, stats=None):
    """Insertion Sort. Stable, in place, O(n^2) worst/avg, O(n) best (already sorted)."""
    arr = list(data)
    comps = moves = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comps += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]  # shift right
                moves += 1
                j -= 1
            else:
                break
        if j + 1 != i:
            arr[j + 1] = key
            moves += 1
    if stats:
        stats.comparisons += comps
        stats.movements += moves
    return arr


def merge_sort(data, stats=None):
    """Top-down Merge Sort. Stable, O(n log n) always, O(n) auxiliary buffer."""
    arr = list(data)
    n = len(arr)
    buf = [None] * n  # the single auxiliary buffer (O(n) extra space)
    counters = [0, 0]  # [comparisons, movements]

    def merge(lo, mid, hi):
        # copy left half into buffer, merge back into arr
        for k in range(lo, mid):
            buf[k] = arr[k]
        counters[1] += mid - lo
        i, j, k = lo, mid, lo
        while i < mid and j < hi:
            counters[0] += 1
            if arr[j] < buf[i]:
                arr[k] = arr[j]
                j += 1
            else:  # <= keeps equal items in original order (stable)
                arr[k] = buf[i]
                i += 1
            k += 1
            counters[1] += 1
        while i < mid:
            arr[k] = buf[i]
            i += 1
            k += 1
            counters[1] += 1
        # any remainder of the right half is already in place

    def sort(lo, hi):
        if hi - lo < 2:
            return
        mid = (lo + hi) // 2
        sort(lo, mid)
        sort(mid, hi)
        merge(lo, mid, hi)

    sort(0, n)
    if stats:
        stats.comparisons += counters[0]
        stats.movements += counters[1]
    return arr


def quick_sort(data, stats=None):
    """Quick Sort: median-of-three pivot + three-way (Dutch flag) partitioning.

    Pivot strategy: the median of the first, middle and last element. This
    avoids the O(n^2) behaviour plain first/last-element pivots show on sorted
    and reverse-sorted input. Three-way partitioning groups all keys equal to
    the pivot together so duplicate-heavy input does not degrade either.
    Extra space: O(log n) stack - always recurse on the smaller side and loop
    on the larger. Not stable.
    """
    arr = list(data)
    counters = [0, 0]

    def median_of_three(lo, hi):
        mid = (lo + hi) // 2
        a, b, c = arr[lo], arr[mid], arr[hi]
        counters[0] += 3
        if a < b:
            if b < c:
                return b
            return c if a < c else a
        if a < c:
            return a
        return c if b < c else b

    def sort(lo, hi):
        while lo < hi:
            pivot = median_of_three(lo, hi)
            lt, i, gt = lo, lo, hi
            while i <= gt:
                counters[0] += 1
                if arr[i] < pivot:
                    arr[lt], arr[i] = arr[i], arr[lt]
                    counters[1] += 2
                    lt += 1
                    i += 1
                else:
                    counters[0] += 1
                    if arr[i] > pivot:
                        arr[i], arr[gt] = arr[gt], arr[i]
                        counters[1] += 2
                        gt -= 1
                    else:
                        i += 1
            # arr[lo:lt] < pivot, arr[lt:gt+1] == pivot, arr[gt+1:hi+1] > pivot
            if lt - lo < hi - gt:
                sort(lo, lt - 1)
                lo = gt + 1
            else:
                sort(gt + 1, hi)
                hi = lt - 1

    sort(0, len(arr) - 1)
    if stats:
        stats.comparisons += counters[0]
        stats.movements += counters[1]
    return arr


def heap_sort(data, stats=None):
    """Heap Sort (max-heap). Not stable, in place (O(1) extra), O(n log n) always."""
    arr = list(data)
    n = len(arr)
    counters = [0, 0]

    def sift_down(root, size):
        while True:
            child = 2 * root + 1
            if child >= size:
                return
            if child + 1 < size:
                counters[0] += 1
                if arr[child + 1] > arr[child]:
                    child += 1
            counters[0] += 1
            if arr[child] > arr[root]:
                arr[root], arr[child] = arr[child], arr[root]
                counters[1] += 2
                root = child
            else:
                return

    for start in range(n // 2 - 1, -1, -1):  # build max-heap
        sift_down(start, n)
    for end in range(n - 1, 0, -1):  # repeatedly move max to the end
        arr[0], arr[end] = arr[end], arr[0]
        counters[1] += 2
        sift_down(0, end)
    if stats:
        stats.comparisons += counters[0]
        stats.movements += counters[1]
    return arr


ALGORITHMS = {
    "Bubble": bubble_sort,
    "Selection": selection_sort,
    "Insertion": insertion_sort,
    "Merge": merge_sort,
    "Quick": quick_sort,
    "Heap": heap_sort,
}
QUADRATIC = {"Bubble", "Selection", "Insertion"}
