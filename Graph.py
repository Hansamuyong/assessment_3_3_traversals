from collections import deque


class Graph:
    """GRAPH (BFS & DFS)"""

    def bfs(self):
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

    def dfs(self):
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

    def run(self):
        print("=== ASSESSMENT 3.3: NON-LINEAR DATA STRUCTURE ===")
        print("Student: Torres, Basilio III B. | BSIT - 2B\n")

        print("1. Graph BFS       :", "-".join(self.bfs()))
        print("2. Graph DFS       :", "-".join(self.dfs()))


if __name__ == "__main__":
    Graph().run()