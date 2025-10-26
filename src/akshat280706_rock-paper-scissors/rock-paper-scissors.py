#rock paper scissors game implementation
import sys
import random
print("")
player_choice=input("enter...\n1. For Rock\n2. For paper\n3. For Scissors:\n\n")

player=int(player_choice)

if player<1 | player>3:
    sys.exit("Invalid input, Choose Between 1,2,3")

computer_choice= random.choice("123")
computer= int(computer_choice)

print("")

print("you chose:" + player_choice + ".")
print("computer chose:" + computer_choice+ ".")

if player==1 and computer==3:
    print("🎊congratulations, you won")
elif player==2 and computer==1:
    print("🎊congratulations, you won ")
elif player==3 and computer==2:
    print("🎊congratulations, you won")
elif player==computer:
    print("Tie game")
else:
    print("😞computer wins")