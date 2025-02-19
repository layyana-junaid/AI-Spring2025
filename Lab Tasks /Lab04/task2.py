import random 
import time
from collections import dequeue

class AStarDynamic:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
    
    def heuristic(self, node):
        return abs(node[0] - self.goal[0]) + abs(node[1] - self.goal[1])
    
    def get_neighbors(self, node):
        return self.graph.get(node, [])
    
    def a_star(self):
        open_set = [(0, self.start)]
        g_cost = {self.start: 0}
        came_from = {}
        while open_set:
            open_set.sort()  
            _, current = open_set.pop(0)
            if current == self.goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                return path[::-1]
            for neighbor, cost in self.get_neighbors(current):
                dynamic_cost = cost + random.randint(-1, 2) 
                tentative_g_cost = g_cost[current] + dynamic_cost
                if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                    g_cost[neighbor] = tentative_g_cost
                    open_set.append((tentative_g_cost + self.heuristic(neighbor), neighbor))
                    came_from[neighbor] = current
            time.sleep(0.5)  
        return []

