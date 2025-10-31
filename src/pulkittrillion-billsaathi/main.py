def main():
    print("🪙 Billsaathi: Your Smart Indian Dining Companion")
    print("-" * 50)
    
    try:
        bill = float(input("Enter total bill amount (₹): "))
        has_service_charge = input("Does the bill include Service Charge? (y/n): ").strip().lower() == 'y'
        people = int(input("Number of people splitting the bill: "))

        if bill <= 0 or people <= 0:
            print("❌ Please enter valid positive numbers.")
            return

        # 🔍 Bharat Tip Optimization Logic (BTOL)
        if has_service_charge:
            # Service charge already covers staff → small optional tip
            tip_percent = 5  # "Token of appreciation"
            note = "✅ Service charge included → small tip suggested"
        else:
            # No service charge → fair tip expected
            if bill < 500:
                tip_percent = 10  # Local dhaba / small eatery
            elif 500 <= bill < 2000:
                tip_percent = 12  # Casual restaurant (e.g., Pune cafes)
            else:
                tip_percent = 15  # Fine dining (e.g., Mumbai/Delhi)
            note = "💡 No service charge → fair tip applied"

        tip = bill * (tip_percent / 100)
        total = bill + tip
        per_person = total / people

        print(f"\n{note}")
        print(f"📊 Smart Tip ({tip_percent}%): ₹{tip:.2f}")
        print(f"🧾 Total Payable: ₹{total:.2f}")
        print(f"👥 Per Person: ₹{per_person:.2f}")
        print("\n🙏 Thank you for supporting service staff!")

    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    main()