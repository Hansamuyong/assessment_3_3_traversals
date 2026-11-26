class DFSTree:
    """Assessment 3.6: DFS Methods in Tree"""

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def insert(self, root, value):
        """Insert a value into a binary search tree (duplicates discarded)."""
        if root is None:
            return self.Node(value)
        if value < root.value:
            root.left = self.insert(root.left, value)
        elif value > root.value:
            root.right = self.insert(root.right, value)
        return root

    def build_tree(self, name):
        """Build a tree from the letters of a name (no symbols, no duplicates)."""
        root = None
        for ch in name.upper():
            if ch.isalpha():
                root = self.insert(root, ch)
        return root

    def preorder(self, node, result):
        """Root -> Left -> Right"""
        if node:
            result.append(node.value)
            self.preorder(node.left, result)
            self.preorder(node.right, result)
        return result

    def inorder(self, node, result):
        """Left -> Root -> Right"""
        if node:
            self.inorder(node.left, result)
            result.append(node.value)
            self.inorder(node.right, result)
        return result

    def postorder(self, node, result):
        """Left -> Right -> Root"""
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.value)
        return result

    def dfs_iterative(self, root):
        if root is None:
            return []
        stack, result = [root], []
        while stack:
            node = stack.pop()
            result.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    def run(self):
        full_name = "Basilio B. Torres"
        root = self.build_tree(full_name)

        print("=== ASSESSMENT 3.6: DFS METHODS IN TREE ===")
        print("Student: Torres, Basilio III B. | BSIT - 2B\n")

        # Display results
        print("Full Name:          ", full_name)
        print("Preorder DFS:       ", self.preorder(root, []))
        print("Inorder DFS:        ", self.inorder(root, []))
        print("Postorder DFS:      ", self.postorder(root, []))
        print("Iterative DFS:      ", self.dfs_iterative(root))


if __name__ == "__main__":
    DFSTree().run()