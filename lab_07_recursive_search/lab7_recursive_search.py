def recursive_binary_search(arr, low, high, target):
    # 1. Base Case: If low > high, target is not in array
    if low > high:
        return -1

    # 2. Find the middle index
    mid = (low + high) // 2

    # If the middle element is the target, return its index
    if arr[mid] == target:
        return mid

    # 3. If arr[mid] is greater than target, search the left half
    if arr[mid] > target:
        return recursive_binary_search(arr, low, mid - 1, target)

    # 4. Otherwise, search the right half
    return recursive_binary_search(arr, mid + 1, high, target)


if __name__ == "__main__":
    data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target_val = 23

    result = recursive_binary_search(
        data, 0, len(data) - 1, target_val
    )

    print(f"Element found at index: {result}")
