import heapq

graph = {
    'S': {'A': 1, 'B': 5},
    'A': {'C': 9, 'D': 5},
    'B': {'E': 2, 'F': 1},
    'C': {'G': 1},
    'D': {'G': 7},
    'E': {'G': 20},
    'F': {'G': 10},
    'G': {}
}

def ucs(start,goal):
    path=[]
    visited=set()
    cost=0
    queue=[(cost,start,path)]
    while queue:
        cost,current,path=heapq.heappop(queue)
        if current==goal:
            path.append(current)
            return cost,path
        if current not in visited:
            visited.add(current)
            path=path+[current]
            for x,y in graph.get(current,{}).items():
                heapq.heappush(queue,(cost+y,x,path))


    return float('inf'),None
                
print(ucs('S','G'))
                
