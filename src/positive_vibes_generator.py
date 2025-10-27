# positive_vibes_generator.py
# Hacktoberfest 2025 - Beginner friendly mini project by Minal

import random
import datetime

quotes = [
    "Keep shining, you are doing great! ✨",
    "Believe in yourself — you are stronger than you think 💪",
    "One positive thought can change your whole day 🌈",
    "Keep going, success is closer than you imagine 🚀",
    "You are enough, just the way you are 🌸",
    "Every sunrise is another chance to make your dreams real 🌞"
]

today = datetime.datetime.now().strftime("%A, %d %B %Y")
print(f"\n 🌸 Positive Vibes Generator 🌸 ")
print(f"🌼 Today's Date: {today}")
print(f"✨ Your Quote for Today: {random.choice(quotes)}\n")
