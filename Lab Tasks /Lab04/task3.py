import random
import time

class DeliveryRoute:
    def __init__(self, points, time_windows):
        self.points = points
        self.time_windows = time_windows
    
    def heuristic(self, current, next_point):
        return abs(current[0] - next_point[0]) + abs(current[1] - next_point[1])
    
    def find_route(self):
        current = (0, 0)  
        route = []
        while self.points:
            self.points.sort(key=lambda p: self.time_windows[p])
            next_point = min(self.points, key=lambda p: self.heuristic(current, p))
            if self.time_windows[next_point] >= time.time():
                route.append(next_point)
                self.points.remove(next_point)
                current = next_point
        return route
