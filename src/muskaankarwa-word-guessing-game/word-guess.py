import random
def word_guess_game():
    print("Welcome to the Word Guessing Game!")
    print("Try to guess the secret word, one letter at a time.")
    print("You have limited attempts, so choose carefully.\n")

    words = ["python", "developer", "program", "computer", "keyboard", "science", "machine", "project", "internet", "variable"]

    word = random.choice(words)
    guessed_letters = []
    attempts = 7
    word_display = ["_"] * len(word)

    while attempts > 0:
        print("Word:", " ".join(word_display))
        print(f"Attempts left: {attempts}")
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!\n")
            for i in range(len(word)):
                if word[i] == guess:
                    word_display[i] = guess
        else:
            print("Incorrect guess.\n")
            attempts -= 1

        if "_" not in word_display:
            print("Congratulations! You guessed the word:", word)
            break

    if "_" in word_display:
        print(f"Out of attempts! The correct word was: {word}")

    print("Game Over.")

if __name__ == "__main__":
    word_guess_game()
