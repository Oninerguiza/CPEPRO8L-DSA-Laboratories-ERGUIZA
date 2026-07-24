class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        # Create a new node
        new_node = Node(data)

        # Point new node to current head
        new_node.next = self.head

        # Update head
        self.head = new_node

    def insert_tail(self, data):
        # Create a new node
        new_node = Node(data)

        # If the list is empty
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node
        temp = self.head
        while temp.next:
            temp = temp.next

        # Link the last node to the new node
        temp.next = new_node

    def delete_value(self, target):
        # Handle empty list
        if self.head is None:
            return False

        # If the head contains the target
        if self.head.data == target:
            self.head = self.head.next
            return True

        previous = self.head
        current = self.head.next

        # Search for the target node
        while current:
            if current.data == target:
                previous.next = current.next
                return True

            previous = current
            current = current.next

        # Target not found
        return False

    def search(self, target):
        temp = self.head

        while temp:
            if temp.data == target:
                return True
            temp = temp.next

        return False

    def display(self):
        temp = self.head
        elements = []

        while temp:
            elements.append(str(temp.data))
            temp = temp.next

        print(" -> ".join(elements) + " -> None")


if __name__ == "__main__":
    sll = SinglyLinkedList()

    sll.insert_head(10)
    sll.insert_head(20)
    sll.insert_tail(30)

    sll.display()  # Expected: 20 -> 10 -> 30 -> None

    sll.delete_value(10)

    sll.display()  # Expected: 20 -> 30 -> None

    print(f"Is 30 in list? {sll.search(30)}")  # Expected: True