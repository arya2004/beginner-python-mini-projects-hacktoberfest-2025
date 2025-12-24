def binary_to_decimal(binary_str):
    """
    Convert a binary number (string) to decimal.
    """
    decimal = 0
    power = 0

    for digit in reversed(binary_str):
        if digit not in ('0', '1'):
            raise ValueError("Invalid binary number")
        decimal += int(digit) * (2 ** power)
        power += 1

    return decimal


if __name__ == "__main__":
    binary = input("Enter a binary number: ")
    try:
        result = binary_to_decimal(binary)
        print(f"Decimal value: {result}")
    except ValueError as e:
        print(e)
