import time, math, sys

def timer():
  given_time = input("How many minute(s) countdown do you want? ") # get minnute value from user
  response = "" # init response

  if type(given_time) is int and 1 <= int(given_time) <= 60: # validate input
    given_time_in_sec = int(given_time) * 60 # turn minute value to seconds

    while given_time_in_sec > 0:
      minute = math.floor(given_time_in_sec / 60) if len(str(math.floor(given_time_in_sec / 60))) > 1 else "0" + str(math.floor(given_time_in_sec / 60)) # calc mins left
      second = math.floor(given_time_in_sec % 60) if len(str(math.floor(given_time_in_sec % 60))) > 1 else "0" + str(math.floor(given_time_in_sec % 60)) # calc seeconds left
      print(f"{minute}:{second}") # display current time left to user
      time.sleep(1) # pause program for a sec
      sys.stdout.write("\033[F") # take cursor to beginning of line above
      sys.stdout.write("\033[K") # clear line where cursor is
      sys.stdout.flush() # print again on same line
      given_time_in_sec -= 1 # deduct 1 sec from total time
      response = "Time up!" # update response
  else:
    response  = "Please eter a valid integer representinng minute value between 1 and 60 (both inclusive)" # update response in case of wrong value

  return response # display responnse

print(timer())