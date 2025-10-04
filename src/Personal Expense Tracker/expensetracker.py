import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

def load_expenses():
    expenses = []
    if os.path.exists(FILENAME):
        with open(FILENAME, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                expenses.append(row)
    return expenses

def save_expenses(expenses):
    with open(FILENAME, 'w', newline='') as csvfile:
        fieldnames = ['date', 'amount', 'category', 'note']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for exp in expenses:
            writer.writerow(exp)

def add_expense(expenses):
    date = input("Date (YYYY-MM-DD) [leave blank for today]: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    amount = input("Amount: ")
    category = input("Category (e.g., food, transport, bills): ")
    note = input("Note (optional): ")

    expenses.append({
        'date': date,
        'amount': amount,
        'category': category,
        'note': note
    })
    print("✅ Expense added!")

def view_expenses(expenses):
    print("\n🧾 All Expenses:")
    for exp in expenses:
        print(f"{exp['date']} - ${exp['amount']} - {exp['category']} - {exp['note']}")
    print()

def view_summary(expenses):
    total = sum(float(exp['amount']) for exp in expenses)
    print(f"\n💰 Total Spent: ${total:.2f}")

    category_totals = {}
    for exp in expenses:
        cat = exp['category']
        category_totals[cat] = category_totals.get(cat, 0) + float(exp['amount'])

    print("📊 Spending by Category:")
    for cat, amt in category_totals.items():
        print(f"  {cat}: ${amt:.2f}")
    print()

def main():
    expenses = load_expenses()

    while True:
        print("=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            view_summary(expenses)
        elif choice == '4':
            save_expenses(expenses)
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
