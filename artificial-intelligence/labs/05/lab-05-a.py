# %%
from collections import deque


class Node:
    def __init__(self: Node, value: str) -> None:
        self.value = value
        self.neighbors = []


class Graph:
    def __init__(self: Graph) -> None:
        self.nodes = {}

    def add_node(self: Graph, value: str) -> None:
        if value not in self.nodes:
            self.nodes[value] = Node(value)

    def add_edge(
        self: Graph, source: str, destination: str, directed: bool = False
    ) -> None:
        if source in self.nodes and destination in self.nodes:
            self.nodes[source].neighbors.append(self.nodes[destination])

            if not directed:
                self.nodes[destination].neighbors.append(self.nodes[source])

    def build(self: Graph, adjacency: dict, directed: bool = True) -> None:
        for node, neighbors in adjacency.items():
            self.add_node(node)

            for neighbor in neighbors:
                self.add_node(neighbor)

        for node, neighbors in adjacency.items():
            for neighbor in neighbors:
                self.add_edge(node, neighbor, directed)

    def bfs(self, start, goal, return_path=False, check_visited=True, max_steps=100):
        self.last_stopped = False
        queue = deque([start])
        visited = {start}
        parent = {start: None}
        order = []

        while queue:
            current = queue.popleft()
            order.append(current)

            if current == goal:
                if not return_path:
                    return order
                path, node = [], goal
                while node is not None:
                    path.append(node)
                    node = parent[node]
                return path[::-1]

            if len(order) > max_steps:
                self.last_stopped = True
                return None

            for neighbor in sorted(
                self.nodes[current].neighbors, key=lambda n: n.value
            ):
                if check_visited and neighbor.value in visited:
                    continue
                visited.add(neighbor.value)
                parent.setdefault(neighbor.value, current)
                queue.append(neighbor.value)
        return None

    def dfs(self, start, goal, return_path=False, check_visited=True, max_steps=100):
        self.last_stopped = False
        stack = [(start, None)]  # (node, parent) pairs
        visited = set()
        parent = {}
        order = []

        while stack:
            current, par = stack.pop()

            if check_visited and current in visited:
                continue
            visited.add(current)
            parent.setdefault(current, par)
            order.append(current)

            if current == goal:
                if not return_path:
                    return order
                path, node = [], goal
                while node is not None:
                    path.append(node)
                    node = parent[node]
                return path[::-1]

            if len(order) > max_steps:
                self.last_stopped = True
                return None

            for neighbor in sorted(
                self.nodes[current].neighbors, key=lambda n: n.value, reverse=True
            ):
                if not check_visited or neighbor.value not in visited:
                    stack.append((neighbor.value, current))
        return None


graph1 = {
    "S": ["A", "B"],
    "A": ["C", "D"],
    "B": ["E"],
    "C": ["F"],
    "D": ["G"],
    "E": [],
    "F": ["G"],
    "G": [],
}

graph2 = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E", "F"],
    "D": ["G", "H"],
    "E": ["I", "J"],
    "F": ["K", "L"],
    "G": [],
    "H": [],
    "I": [],
    "J": [],
    "K": [],
    "L": [],
}

graph3 = {"A": ["B"], "B": ["C", "D"], "C": ["A", "E"], "D": ["F"], "E": ["F"], "F": []}

# ====================================================================================================

# %%
# Exercise 4.1.
# Using Breadth First Search (BFS) algorithm, write out the order in which nodes are added to the explored
# set, with start state S and goal state G. Break ties in alphabetical order. Additionally, what is the path
# returned by each algorithm? What is the total cost of each path?

weights41 = {
    ("S", "A"): 3,
    ("S", "C"): 2,
    ("S", "D"): 2,
    ("D", "B"): 3,
    ("B", "E"): 2,
    ("C", "F"): 1,
    ("F", "E"): 0,
    ("F", "G"): 4,
    ("E", "G"): 2,
    ("D", "G"): 8,
}
adj41 = {}
for u, v in weights41:
    adj41.setdefault(u, []).append(v)

graph = Graph()
graph.build(adj41)

