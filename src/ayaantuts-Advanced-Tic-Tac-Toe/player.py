import math
import random

class Player:
	def __init__(self, letter):
		self.letter = letter

	def get_next_move(self, game):
		raise NotImplementedError("This method should be implemented by subclasses.")

class RandomComputerPlayer(Player):
	def get_next_move(self, game):
		return random.choice(game.available_moves())

class HumanPlayer(Player):
	def get_next_move(self, game):
		while True:
			square = input(f"{self.letter}'s turn. Input move (0-8): ")
			try:
				val = int(square)
				if val not in game.available_moves():
					raise ValueError
				return val
			except ValueError:
				print("Invalid square. Try again!")

class GeniusComputerPlayer(Player):
	def get_next_move(self, game):
		# If it is the beginning of the game, no need to execute minimax
		if len(game.available_moves()) == 9:
			return random.choice(game.available_moves())
		return self.minimax(game, self.letter)['position']

	def minimax(self, state, player):
		# The current player will aim to maximize it's score
		max_player = self.letter
		# By minimising the other player's score
		other_player = 'O' if player == 'X' else 'X'

		# If there other player is the winner in any state, it's either the worst case or best case
		if state.current_winner == other_player:
			return {
				'position': None,
				'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)
			}
		# Or if the board does not have any empty squares, it is a neutral choice
		elif not state.empty_squares():
			return {'position': None, 'score': 0}

		# Initialise best move with suitable values
		if player == max_player:
			best = {'position': None, 'score': -math.inf}
		else:
			best = {'position': None, 'score': math.inf}

		# Loop through each move and solve the board until someone wins or no empty squares
		for move in state.available_moves():
			state.make_move(move, player)
			sim_score = self.minimax(state, other_player)
			state.board[move] = ' '
			state.current_winner = None
			sim_score['position'] = move

			if player == max_player:
				if sim_score['score'] > best['score']:
					best = sim_score
			else:
				if sim_score['score'] < best['score']:
					best = sim_score
		# Return the best possible move
		return best
