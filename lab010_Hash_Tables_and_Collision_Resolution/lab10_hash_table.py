class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity=10):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")

        self.capacity = capacity
        self.buckets = [None] * capacity

    def _hash(self, key):
        # Sum ASCII values and calculate the bucket index.
        return sum(ord(char) for char in str(key)) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        current = self.buckets[index]

        # Update the value if the key already exists.
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        # Create a new node.
        new_node = HashNode(key, value)

        # Insert into an empty bucket.
        if self.buckets[index] is None:
            self.buckets[index] = new_node
        else:
            # Append to the linked list when a collision occurs.
            current = self.buckets[index]

            while current.next is not None:
                current = current.next

            current.next = new_node

    def get(self, key):
        # Search for a key in its bucket.
        index = self._hash(key)
        current = self.buckets[index]

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def display(self):
        for idx in range(self.capacity):
            chain = []
            temp = self.buckets[idx]

            while temp:
                chain.append(f"[{temp.key}: {temp.value}]")
                temp = temp.next

            print(f"Bucket {idx}: " + " -> ".join(chain))


if __name__ == "__main__":
    ht = HashTable(5)

    ht.put("Alice", 25)
    ht.put("Bob", 30)
    ht.put("Charlie", 35)

    print("Initial hash table:")
    ht.display()

    print("\nSearch result for Alice:", ht.get("Alice"))

    # Update an existing key.
    ht.put("Alice", 26)
    print("Updated value for Alice:", ht.get("Alice"))

    # Demonstrate a collision.
    ht.put("Eve", 22)
    ht.put("Vee", 28)

    print("\nHash table after inserting Eve and Vee:")
    ht.display()