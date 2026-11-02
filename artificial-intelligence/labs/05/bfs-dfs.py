graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

def bfs(start, goal):
    path = []
    visited = set()
    queue = [start]

    while queue:
        current = queue.pop(0)
        if current == goal:
            path.append(current)
            return path
        if current not in visited:
            visited.add(current)
            path.append(current)
            for neighbor in graph.get(current, []):
                queue.append(neighbor)
    return None

print(bfs('S', 'G'))


def dfs(start, goal):
    path = []
    visited = set()
    stack = [start]

    while stack:
        current = stack.pop()
        if current == goal:
            path.append(current)
            return path
        if current not in visited:
            visited.add(current)
            path.append(current)
            for neighbor in reversed(graph.get(current, [])):
                stack.append(neighbor)
    return None

print(dfs('S', 'G'))
