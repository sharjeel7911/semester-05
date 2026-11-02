# %%
from collections import deque

graph = {}


def bfs(start, goal):
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        if node == goal:
            path, n = [], goal
            while n is not None:
                path.append(n)
                n = parent[n]
            return order, path[::-1]

        for nb in sorted(graph[node]):
            if nb not in visited:
                visited.add(nb)
                parent[nb] = node
                queue.append(nb)
    return None, None


def dfs(start, goal):
    stack = [start]
    visited = set()
    parent = {start: None}
    order = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)

        if node == goal:
            path, n = [], goal
            while n is not None:
                path.append(n)
                n = parent[n]
            return order, path[::-1]

        for nb in sorted(graph[node], reverse=True):
            if nb not in visited:
                stack.append(nb)
                parent.setdefault(nb, node)
    return None, None


def path_cost(path, weights):
    return sum(weights[(a, b)] for a, b in zip(path, path[1:]))


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
graph3 = {
    "A": ["B"],
    "B": ["C", "D"],
    "C": ["A", "E"],
    "D": ["F"],
    "E": ["F"],
    "F": [],
}

# Exercise 4.1: weighted graph from the figure
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
graph = {}
for u, v in weights41:
    graph.setdefault(u, []).append(v)
for n in "SABCDEFG":
    graph.setdefault(n, [])

order, path = bfs("S", "G")
print("4.1 BFS explored:", order)
print("4.1 BFS path:", path, "Cost:", path_cost(path, weights41))
order, path = dfs("S", "G")
print("4.1 DFS explored:", order)
print("4.1 DFS path:", path, "Cost:", path_cost(path, weights41))

# Exercise 4.2: graph1, S to G
graph = graph1
print("\n4.2 BFS:", bfs("S", "G")[0])
print("4.2 DFS:", dfs("S", "G")[0])

# Exercise 4.3: graph2, A to J and A to G
graph = graph2
for goal in ["J", "G"]:
    b, _ = bfs("A", goal)
    d, _ = dfs("A", goal)
    print(f"\nA to {goal}")
    print("BFS:", b, "Length:", len(b))
    print("DFS:", d, "Length:", len(d))

# Exercise 4.4b: graph3 with visited check (both functions always use it)
graph = graph3
print("\n4.4b BFS:", bfs("A", "F")[0])
print("4.4b DFS:", dfs("A", "F")[0])

# Exercise 4.5: BFS path from S to G on graph1
graph = graph1
print("\n4.5 Path:", bfs("S", "G")[1])
