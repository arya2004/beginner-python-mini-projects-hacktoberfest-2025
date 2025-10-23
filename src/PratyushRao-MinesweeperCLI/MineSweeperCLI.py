import random
import os

# --- Game Setup ---
class Minesweeper:
    def __init__(self, size=8, mines=10):
        self.size = size
        self.mines = mines
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.display = [['■' for _ in range(size)] for _ in range(size)]
        self.revealed = set()
        self.flags = set()
        self._place_mines()

    def _place_mines(self):
        positions = set()
        while len(positions) < self.mines:
            x, y = random.randrange(self.size), random.randrange(self.size)
            positions.add((x, y))
        self.mines_pos = positions
        for x, y in positions:
            self.board[x][y] = '*'
        # Fill numbers around mines
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] == '*':
                    continue
                self.board[x][y] = str(self._count_adjacent_mines(x, y))

    def _count_adjacent_mines(self, x, y):
        cnt = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if (i, j) in self.mines_pos:
                    cnt += 1
        return cnt

    def reveal(self, x, y):
        if (x, y) in self.flags or (x, y) in self.revealed:
            return True
        if (x, y) in self.mines_pos:
            return False  # hit a mine
        self._flood_fill(x, y)
        return True

    def _flood_fill(self, x, y):
        if (x, y) in self.revealed or not (0 <= x < self.size and 0 <= y < self.size):
            return
        self.revealed.add((x, y))
        self.display[x][y] = self.board[x][y]
        if self.board[x][y] == '0':
            self.display[x][y] = ' '
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i < self.size and 0 <= j < self.size:
                        self._flood_fill(i, j)

    def toggle_flag(self, x, y):
        if (x, y) in self.revealed:
            return
        if (x, y) in self.flags:
            self.flags.remove((x, y))
            self.display[x][y] = '■'
        else:
            self.flags.add((x, y))
            self.display[x][y] = '⚑'

    def check_win(self):
        return len(self.revealed) == self.size * self.size - self.mines

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("   " + " ".join(map(str, range(self.size))))
        for i, row in enumerate(self.display):
            print(f"{i:2} " + " ".join(row))


# --- Game Loop ---
def play():
    size = int(input("Enter grid size (e.g. 8): "))
    mines = int(input("Enter number of mines: "))
    game = Minesweeper(size, mines)

    while True:
        game.print_board()
        print(f"Flags: {len(game.flags)}/{game.mines}")
        move = input("Enter move (r x y to reveal / f x y to flag): ").split()
        if len(move) != 3:
            continue
        cmd, x, y = move[0], int(move[1]), int(move[2])

        if cmd == 'r':
            alive = game.reveal(x, y)
            if not alive:
                game.print_board()
                print("💣 Boom! You hit a mine!")
                break
            if game.check_win():
                game.print_board()
                print("🎉 You win! All safe cells revealed!")
                break
        elif cmd == 'f':
            game.toggle_flag(x, y)

if __name__ == "__main__":
    play()
