import time

work = int(input("Enter the minutes you want to work"))*60
long_break = int(input("Enter the time you want to take for long break"))*60
short = int(input("Enter the time you want to take for short break"))*60

def pomodoro(total_secs,label):
  while total_secs>0:
    mins = total_secs//60
    secs = total_secs%60
    print(f"{label}-{mins:02d}:{secs:02d}",end="\r")
    time.sleep(1)
    total_secs-=1
   

print("Press enter or run to start pomodoro")

for i in range(1,5):
   print("Time to focus")
   pomodoro(work,"WORK")

   if i<4:
     print("Time to take short break")
     pomodoro(short,"SHORT BREAK")

   else:
     print("Time to take a long break")
     pomodoro(long,"LONG BREAK")


print("Your all sessions are complete congrats")


    
           
