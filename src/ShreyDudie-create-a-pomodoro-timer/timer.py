import time

def pomodoro(minutes=25):
    print(f"Pomodoro started: {minutes} minutes.")
    for remaining in range(minutes*60, 0, -1):
        mins, secs = divmod(remaining, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
    print("⏰ Time's up! Take a short break.")

if __name__ == "__main__":
    pomodoro()
