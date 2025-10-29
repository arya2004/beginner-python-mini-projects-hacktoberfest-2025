# Tic Tac Toe Game
# Beginner-friendly version

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    winner = None

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while not is_board_full(board) and winner is None:
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))
            if board[row][col] == " ":
                board[row][col] = current_player
                print_board(board)
                if check_winner(board, current_player):
                    winner = current_player
                    print(f"Player {winner} wins!")
                else:
                    current_player = "O" if current_player == "X" else "X"
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")

    if winner is None:
        print("It's a tie!")

if __name__ == "__main__":
    main()
