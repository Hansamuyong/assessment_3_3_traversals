from collections import deque


# ==========================================
# PART 1: BINARY TREE (BFS & DFS)
# ==========================================
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_binary_tree():
    """
    Constructs the Binary Tree from Page 1:
           T
         /   \\
        O     R
       / \\     \\
      R   E     S
    """
    root = TreeNode('T')
    root.left = TreeNode('O')
    root.right = TreeNode('R')

    root.left.left = TreeNode('R')
    root.left.right = TreeNode('E')
    root.right.right = TreeNode('S')
    return root


def binary_tree_bfs(root):
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


def binary_tree_dfs(root):
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


# ==========================================
# PART 2: GRAPH (BFS & DFS)
# ==========================================
def graph_bfs():
    labels = {
        'T': 'T', 'O': 'O', 'R1': 'R',
        'R2': 'R', 'S': 'S', 'E': 'E'
    }
    adj_list = {
        'T': ['O', 'R1'],
        'O': ['T', 'R2', 'E'],
        'R1': ['T', 'S', 'E'],
        'R2': ['O', 'S'],
        'S': ['R1', 'R2', 'E'],
        'E': ['O', 'R1', 'S']
    }

    visited = set(['T'])
    queue = deque(['T'])
    traversal_order = []

    while queue:
        current = queue.popleft()
        traversal_order.append(labels[current])

        for neighbor in adj_list[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


def graph_dfs():
    labels = {
        'T': 'T', 'O': 'O', 'R_top': 'R',
        'S': 'S', 'E': 'E', 'R_bottom': 'R'
    }
    adj_list = {
        'T': ['O'],
        'O': ['T', 'R_top', 'R_bottom'],
        'R_top': ['O', 'S'],
        'S': ['R_top', 'E'],
        'E': ['S', 'R_bottom'],
        'R_bottom': ['O', 'E']
    }

    visited = set()
    stack = ['T']
    traversal_order = []

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            traversal_order.append(labels[current])

            for neighbor in reversed(adj_list[current]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal_order


# ==========================================
# EXECUTION & OUTPUT VERIFICATION
# ==========================================
if __name__ == "__main__":
    tree_root = build_binary_tree()

    print("=== ASSESSMENT 3.3: NON-LINEAR DATA STRUCTURE ===")
    print("Student: Torres, Basilio III B. | BSIT - 2B\n")

    print("1. Binary Tree BFS :", "-".join(binary_tree_bfs(tree_root)))
    print("2. Binary Tree DFS :", "-".join(binary_tree_dfs(tree_root)))
    print("3. Graph BFS       :", "-".join(graph_bfs()))
    print("4. Graph DFS       :", "-".join(graph_dfs()))