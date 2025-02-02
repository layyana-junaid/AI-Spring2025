'''Layyana Junaid 23k-0056 BSAI-4A'''
'''Fire Fighting Robot'''

class FirefightingRobot:
    def __init__(self):
        self.grid = {
            "a": "Safe", "b": "Safe", "c": "🔥", 
            "d": "Safe", "e": "🔥", "f": "Safe", 
            "g": "Safe", "h": "Safe", "j": "🔥"
        }
        self.path = ["a", "b", "c", "d", "e", "f", "g", "h", "j"]
        self.current_position = "a"

    def display_environment(self):
        print("\nBuilding Status:")
        print(f"{self.grid['a']}  {self.grid['b']}  {self.grid['c']}")
        print(f"{self.grid['d']}  {self.grid['e']}  {self.grid['f']}")
        print(f"{self.grid['g']}  {self.grid['h']}  {self.grid['j']}")
        print("-" * 30)

    def move_and_extinguish(self):
        for room in self.path:
            self.current_position = room
            print(f"\n🤖 Moving to room {room}...")

            if self.grid[room] == "🔥":
                print(f"🔥 Fire detected in room {room}! Extinguishing...")
                self.grid[room] = "Safe"
                print(f"✅ Fire extinguished in {room}.")

            self.display_environment() 

robot = FirefightingRobot()
robot.display_environment()
robot.move_and_extinguish()
print("🏆 All fires have been extinguished!")
