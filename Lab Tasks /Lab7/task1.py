import copy

WHITE, BLACK = 'W', 'B'

class Board:
    def __init__(self):
        self.board = self.create_board()
    
    def create_board(self):
        board = [[' ' for _ in range(8)] for _ in range(8)]
        for row in range(3):
            for col in range((row + 1) % 2, 8, 2):
                board[row][col] = BLACK
        for row in range(5, 8):
            for col in range((row + 1) % 2, 8, 2):
                board[row][col] = WHITE
        return board

    def display(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def get_valid_moves(self, color):
        # Simplified: returns list of valid moves for a player
        # Ideally should check for captures and enforce them
        moves = []
        direction = -1 if color == WHITE else 1
        for r in range(8):
            for c in range(8):
                if self.board[r][c] == color:
                    for dc in [-1, 1]:
                        nr, nc = r + direction, c + dc
                        if 0 <= nr < 8 and 0 <= nc < 8 and self.board[nr][nc] == ' ':
                            moves.append(((r, c), (nr, nc)))
        return moves

    def move_piece(self, start, end):
        sr, sc = start
        er, ec = end
        self.board[er][ec] = self.board[sr][sc]
        self.board[sr][sc] = ' '

    def evaluate(self):
        w = sum(row.count(WHITE) for row in self.board)
        b = sum(row.count(BLACK) for row in self.board)
        return b - w

    def is_game_over(self):
        return not self.get_valid_moves(WHITE) or not self.get_valid_moves(BLACK)

def minimax(board, depth, maximizing, alpha, beta):
    if depth == 0 or board.is_game_over():
        return board.evaluate(), None
    color = BLACK if maximizing else WHITE
    best_move = None
    moves = board.get_valid_moves(color)

    if maximizing:
        max_eval = float('-inf')
        for move in moves:
            new_board = copy.deepcopy(board)
            new_board.move_piece(*move)
            eval, _ = minimax(new_board, depth - 1, False, alpha, beta)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in moves:
            new_board = copy.deepcopy(board)
            new_board.move_piece(*move)
            eval, _ = minimax(new_board, depth - 1, True, alpha, beta)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

# Demo loop (text-based)
game = Board()
game.display()
while not game.is_game_over():
    move = input("Enter your move (e.g., 2 3 3 4): ").split()
    move = ((int(move[0]), int(move[1])), (int(move[2]), int(move[3])))
    game.move_piece(*move)
    game.display()

    if game.is_game_over():
        break

    _, ai_move = minimax(game, 3, True, float('-inf'), float('inf'))
    if ai_move:
        game.move_piece(*ai_move)
        print(f"AI moves: {ai_move[0]} → {ai_move[1]}")
        game.display()

