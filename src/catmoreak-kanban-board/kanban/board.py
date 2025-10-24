import json
import uuid
from pathlib import Path
from datetime import datetime

COLUMNS = ["Todo", "In Progress", "Done"]

class Card:
    def __init__(self, title, description="", tags=None, priority="medium", column="Todo"):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.tags = tags or []
        self.priority = priority
        self.column = column
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        card = Card(data['title'], data.get('description', ''), data.get('tags', []), data.get('priority', 'medium'), data.get('column', 'Todo'))
        card.id = data['id']
        card.created_at = data.get('created_at', datetime.now().isoformat())
        card.updated_at = data.get('updated_at', card.created_at)
        return card

class Board:
    def __init__(self, name):
        self.name = name
        self.columns = COLUMNS.copy()
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def move_card(self, card_id, new_column):
        for card in self.cards:
            if card.id == card_id:
                card.column = new_column
                card.updated_at = datetime.now().isoformat()
                return True
        return False

    def to_dict(self):
        return {
            'name': self.name,
            'columns': self.columns,
            'cards': [c.to_dict() for c in self.cards]
        }

    @staticmethod
    def from_dict(data):
        board = Board(data['name'])
        board.columns = data.get('columns', COLUMNS.copy())
        board.cards = [Card.from_dict(c) for c in data.get('cards', [])]
        return board

    def save(self, path):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, indent=2)

    @staticmethod
    def load(path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return Board.from_dict(data)
