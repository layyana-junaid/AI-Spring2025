import sys
from collections import deque

class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid
        self.domains = {}
        self.initialize_domains()
        self.neighbors = self.build_neighbor_map()
        
    def initialize_domains(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != 0:
                    self.domains[(i, j)] = {self.grid[i][j]}
                else:
                    self.domains[(i, j)] = set(range(1, 10))
    
    def build_neighbor_map(self):
        neighbors = {}
        for i in range(9):
            for j in range(9):
                # Get row, column, and box neighbors
                row_neighbors = {(i, c) for c in range(9) if c != j}
                col_neighbors = {(r, j) for r in range(9) if r != i}
                
                box_i, box_j = i // 3, j // 3
                box_neighbors = {
                    (r, c) for r in range(box_i*3, box_i*3+3)
                    for c in range(box_j*3, box_j*3+3)
                    if (r, c) != (i, j)
                }
                
                neighbors[(i, j)] = row_neighbors | col_neighbors | box_neighbors
        return neighbors
    
    def is_consistent(self, var, value, assignment):
        for neighbor in self.neighbors[var]:
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True
    
    def select_unassigned_variable(self, assignment):
        unassigned = [v for v in self.domains if v not in assignment]
        return min(unassigned, key=lambda v: len(self.domains[v]))
    
    def order_domain_values(self, var, assignment):
        def count_conflicts(value):
            count = 0
            for neighbor in self.neighbors[var]:
                if neighbor not in assignment and value in self.domains[neighbor]:
                    count += 1
            return count
        
        return sorted(self.domains[var], key=count_conflicts)
    
    def ac3(self):
        queue = deque()
        for var in self.domains:
            for neighbor in self.neighbors[var]:
                queue.append((var, neighbor))
        
        while queue:
            xi, xj = queue.popleft()
            if self.revise(xi, xj):
                if not self.domains[xi]:
                    return False
                for xk in self.neighbors[xi] - {xj}:
                    queue.append((xk, xi))
        return True
    
    def revise(self, xi, xj):
        revised = False
        for x in set(self.domains[xi]):
            if all(x != y for y in self.domains[xj]):
                continue
            self.domains[xi].remove(x)
            revised = True
        return revised
    
    def backtrack(self, assignment):
        if len(assignment) == 81:
            return assignment
        
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.backtrack(assignment)
                if result is not None:
                    return result
                del assignment[var]
        return None
    
    def solve(self):
        if not self.ac3():
            return None
        
        assignment = {}
        for var in self.domains:
            if len(self.domains[var]) == 1:
                assignment[var] = next(iter(self.domains[var]))
        
        solution = self.backtrack(assignment)
        if solution:
            return self.solution_to_grid(solution)
        return None
    
    def solution_to_grid(self, solution):
        grid = [[0]*9 for _ in range(9)]
        for (i, j), val in solution.items():
            grid[i][j] = val
        return grid

def read_puzzles(filename):
    puzzles = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) == 81:
                puzzle = []
                for i in range(9):
                    row = []
                    for j in range(9):
                        char = line[i*9 + j]
                        row.append(0 if char == '.' else int(char))
                    puzzle.append(row)
                puzzles.append(puzzle)
    return puzzles

def grid_to_string(grid):
    return ''.join(str(grid[i][j]) for i in range(9) for j in range(9))

def solve_sudokus(input_file):
    puzzles = read_puzzles(input_file)
    for puzzle in puzzles:
        solver = SudokuSolver(puzzle)
        solution = solver.solve()
        if solution:
            print(grid_to_string(solution))
        else:
            print("No solution found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sudoku_solver.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    solve_sudokus(input_file)
