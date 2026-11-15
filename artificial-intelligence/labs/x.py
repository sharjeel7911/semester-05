from collections import deque


def bfs(graph: dict, start: str, goal: str) -> list | None:
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None


def dfs(graph: dict, start: str, goal: str) -> list | None:
    stack = [[start]]
    visited = {start}

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        # for neighbor in reversed(graph.get(node, [])):
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(path + [neighbor])
    return None


from heapq import heappop, heappush


def ucs(graph: dict, start: str, goal: str) -> tuple[list, int] | None:
    queue = [(0, [start])]
    visited = set()

    while queue:
        cost, path = heappop(queue)
        node = path[-1]

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)

            # for neighbor, weight in graph.get(node, []):
            for neighbor, weight in graph.get(node, {}).items():
                if neighbor not in visited:
                    heappush(queue, (cost + weight, path + [neighbor]))
    return None


def gbfs(graph: dict, heuristic: dict, start: str, goal: str) -> list | None:
    queue = [(heuristic[start], [start])]
    visited = set()

    while queue:
        hue, path = heappop(queue)
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    heappush(queue, (heuristic[neighbor], path + [neighbor]))

    return None


def astar(graph: dict, heuristic: dict, start: str, goal: str):
    queue = [(heuristic[start], 0, [start])]
    visited = set()

    while queue:
        fn, cost, path = heappop(queue)
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    new_cost = cost + weight
                    new_fn = new_cost + heuristic[neighbor]
                    heappush(queue, (new_fn, new_cost, path + [neighbor]))

    return None
