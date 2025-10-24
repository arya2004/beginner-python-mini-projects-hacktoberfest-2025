import unittest
from kanban.board import Board, Card
import tempfile
import os

class TestBoard(unittest.TestCase):
    def test_add_and_move_card(self):
        board = Board("test")
        card = Card("Test Card", "desc", ["tag1"], "high")
        board.add_card(card)
        self.assertEqual(len(board.cards), 1)
        self.assertEqual(board.cards[0].column, "Todo")
        board.move_card(card.id, "In Progress")
        self.assertEqual(board.cards[0].column, "In Progress")

    def test_save_and_load(self):
        board = Board("test")
        card = Card("Test Card")
        board.add_card(card)
        with tempfile.NamedTemporaryFile(delete=False) as tf:
            board.save(tf.name)
            loaded = Board.load(tf.name)
            self.assertEqual(loaded.name, "test")
            self.assertEqual(len(loaded.cards), 1)
        os.remove(tf.name)

if __name__ == "__main__":
    unittest.main()
