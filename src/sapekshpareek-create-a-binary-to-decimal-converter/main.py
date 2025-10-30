#!/usr/bin/env python3
"""
Binary to Decimal Converter

Beginner-friendly CLI tool to convert binary strings to decimal numbers.
Supports integer and fractional binaries and optional detailed conversion steps.
"""
import argparse
import sys


def validate_binary(s: str) -> None:
    """Validate a binary string. Raises ValueError on invalid input."""
    if not isinstance(s, str) or not s:
        raise ValueError("Input must be a non-empty string.")
    if s.startswith("-"):
        s2 = s[1:]
    else:
        s2 = s
    if s2.count(".") > 1:
        raise ValueError("Invalid binary: more than one decimal point.")
    allowed = set("01.")
    if any(ch not in allowed for ch in s2):
        raise ValueError("Invalid character in binary input. Only 0, 1 and optional '.' are allowed.")


def binary_to_decimal(s: str) -> float:
    """Convert binary string to decimal number.

    Examples:
      '101' -> 5
      '10.11' -> 2.75
      '-101' -> -5
    """
    validate_binary(s)
    sign = -1 if s.startswith("-") else 1
    if s.startswith("-"):
        s = s[1:]
    if "." in s:
        int_part, frac_part = s.split(".")
    else:
        int_part, frac_part = s, ""

    dec_int = 0
    if int_part:
        for ch in int_part:
            dec_int = dec_int * 2 + int(ch)

    dec_frac = 0.0
    if frac_part:
        for i, ch in enumerate(frac_part, start=1):
            dec_frac += int(ch) * (2 ** -i)

    return sign * (dec_int + dec_frac)


def conversion_steps(s: str) -> str:
    """Return a multi-line string showing step-by-step conversion from binary to decimal."""
    validate_binary(s)
    sign = "-" if s.startswith("-") else ""
    if s.startswith("-"):
        s = s[1:]
    if "." in s:
        int_part, frac_part = s.split(".")
    else:
        int_part, frac_part = s, ""

    lines = []
    lines.append(f"Input (binary): {sign}{s}")

    if int_part:
        lines.append("\nInteger part conversion:")
        total_int = 0
        power = len(int_part) - 1
        for ch in int_part:
            val = int(ch) * (2 ** power)
            lines.append(f"  {ch} * 2^{power} = {val}")
            total_int += val
            power -= 1
        lines.append(f"  Sum (integer) = {total_int}")
    else:
        total_int = 0
        lines.append("\nInteger part conversion: (empty, treated as 0)")

    if frac_part:
        lines.append("\nFractional part conversion:")
        total_frac = 0.0
        for i, ch in enumerate(frac_part, start=1):
            val = int(ch) * (2 ** -i)
            lines.append(f"  {ch} * 2^-{i} = {val}")
            total_frac += val
        lines.append(f"  Sum (fractional) = {total_frac}")
    else:
        total_frac = 0.0
        lines.append("\nFractional part conversion: (none)")

    lines.append("\nFinal result:")
    lines.append(f"  {total_int} + {total_frac} = {total_int + total_frac}")
    if sign == "-":
        lines.append(f"  Apply sign -> -{total_int + total_frac}")

    return "\n".join(lines)


def _parse_args():
    parser = argparse.ArgumentParser(description="Binary to Decimal Converter")
    parser.add_argument("--bin", "-b", dest="binary", help="Binary string to convert (e.g. 101, 10.11, -101)")
    parser.add_argument("--steps", action="store_true", help="Show detailed conversion steps")
    return parser.parse_args()


def main():
    args = _parse_args()
    if args.binary:
        user_input = args.binary.strip()
    else:
        try:
            user_input = input("Enter a binary number (e.g. 101 or 10.11): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("No input provided. Exiting.")
            sys.exit(1)

    try:
        result = binary_to_decimal(user_input)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    if isinstance(result, float) and result.is_integer():
        result_out = int(result)
    else:
        result_out = round(result, 10)

    print(f"Binary: {user_input}")
    print(f"Decimal: {result_out}")

    if args.steps:
        print("\n" + conversion_steps(user_input))


if __name__ == "__main__":
    main()
