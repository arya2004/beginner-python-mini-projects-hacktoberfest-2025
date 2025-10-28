import json
import os
from datetime import datetime

DATA_FILE = "tracker_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_task():
    date = str(datetime.now().date())
    task = input("Enter your task: ")
    data = load_data()
    data.setdefault(date, []).append(task)
    save_data(data)
    print(f"✅ Task added for {date}!")

def view_tasks():
    data = load_data()
    if not data:
        print("No tasks found.")
        return
    for date, tasks in data.items():
        print(f"\n📅 {date}:")
        for i, task in enumerate(tasks, 1):
            print(f"  {i}. {task}")

def clear_tasks():
    os.remove(DATA_FILE) if os.path.exists(DATA_FILE) else None
    print("🧹 All tasks cleared!")

def main():
    while True:
        print("\n--- Daily Tracker CLI ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Clear All Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            clear_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
