import random

# Word list
words = ["python", "programming", "developer", "hangman", "computer", "keyboard", "algorithm"]

# Choose a random word
word = random.choice(words)
word_letters = set(word)  # Unique letters in the word
guessed_letters = set()    # Letters guessed by the player
tries = 6                  # Number of allowed wrong guesses

print("=== Welcome to Hangman ===")
print(f"The word has {len(word)} letters.")

# Game loop
while tries > 0 and word_letters != guessed_letters:
    # Display current progress
    display = [letter if letter in guessed_letters else "_" for letter in word]
    print("Word: ", " ".join(display))
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print(f"Remaining tries: {tries}")
    
    # Player input
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.\n")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue
    
    guessed_letters.add(guess)
    
    if guess in word_letters:
        print(f"Good job! '{guess}' is in the word.\n")
    else:
        print(f"Sorry! '{guess}' is not in the word.\n")
        tries -= 1

# End game
if word_letters == guessed_letters:
    print(f"Congratulations! You guessed the word: {word}")
else:
    print(f"Game over! The word was: {word}")
