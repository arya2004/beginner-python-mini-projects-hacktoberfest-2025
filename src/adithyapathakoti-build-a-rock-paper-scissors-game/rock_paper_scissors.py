import random

def get_user_choice():
    while True:
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        choice = input("Enter 1/2/3: ")

        if choice == "1":
            return "Rock"
        elif choice == "2":
            return "Paper"
        elif choice == "3":
            return "Scissors"
        else:
            print("❌ Invalid choice! Please try again.")
            
def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a Tie! 🤝"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        return "🎉 You Win!"
    else:
        return "💻 Computer Wins!"

def play_game():
    print("=== Rock Paper Scissors Game ===")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\n👉 You chose: {user_choice}")
    print(f"🤖 Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(f"\n🏆 Result: {result}")

if __name__ == "__main__":
    while True:
        play_game()
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != "y":
            print("👋 Thanks for playing! Goodbye.")
            break
