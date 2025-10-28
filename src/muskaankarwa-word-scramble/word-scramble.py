import random
import time

def word_scramble():
    words = ["python", "keyboard", "adventure", "challenge", "programming", "island", "treasure", "developer", "coffee", "music"]
    score = 0

    print("🔠 Welcome to the Word Scramble Game!")
    print("Unscramble the letters to form a valid word. Type 'quit' to exit.")
    time.sleep(1)

    while True:
        word = random.choice(words)
        scrambled = ''.join(random.sample(word, len(word)))

        print("\nScrambled word:", scrambled)
        guess = input("Your guess: ").lower()

        if guess == "quit":
            print("👋 Thanks for playing!")
            break

        if guess == word:
            score += 10
            print("✅ Correct! You earned 10 points.")
        else:
            print(f"❌ Wrong! The correct word was '{word}'.")
            score -= 5

        print(f"Current Score: {score}")
        time.sleep(1)

    print(f"\n🏁 Final Score: {score}")
    if score > 30:
        print("🔥 You're a word master!")
    elif score > 10:
        print("💪 Nice job!")
    else:
        print("😅 Better luck next time!")

word_scramble()
