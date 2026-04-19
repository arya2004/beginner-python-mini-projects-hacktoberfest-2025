def binary_to_decimal(binary_str):
    """Convert a binary string to decimal number."""
    try:
        # Validate that input contains only 0s and 1s
        for char in binary_str:
            if char not in ('0', '1'):
                return None, "Invalid binary number! Only 0s and 1s are allowed."
        
        decimal = int(binary_str, 2)
        return decimal, None
    except ValueError:
        return None, "Invalid input! Please enter a valid binary number."


def decimal_to_binary(decimal_num):
    """Convert a decimal number to binary string."""
    try:
        num = int(decimal_num)
        if num < 0:
            return None, "Please enter a positive number."
        return bin(num)[2:], None
    except ValueError:
        return None, "Invalid input! Please enter a valid decimal number."


def main():
    print("=" * 40)
    print("   Binary ↔ Decimal Converter")
    print("=" * 40)

    while True:
        print("\nOptions:")
        print("  1. Binary  → Decimal")
        print("  2. Decimal → Binary")
        print("  3. Exit")

        choice = input("\nEnter your choice (1/2/3): ").strip()

        if choice == '1':
            binary_input = input("Enter binary number: ").strip()
            result, error = binary_to_decimal(binary_input)
            if error:
                print(f"❌ Error: {error}")
            else:
                print(f"✅ {binary_input} in decimal is: {result}")

        elif choice == '2':
            decimal_input = input("Enter decimal number: ").strip()
            result, error = decimal_to_binary(decimal_input)
            if error:
                print(f"❌ Error: {error}")
            else:
                print(f"✅ {decimal_input} in binary is: {result}")

        elif choice == '3':
            print("\nGoodbye! 👋")
            break

        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()