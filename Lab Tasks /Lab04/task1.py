import random
import time
from collections import deque

class MazeSolver:
    def __init__(self, maze, start, goals):
        self.maze = maze
        self.start = start
        self.goals = set(goals)
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def heuristic(self, point, goal):
        return abs(point[0] - goal[0]) + abs(point[1] - goal[1])
    
    def bfs(self, start, end):
        queue = deque([(start, [start])])
        visited = set()
        while queue:
            (x, y), path = queue.popleft()
            if (x, y) == end:
                return path
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if (nx, ny) in visited or self.maze[nx][ny] == "#":
                    continue
                queue.append(((nx, ny), path + [(nx, ny)]))
        return []
    
    def find_shortest_path(self):
        current = self.start
        total_path = []
        while self.goals:
            nearest_goal = min(self.goals, key=lambda g: self.heuristic(current, g))
            path = self.bfs(current, nearest_goal)
            if not path:
                return []
            total_path.extend(path[1:])
            current = nearest_goal
            self.goals.remove(nearest_goal)
        return total_path


