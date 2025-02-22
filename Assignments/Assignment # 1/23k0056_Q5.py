'''Layyana Junaid 23k-0056 BSAI-4A'''

import heapq


romania_map = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Oradea': 71, 'Arad': 75},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

#Heuristic values 
heuristics = {
    'Arad': 366, 'Zerind': 374, 'Oradea': 380, 'Sibiu': 253, 'Timisoara': 329,
    'Lugoj': 244, 'Mehadia': 241, 'Drobeta': 242, 'Craiova': 160, 'Rimnicu Vilcea': 193,
    'Fagaras': 178, 'Pitesti': 100, 'Bucharest': 0, 'Giurgiu': 77, 'Urziceni': 80,
    'Hirsova': 151, 'Eforie': 161, 'Vaslui': 199, 'Iasi': 226, 'Neamt': 234
}

#Breadth-First Search (BFS) 
def bfs(start, goal):
    queue = [(start, [start])]
    visited = set()
    while queue:
        node, path = queue.pop(0)
        if node == goal:
            cost = sum(romania_map[path[i]][path[i+1]] for i in range(len(path)-1))
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor in romania_map[node]:
                queue.append((neighbor, path + [neighbor]))
    return None, float('inf')

#Uniform Cost Search
def ucs(start, goal):
    pq = [(0, start, [start])]
    visited = set()
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node == goal:
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor, weight in romania_map[node].items():
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
    return None, float('inf')

#Greedy Best-First Search 
def greedy_bfs(start, goal):
    pq = [(heuristics[start], start, [start])]
    visited = set()
    while pq:
        _, node, path = heapq.heappop(pq)
        if node == goal:
            cost = sum(romania_map[path[i]][path[i+1]] for i in range(len(path)-1))
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor in romania_map[node]:
                heapq.heappush(pq, (heuristics[neighbor], neighbor, path + [neighbor]))
    return None, float('inf')

#Iterative Deepening Depth-First Search
def dls(node, goal, depth, path, visited):
    if depth == 0 and node == goal:
        return path
    if depth > 0:
        visited.add(node)
        for neighbor in romania_map[node]:
            if neighbor not in visited:
                new_path = dls(neighbor, goal, depth - 1, path + [neighbor], visited)
                if new_path:
                    return new_path
        visited.remove(node)
    return None

def iddfs(start, goal):
    depth = 0
    while True:
        visited = set()
        path = dls(start, goal, depth, [start], visited)
        if path:
            cost = sum(romania_map[path[i]][path[i+1]] for i in range(len(path)-1))
            return path, cost
        depth += 1

def compare_algorithms(start, goal):
    print(f"\nFinding path from {start} to {goal}...\n")

    bfs_path, bfs_cost = bfs(start, goal)
    ucs_path, ucs_cost = ucs(start, goal)
    greedy_path, greedy_cost = greedy_bfs(start, goal)
    iddfs_path, iddfs_cost = iddfs(start, goal)

    print("Results:")
    print(f"BFS Path: {bfs_path}, Cost: {bfs_cost}")
    print(f"UCS Path: {ucs_path}, Cost: {ucs_cost}")
    print(f"Greedy Best-First Path: {greedy_path}, Cost: {greedy_cost}")
    print(f"IDDFS Path: {iddfs_path}, Cost: {iddfs_cost}")

source = "Arad"
destination = "Bucharest"
compare_algorithms(source, destination)
