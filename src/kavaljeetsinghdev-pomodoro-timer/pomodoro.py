import time
import os

# Pomodoro Timer Settings (in minutes)
WORK_DURATION = 25
SHORT_BREAK = 5
LONG_BREAK = 15
SESSIONS_BEFORE_LONG_BREAK = 4

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown(minutes):
    total_seconds = minutes * 60
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"\r⏳ Time left: {timer}", end="")
        time.sleep(1)
        total_seconds -= 1
    print("\r✅ Time's up!            ")

def pomodoro_cycle():
    session = 0
    while True:
        session += 1
        clear_screen()
        print(f"🍅 Pomodoro Session {session} Started! Focus for {WORK_DURATION} minutes.")
        countdown(WORK_DURATION)

        if session % SESSIONS_BEFORE_LONG_BREAK == 0:
            print(f"\n💤 Take a long break for {LONG_BREAK} minutes.")
            countdown(LONG_BREAK)
        else:
            print(f"\n☕ Take a short break for {SHORT_BREAK} minutes.")
            countdown(SHORT_BREAK)

        user_choice = input("\nPress Enter to start the next session or type 'q' to quit: ").lower()
        if user_choice == 'q':
            print("👋 Good job! Stay consistent and come back later.")
            break

if __name__ == "__main__":
    clear_screen()
    print("🔥 Welcome to Pomodoro Timer 🔥")
    print("Work smart, take breaks, and stay focused!")
    input("\nPress Enter to start your first Pomodoro session...")
    pomodoro_cycle()
