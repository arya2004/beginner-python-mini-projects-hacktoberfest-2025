import random

def func():
    user = input("Enter the choice: rock, paper, scissors : ").lower()
    op = ["rock", "paper", "scissors"]
    comp = random.choice(op)
    print("The choice of computer is: " + comp)

    if user not in op:
        print("Invalid option")
       

    if user == "rock":
        if user == comp:
            print("It is a tie")
        elif comp == "paper":
            print("Computer wins")
        elif comp == "scissors":
            print("User wins")

    elif user == "paper":
        if user == comp:
            print("It is a tie")
        elif comp == "scissors":
            print("Computer wins")
        elif comp == "rock":
            print("User wins")

    elif user == "scissors":
        if user == comp:
            print("It is a tie")
        elif comp == "rock":
            print("Computer wins")
        elif comp == "paper":
            print("User wins")

func()
