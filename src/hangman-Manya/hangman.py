import random

# List of possible words
word_list = [
    "python", "hangman", "developer", "artificial", "intelligence",
    "keyboard", "monitor", "laptop", "programming", "algorithm"
]

# Hangman stages (visuals)
stages = [
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / \\
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / 
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |      
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|
       |      |
       |      
       -
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      |
       |      
       -
    """,
    """
       --------
       |      |
       |      O
       |    
       |      
       |      
       -
    """,
    """
       --------
       |      |
       |      
       |    
       |      
       |      
       -
    """
]

def hangman():
    word = random.choice(word_list)
    word_letters = set(word)
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = len(stages) - 1

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while wrong_guesses < max_attempts and word_letters:
        print(stages[wrong_guesses])
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        print("Word:", " ".join([letter if letter in guessed_letters else "_" for letter in word]))

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print("✅ Good guess!")
        else:
            wrong_guesses += 1
            print("❌ Wrong guess!")

    # Game over
    print(stages[wrong_guesses])
    if not word_letters:
        print(f"🎉 Congratulations! You guessed the word: {word}")
    else:
        print(f"💀 You lost! The word was: {word}")

if __name__ == "__main__":
    hangman()
    