for name, search in (("BFS", graph.bfs), ("DFS", graph.dfs)):
    print(f"{name} explored:", search("S", "G"))
    path = search("S", "G", return_path=True)
    cost = sum(weights41[(a, b)] for a, b in zip(path, path[1:]))
    print(f"{name} path:", path, "Cost:", cost)

# ====================================================================================================

# %%
# Exercise 4.2.
# In the following exercises a graph is stored in Python as a dictionary: each key is a node and its list holds
# the nodes that it points to. All edges are one-way, so if A points to B you can go from A to B, but not from
# B to A. Graph 1 (Figure 4-6) is stored as follows.
# graph1 = {'S': ['A', 'B'], 'A': ['C', 'D'],
# 'B': ['E'], 'C': ['F'],
# 'D': ['G'], 'E': [], 'F': ['G'], 'G': []}
# Implement two functions, bfs(start, goal) and dfs(start, goal). bfs must use a queue
# and dfs must use a stack. Both functions read the global variable graph, visit the neighbors of a node
# in alphabetical order, test for the goal when a node is removed from the frontier, and return the list of
# nodes in the order in which they were visited (ending with the goal), or None if the goal cannot be
# reached. Hint: for dfs, push the neighbors onto the stack in reversed order so that the alphabetically first
# neighbor is popped first.
# Set graph = graph1, then run bfs('S', 'G') and dfs('S', 'G') and print both results.

# %%
graph = Graph()
graph.build(graph1)

print("BFS:", graph.bfs("S", "G"))
print("DFS:", graph.dfs("S", "G"))

# ====================================================================================================

# %%
# Exercise 4.3.
# Graph 2 (Figure 4-7) is the tree from Figure 4-2. It is stored as follows.
# graph2 = {'A': ['B', 'C'], 'B': ['D'],
# 'C': ['E', 'F'], 'D': ['G', 'H'],
# 'E': ['I', 'J'], 'F': ['K', 'L'],
# 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': []}
# Set graph = graph2 and run bfs and dfs from 'A' to 'J', and then from 'A' to 'G'. For each run, print
# the result and its length using len(). Which algorithm visits fewer nodes in each case?

graph = Graph()
graph.build(graph2)

for goal in ["J", "G"]:
    bfs_result = graph.bfs("A", goal)
    dfs_result = graph.dfs("A", goal)

    print(f"\nA to {goal}")
    print("BFS:", bfs_result, "Length:", len(bfs_result))
    print("DFS:", dfs_result, "Length:", len(dfs_result))

# ====================================================================================================

# %%
# Exercise 4.4.
# Graph 3 (Figure 4-8) contains a cycle: A points to B, B points to C, and C points back to A. It is stored as
# follows.
# graph3 = {'A': ['B'], 'B': ['C', 'D'],
# 'C': ['A', 'E'], 'D': ['F'],
# 'E': ['F'], 'F': []}
#   a. Set graph = graph3 and run bfs('A', 'F') and dfs('A', 'F') without skipping
# nodes that were already visited. Describe what happens in each case and explain why. (If a
# program does not stop, interrupt it manually.)
#   b. Modify both functions so that a node which has already been visited is skipped (use a visited
# set). Run both functions again on graph3 and print the results.

# %%
graph = Graph()
graph.build(graph3)

# 4.4a: no visited check (DFS loops, so it stops at max_steps)
print("4.4a BFS:", graph.bfs("A", "F", check_visited=False))
print("4.4a DFS:", graph.dfs("A", "F", check_visited=False))
print("4.4a DFS stopped by loop:", graph.last_stopped)

# 4.4b: with visited check
print("4.4b BFS:", graph.bfs("A", "F"))
print("4.4b DFS:", graph.dfs("A", "F"))

# ====================================================================================================

# %%
# Exercise 4.5.
# The functions above return the order in which the nodes were visited, not the path from the start to the
# goal. Modify bfs so that it returns the actual path (for example, keep a dictionary parent that stores
# the node from which each node was reached, and rebuild the path backwards from the goal). Test it on
# graph1 with start 'S' and goal 'G'.

# %%
graph = Graph()
graph.build(graph1)

print("Path:", graph.bfs("S", "G", return_path=True))
