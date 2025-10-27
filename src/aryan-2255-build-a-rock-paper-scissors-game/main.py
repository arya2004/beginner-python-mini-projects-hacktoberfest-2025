import random

while True:
    user_move = input("Enter Rock, Paper, Scissors or Quit: ")
    if user_move == "quit":
        break

    number = random.randint(0, 2)

    if number == 0:
        print("Rock")
        if user_move == "Rock":
            print("Draw!")
        elif user_move == "Scissors":
            print("Computer wins!")
        else:
            print("User wins!")

    elif number == 1:
        print("Scissors")
        if user_move == "Rock":
            print("User wins!")
        elif user_move == "Scissors":
            print("Draw!")
        else:
            print("Computer wins!")

    else:
        print("Paper")
        if user_move == "Rock":
            print("Computer wins!")
        elif user_move == "Scissors":
            print("User wins!")
        else:
            print("Draw!")
          