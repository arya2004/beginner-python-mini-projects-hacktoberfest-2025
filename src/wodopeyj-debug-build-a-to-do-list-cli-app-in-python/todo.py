"""Simple task manager with a clean CLI."""

from asyncio import tasks
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet. Add one!")
        return
    print("\nYour tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task.get("done") else "○"
        print(f"{i}. {status} {task['title']} ({task.get('tag', 'general')})")

def add_task(tasks):
    title = input("Task: ").strip()
    if not title:
        print("Task cannot be empty.")
        return
    tag = input("Tag [general]: ").strip() or "general"
    tasks.append({"title": title, "tag": tag, "done": False})
    save_tasks(tasks)
    print("Task added.")


def pick_task(tasks, prompt):
    if not tasks:
        print("No tasks available.")
        return None
    try:
        index = int(input(prompt)) - 1
    except ValueError:
        print("Invalid number.")
        return None
    if 0 <= index < len(tasks):
        return index
    print("Task number out of range.")
    return None


def mark_done(tasks):
   pass


def delete_task(tasks):
    index = pick_task(tasks, "Task number to delete: ")
    if index is None:
        return
    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f"Removed: {removed['title']}")


def main():
    tasks = load_tasks()
    while True:
        print("\n=== MoonList ===")
        print("1. Add task   2. View tasks")
        print("3. Mark done 4. Delete task")
        print("5. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Choose a valid option.")


if __name__ == "__main__":
    main()
