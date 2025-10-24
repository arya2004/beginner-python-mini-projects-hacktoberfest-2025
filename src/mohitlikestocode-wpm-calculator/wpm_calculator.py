"""Words Per Minute (WPM) calculator - minimal and friendly CLI.

Usage (powershell):
    python wpm_calculator.py

Features:
- interactive CLI
- short/medium/long sample texts or custom text
- calculates gross WPM (chars/5), words/min, accuracy and net WPM

Keep it simple and fast to use.
"""

from time import perf_counter
import textwrap
import sys


SAMPLES = {
    "short": "The quick brown fox jumps over the lazy dog.",
    "medium": (
        "Python is an interpreted, high-level and general-purpose programming language."
    ),
    "long": (
        "Typing quickly is a skill that improves with practice. Short, focused sessions "
        "are better than long, unfocused ones. Concentrate on accuracy first, then "
        "speed will follow."
    ),
}


def measure_typing(sample_text: str) -> dict:
    """Run a single typing test with the given sample_text.

    Returns a dict with elapsed_seconds, gross_wpm_chars, gross_wpm_words,
    correct_words, total_words, accuracy_percent, net_wpm.
    """
    print("\nSample text:\n")
    print(textwrap.fill(sample_text, width=78))
    print("\nWhen you're ready, press Enter to start typing. Type the text and press Enter when done.")
    input("Press Enter to start...")

    start = perf_counter()
    try:
        typed = input()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
        sys.exit(0)
    end = perf_counter()

    elapsed = max(end - start, 0.0001)
    minutes = elapsed / 60.0

    chars = len(typed)
    words = len(typed.split())

    gross_wpm_chars = (chars / 5.0) / minutes if minutes > 0 else 0.0
    gross_wpm_words = words / minutes if minutes > 0 else 0.0

    # Accuracy: compare word-by-word against sample
    sample_words = sample_text.split()
    typed_words = typed.split()
    total = len(sample_words) if len(sample_words) > 0 else 1
    correct = sum(1 for i, w in enumerate(typed_words) if i < len(sample_words) and w == sample_words[i])
    accuracy = (correct / total) * 100.0

    net_wpm = gross_wpm_chars * (accuracy / 100.0)

    return {
        "elapsed_seconds": elapsed,
        "gross_wpm_chars": gross_wpm_chars,
        "gross_wpm_words": gross_wpm_words,
        "correct_words": correct,
        "total_words": total,
        "accuracy_percent": accuracy,
        "net_wpm": net_wpm,
        "typed": typed,
    }


def print_results(res: dict) -> None:
    print("\n--- Results ---")
    print(f"Time: {res['elapsed_seconds']:.2f} seconds")
    print(f"Gross WPM (chars/5): {res['gross_wpm_chars']:.1f}")
    print(f"Gross WPM (words): {res['gross_wpm_words']:.1f}")
    print(f"Accuracy (word-by-word): {res['accuracy_percent']:.1f}% ({res['correct_words']}/{res['total_words']})")
    print(f"Net WPM (approx): {res['net_wpm']:.1f}")
    print("---------------\n")


def choose_sample() -> str:
    print("Choose a sample or type your own:")
    print("1) Short\n2) Medium\n3) Long\n4) Custom text\n5) Exit")
    choice = input("Select 1-5: ").strip()
    if choice == "1":
        return SAMPLES["short"]
    if choice == "2":
        return SAMPLES["medium"]
    if choice == "3":
        return SAMPLES["long"]
    if choice == "4":
        print("Enter your custom text (single line). Keep it short for best results.")
        return input()
    print("Goodbye.")
    sys.exit(0)


def main() -> None:
    print("\nMinimal WPM Calculator — clean, simple, and fast")
    while True:
        sample = choose_sample()
        if not sample.strip():
            print("Empty sample, please try again.")
            continue
        res = measure_typing(sample)
        print_results(res)

        again = input("Try again? [Y/n]: ").strip().lower()
        if again and again[0] == "n":
            print("Thanks for practicing — keep going!")
            break


if __name__ == "__main__":
    main()
