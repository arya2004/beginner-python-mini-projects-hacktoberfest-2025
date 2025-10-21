from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time

class TicTacToe:
	def __init__(self):
		self.board = [' ' for _ in range(9)]
		self.current_winner = None

	def print_board(self):
		for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
			print('| ' + ' | '.join(row) + ' |')

	@staticmethod
	def print_board_nums():
		for row in [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]:
			print('| ' + ' | '.join(row) + ' |')

	def available_moves(self):
		return [i for i, spot in enumerate(self.board) if spot == ' ']

	def empty_squares(self):
		return ' ' in self.board

	def num_empty_squares(self):
		return self.board.count(' ')

	def make_move(self, square, letter):
		if self.board[square] == ' ':
			self.board[square] = letter
			if self.check_winner(square, letter):
				self.current_winner = letter
			return True
		return False

	def check_winner(self, square, letter):
		row_idx = square // 3
		row = self.board[row_idx*3:(row_idx+1)*3]
		if all(spot == letter for spot in row):
			return True

		col_idx = square % 3
		col = self.board[col_idx:9:3]
		if all(spot == letter for spot in col):
			return True

		if square % 2 == 0:
			diag1 = [self.board[i] for i in [0, 4, 8]]
			if all(spot == letter for spot in diag1):
				return True
			diag2 = [self.board[i] for i in [2, 4, 6]]
			if all(spot == letter for spot in diag2):
				return True

		return False

def play(game, x_player, o_player, print_game=True):
	if print_game:
		TicTacToe.print_board_nums()

	letter = 'X'
	while game.empty_squares():
		player = x_player if letter == 'X' else o_player
		square = player.get_next_move(game)

		if game.make_move(square, letter):
			if print_game:
				print(f"{letter} makes a move to square {square}")
				game.print_board()
				print()

			if game.current_winner:
				if print_game:
					print(f"{game.current_winner} wins!")
				return game.current_winner

			letter = 'O' if letter == 'X' else 'X'
			if print_game and game.num_empty_squares():
				print(f"{letter} is thinking a move")
				time.sleep(1)
		else:
			if print_game:
				print("Invalid move. Try again.")

	if print_game:
		print("It's a tie!")

if __name__ == '__main__':
	x_player = HumanPlayer('X')
	o_player = GeniusComputerPlayer('O') # You can change this to RandomComputerPlayer or HumanPlayer
	t = TicTacToe()
	play(t, x_player, o_player)
