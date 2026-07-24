import ctypes

class DynamicArray:
    def __init__(self):
        self.size = 0          # number of elements
        self.capacity = 1      # initial capacity
        self.array = self._make_array(self.capacity)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        # Check if the index is valid
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        # Return the element at the given index
        return self.array[index]

    def append(self, element):
        # Resize if the array is full
        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        # Add the new element
        self.array[self.size] = element
        self.size += 1

    def _resize(self, new_capacity):
        # Print capacity change trace
        print(f"Resizing from {self.capacity} to {new_capacity}")

        # Create a new array with larger capacity
        new_array = self._make_array(new_capacity)

        # Copy existing elements
        for i in range(self.size):
            new_array[i] = self.array[i]

        # Replace old array with new array
        self.array = new_array
        self.capacity = new_capacity

    def _make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

# Testing script
if __name__ == "__main__":
    arr = DynamicArray()

    for i in range(10):
        arr.append(i)
        print(
            f"Appending {i} | Size: {len(arr)} | "
            f"Capacity: {arr.capacity} | Element at index {i}: {arr[i]}"
        )