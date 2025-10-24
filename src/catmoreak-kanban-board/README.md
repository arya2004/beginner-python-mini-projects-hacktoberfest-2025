# Terminal Kanban Board

A lightweight, dependency-free Kanban board for managing tasks in your terminal. Create boards, add cards, move cards between columns (Todo, In Progress, Done), and persist boards to disk. Perfect for Hacktoberfest and beginner Python contributors.

## Features
- Create/open boards
- Add, list, move, edit, and delete cards
- Save/load boards as JSON
- Simple CLI interface

## Usage
```bash
python -m kanban.cli new myboard
python -m kanban.cli add --board myboard "Write README" --desc "Create the project README" --tags "docs,good-first-issue" --priority high
python -m kanban.cli list --board myboard
python -m kanban.cli move --board myboard 1 "In Progress"
```

## Project Structure
- kanban/board.py — Board and Card models
- kanban/cli.py — CLI entry point
- tests/ — unit tests

## Contributing
See CONTRIBUTING.md for good first issues and contribution guidelines.
