import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses):
    print("\n--- Add Expense ---")
    try:
        amount = float(input("Enter amount: $"))
        category = input("Enter category (e.g. Food, Transport, Bills): ").strip()
        description = input("Enter description: ").strip()
        date = datetime.now().strftime("%Y-%m-%d %H:%M")

        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }
        expenses.append(expense)
        save_expenses(expenses)
        print(f"✅ Expense of ${amount:.2f} added successfully!")
    except ValueError:
        print("❌ Invalid amount! Please enter a number.")

def view_expenses(expenses):
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses found.")
        return
    total = 0
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. [{exp['date']}] {exp['category']} - ${exp['amount']:.2f} ({exp['description']})")
        total += exp['amount']
    print(f"\n💰 Total Spent: ${total:.2f}")

def view_by_category(expenses):
    print("\n--- Expenses by Category ---")
    if not expenses:
        print("No expenses found.")
        return
    categories = {}
    for exp in expenses:
        cat = exp['category']
        categories[cat] = categories.get(cat, 0) + exp['amount']
    for cat, total in categories.items():
        print(f"  {cat}: ${total:.2f}")

def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    try:
        index = int(input("\nEnter expense number to delete: ")) - 1
        if 0 <= index < len(expenses):
            removed = expenses.pop(index)
            save_expenses(expenses)
            print(f"✅ Deleted: {removed['description']}")
        else:
            print("❌ Invalid number!")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    expenses = load_expenses()
    print("=" * 40)
    print("       💸 Expense Tracker CLI")
    print("=" * 40)

    while True:
        print("\nOptions:")
        print("  1. Add Expense")
        print("  2. View All Expenses")
        print("  3. View by Category")
        print("  4. Delete Expense")
        print("  5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            view_by_category(expenses)
        elif choice == '4':
            delete_expense(expenses)
        elif choice == '5':
            print("\nGoodbye! 👋")
            break
        else:
            print("❌ Invalid choice! Please enter 1-5.")

if __name__ == "__main__":
    main()