import ctypes

class DynamicArray:
    def __init__(self):
        self.size = 0  # number of elements
        self.capacity = 1  # initial capacity
        self.array = self._make_array(self.capacity)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        # TODO: Check if the index is valid. If not, raise IndexError.
        # Otherwise, return the element at the index.
        pass

    def append(self, element):
        # TODO: Check if size equals capacity. If so, call _resize to double capacity.
        # Then, place the element at the current size index, and increment size.
        pass

    def _resize(self, new_capacity):
        # TODO: Implement the resizing logic.
        # 1. Print capacity change trace.
        # 2. Make a new array with new_capacity.
        # 3. Copy elements from self.array to the new array.
        # 4. Reassign self.array and self.capacity.
        pass

    def _make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

# Testing script
if __name__ == "__main__":
    arr = DynamicArray()
    for i in range(10):
        arr.append(i)
        print(f"Appending {i} | Size: {len(arr)} | Capacity: {arr.capacity} | Element at index {i}: {arr[i]}")
