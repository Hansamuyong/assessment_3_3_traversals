from collections import deque


class Binary:
    """BINARY TREE (BFS & DFS)"""

    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def build_binary_tree(self):
        """
        Constructs the Binary Tree from Page 1:
               T
             /   \\
            O     R
           / \\     \\
          R   E     S
        """
        root = self.Node('T')
        root.left = self.Node('O')
        root.right = self.Node('R')

        root.left.left = self.Node('R')
        root.left.right = self.Node('E')
        root.right.right = self.Node('S')
        return root

    def bfs(self, root):
        if not root:
            return []
        visited = []
        queue = deque([root])

        while queue:
            current = queue.popleft()
            visited.append(current.val)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return visited

    def dfs(self, root):
        # Pre-Order Traversal: Root -> Left -> Right
        if not root:
            return []
        visited = []
        stack = [root]

        while stack:
            current = stack.pop()
            visited.append(current.val)

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        return visited

    def run(self):
        root = self.build_binary_tree()

        print("=== ASSESSMENT 3.3: NON-LINEAR DATA STRUCTURE ===")
        print("Student: Torres, Basilio III B. | BSIT - 2B\n")

        print("1. Binary Tree BFS :", "-".join(self.bfs(root)))
        print("2. Binary Tree DFS :", "-".join(self.dfs(root)))


if __name__ == "__main__":
    Binary().run()