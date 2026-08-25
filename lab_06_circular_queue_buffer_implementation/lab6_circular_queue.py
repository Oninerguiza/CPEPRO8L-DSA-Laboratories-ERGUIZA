class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            print("Queue overflow: cannot enqueue.")
            return False

        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow: cannot dequeue.")
            return None

        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def display(self):
        print(f"Queue array: {self.queue} | Head: {self.head} | Tail: {self.tail}")


if __name__ == "__main__":
    cq = CircularQueue(5)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    print(f"Dequeued: {cq.dequeue()}")  # Expected: Dequeued: 1
    cq.enqueue(4)
    cq.display()