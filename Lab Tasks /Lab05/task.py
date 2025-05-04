#Constraint Satisfaction Problem Question 
from itertools import permutations

class Product:
    def __init__(self, id, frequency, volume):
        self.id = id
        self.frequency = frequency
        self.volume = volume

class Slot:
    def __init__(self, id, distance):
        self.id = id
        self.distance = distance

def solve_warehouse_layout():
    products = [
        Product(1, 15, 2),
        Product(2, 8, 1),
        Product(3, 20, 3)
    ]
    
    slots = [
        Slot(1, 1),
        Slot(2, 2),
        Slot(3, 3)
    ]
    
    best_assignment = None
    min_cost = float('inf')
    
    for assignment in permutations(products):
        current_cost = 0
        valid = True
        
        # Calculate total cost for this assignment
        for i in range(len(slots)):
            current_cost += assignment[i].frequency * slots[i].distance
        
        # Check if this is the best assignment so far
        if current_cost < min_cost:
            min_cost = current_cost
            best_assignment = assignment
    
    # Display the best assignment
    print("Optimal Product Assignment:")
    print(f"{'Slot':<10}{'Distance':<10}{'Product':<10}{'Frequency':<10}{'Volume':<10}")
    for i in range(len(slots)):
        slot = slots[i]
        product = best_assignment[i]
        print(f"{slot.id:<10}{slot.distance:<10}{product.id:<10}{product.frequency:<10}{product.volume:<10}")
    
    print(f"\nTotal Weighted Distance: {min_cost}")

if __name__ == "__main__":
    solve_warehouse_layout()
