import random
runs = [0,1,2,4,6]
tot =0
balls = int(input("Enter number of balls: "))
if balls % 6 != 0:
   print("Balls should be multiple of 6")
   exit()
score_board = []
out = balls // 3
for ball in range(balls):
   if out == 0:
       print("All out")
       break
   else:
       batsman = int(input(f"Enter runs scored on ball {ball+1}: "))
       if batsman not in runs:
           print("Invalid runs. Please enter runs from the following options:")
           print(runs)
           exit()
       else:
           baller_i = random.randint(0,4)
           baller = runs[baller_i]
           if batsman == baller and batsman != 0:
               if out != 0:
                   score_board.append("|   X   |   W   |")
                   out-=1
               else:
                   break
           else:
               tot += batsman
               score_board.append(f"|   {tot}   |   -   |")

for score in score_board:
   print(score)
