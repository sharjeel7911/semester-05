# %%
import heapq

graph = {}


def ucs(start, goal):
    # (cost, node, path), heap breaks ties alphabetically
    frontier = [(0, start, [start])]
    best = {start: 0}
    explored = []

    while frontier:
        cost, node, path = heapq.heappop(frontier)
        if node in explored:  # stale entry, already expanded cheaper
            continue

        explored.append(node)
        if node == goal:
            print("Explored order:", explored)
            return cost, path

        for nb, w in graph[node].items():
            new_cost = cost + w
            if nb not in explored and new_cost < best.get(nb, float("inf")):
                best[nb] = new_cost
                heapq.heappush(frontier, (new_cost, nb, path + [nb]))

    print("Explored order:", explored)
    return float("inf"), None


def ucs_all(start):
    frontier = [(0, start)]
    dist = {start: 0}
    done = set()

    while frontier:
        cost, node = heapq.heappop(frontier)
        if node in done:
            continue
        done.add(node)

        for nb, w in graph[node].items():
            new_cost = cost + w
            if new_cost < dist.get(nb, float("inf")):
                dist[nb] = new_cost
                heapq.heappush(frontier, (new_cost, nb))

    return dist


graph1 = {
    "S": {"A": 1, "B": 5, "D": 3},
    "A": {"C": 2},
    "B": {"G": 10},
    "C": {"G": 3},
    "D": {"G": 9},
    "G": {},
}

graph2 = {
    "S": {"A": 4, "B": 1},
    "A": {"C": 3, "G": 8},
    "B": {"A": 2},
    "C": {"B": 1, "G": 4},
    "G": {},
}

graph3 = {
    "S": {"A": 2, "B": 3},
    "A": {"D": 4},
    "B": {"C": 1, "D": 2},
    "C": {"E": 5},
    "D": {"E": 2, "G": 6},
    "E": {"G": 1},
    "G": {},
}

# Exercise 5.1: weighted graph from the figure
graph = {
    "S": {"A": 3, "C": 2, "D": 2},
    "A": {},
    "B": {"E": 2},
    "C": {"F": 1},
    "D": {"B": 3, "G": 8},
    "E": {"G": 2},
    "F": {"E": 0, "G": 4},
    "G": {},
}
cost, path = ucs("S", "G")
print("5.1 Path:", path, "Total cost:", cost)

# Exercise 5.2
graph = graph1
print("\n5.2 Result:", ucs("S", "G"))

# Exercise 5.3
graph = graph2
cost, path = ucs("S", "G")
print("\n5.3 Path:", path, "Cost:", cost)

# Exercise 5.4
graph = graph3
cost, path = ucs("S", "G")
print("\n5.4 Path:", path, "Cost:", cost)
print("5.4 ucs('G', 'S'):", ucs("G", "S"))

# Exercise 5.5
graph = graph3
dist = ucs_all("S")
print("\n5.5 Lowest costs from S:", dist)
print("5.5 Farthest from S:", max(dist, key=dist.get))
