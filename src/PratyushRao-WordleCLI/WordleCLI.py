import random
import os
from colorama import Fore, Style, init

init(autoreset=True)

# Load words from local file
def load_words(filename="assets/words.txt"):
    with open(filename, "r") as f:
        words = [w.strip().lower() for w in f if len(w.strip()) == 5 and w.strip().isalpha()]
    return words

def choose_word(words):
    return random.choice(words)

def check_guess(guess, secret):
    """Returns a color-coded string (Green, Yellow, Gray) for a guess."""
    result = []
    secret_letters = list(secret)
    guess_letters = list(guess)

    for i in range(5):
        if guess_letters[i] == secret_letters[i]:
            result.append(Fore.GREEN + guess_letters[i].upper() + Style.RESET_ALL)
            secret_letters[i] = None  
        else:
            result.append(None)

    for i in range(5):
        if result[i] is None:
            if guess_letters[i] in secret_letters:
                result[i] = Fore.YELLOW + guess_letters[i].upper() + Style.RESET_ALL
                secret_letters[secret_letters.index(guess_letters[i])] = None
            else:
                result[i] = Fore.LIGHTBLACK_EX + guess_letters[i].upper() + Style.RESET_ALL

    return " ".join(result)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_wordle():
    words = load_words()
    if not words:
        print("❌ No valid 5-letter words found in words.txt!")
        return

    secret = choose_word(words)
    attempts = 6
    guesses = []

    print("\n🎯 Welcome to Wordle CLI!")
    print("Guess the 5-letter word. You have 6 tries.\n")

    for attempt in range(1, attempts + 1):
        while True:
            guess = input(f"Attempt {attempt}/{attempts}: ").strip().lower()
            if len(guess) != 5 or not guess.isalpha():
                print("⚠️ Enter a valid 5-letter word!\n")
                continue
            if guess not in words:
                print("❌ Not in word list!\n")
                continue
            break

        colored = check_guess(guess, secret)
        guesses.append(colored)

        clear_screen()
        print("🎯 Wordle CLI\n")
        for g in guesses:
            print(g)
        print("\n")

        if guess == secret:
            print(f"🏆 Correct! You guessed it in {attempt} tries.\n")
            break
    else:
        print(f"😢 Out of tries! The word was: {secret.upper()}\n")

if __name__ == "__main__":
    play_wordle()
