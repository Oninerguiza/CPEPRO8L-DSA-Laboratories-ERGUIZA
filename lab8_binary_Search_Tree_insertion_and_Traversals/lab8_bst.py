class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        # If key is smaller, insert into the left subtree
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)

        # Otherwise, insert into the right subtree
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def inorder(self, node):
        # Left -> Node -> Right
        if node is not None:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        # Node -> Left -> Right
        if node is not None:
            print(node.key, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        # Left -> Right -> Node
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=" ")


if __name__ == "__main__":
    tree = BST()

    elements = [50, 30, 70, 20, 40, 60, 80]

    for el in elements:
        tree.insert(el)

    print("Inorder Traversal:")
    tree.inorder(tree.root)
    print()

    print("Preorder Traversal:")
    tree.preorder(tree.root)
    print()

    print("Postorder Traversal:")
    tree.postorder(tree.root)
    print()
