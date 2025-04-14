import random

class Battleship:
    def __init__(self):
        self.grid_size = 10
        self.player_grid = [['-' for _ in range(10)] for _ in range(10)]
        self.ai_grid = [['-' for _ in range(10)] for _ in range(10)]
        self.ai_hits = []

        # Simulate hidden ship at B4, B5, B6
        self.ships = {'B4': True, 'B5': True, 'B6': True}

    def attack(self, coord):
        if coord in self.ships:
            del self.ships[coord]
            return "Hit!" if self.ships else "Sunk!"
        return "Miss"

    def ai_attack(self):
        if self.ai_hits:
            # Focus on adjacent
            last_hit = self.ai_hits[-1]
            r, c = ord(last_hit[0]) - 65, int(last_hit[1]) - 1
            options = [(r+dr, c+dc) for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]]
        else:
            options = [(random.randint(0, 9), random.randint(0, 9))]

        for r, c in options:
            if 0 <= r < 10 and 0 <= c < 10:
                coord = f"{chr(65 + r)}{c+1}"
                if self.ai_grid[r][c] == '-':
                    result = self.attack(coord)
                    self.ai_grid[r][c] = 'X' if 'Hit' in result or 'Sunk' in result else 'O'
                    print(f"AI attacks: {coord} → {result}")
                    if "Hit" in result:
                        self.ai_hits.append(coord)
                    return

    def player_turn(self):
        coord = input("Enter attack (e.g., B4): ").strip().upper()
        result = self.attack(coord)
        print(f"Player attacks: {coord} → {result}")

game = Battleship()
while game.ships:
    game.player_turn()
    if not game.ships:
        print("Player wins!")
        break
    game.ai_attack()
    if not game.ships:
        print("AI wins!")
        break
