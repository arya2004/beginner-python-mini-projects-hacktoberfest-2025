#!/usr/bin/env python3
"""
🎯 Guess the Number Game
A simple Python command-line game for fun.
Author: YourName
License: MIT
"""

import random

def play_game():
    print("🎮 Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100...")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("👉 Enter your guess: "))
            attempts += 1
            if guess < number:
                print("📉 Too low! Try again.")
            elif guess > number:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Correct! The number was {number}.")
                print(f"You guessed it in {attempts} attempts! 🏆")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    play_game()
