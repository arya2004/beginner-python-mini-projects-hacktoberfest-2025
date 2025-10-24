import argparse
from pathlib import Path
from .board import Board, Card

BOARDS_DIR = Path(__file__).parent.parent / "boards"
BOARDS_DIR.mkdir(exist_ok=True)

def board_path(name):
    return BOARDS_DIR / f"{name}.json"

def main():
    parser = argparse.ArgumentParser(description="Terminal Kanban Board")
    subparsers = parser.add_subparsers(dest="command")

    sp_new = subparsers.add_parser("new")
    sp_new.add_argument("name")

    sp_add = subparsers.add_parser("add")
    sp_add.add_argument("--board", required=True)
    sp_add.add_argument("title")
    sp_add.add_argument("--desc", default="")
    sp_add.add_argument("--tags", default="")
    sp_add.add_argument("--priority", default="medium")

    sp_list = subparsers.add_parser("list")
    sp_list.add_argument("--board", required=True)

    sp_move = subparsers.add_parser("move")
    sp_move.add_argument("--board", required=True)
    sp_move.add_argument("card_id")
    sp_move.add_argument("column")

    args = parser.parse_args()

    if args.command == "new":
        board = Board(args.name)
        board.save(board_path(args.name))
        print(f"Board '{args.name}' created.")
    elif args.command == "add":
        path = board_path(args.board)
        board = Board.load(path)
        tags = [t.strip() for t in args.tags.split(",") if t.strip()]
        card = Card(args.title, args.desc, tags, args.priority)
        board.add_card(card)
        board.save(path)
        print(f"Added card '{args.title}' to board '{args.board}'.")
    elif args.command == "list":
        path = board_path(args.board)
        board = Board.load(path)
        for col in board.columns:
            print(f"\n=== {col} ===")
            for card in board.cards:
                if card.column == col:
                    print(f"[{card.id[:8]}] {card.title} ({card.priority}) Tags: {', '.join(card.tags)}")
    elif args.command == "move":
        path = board_path(args.board)
        board = Board.load(path)
        if board.move_card(args.card_id, args.column):
            board.save(path)
            print(f"Moved card {args.card_id} to {args.column}.")
        else:
            print(f"Card {args.card_id} not found.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
