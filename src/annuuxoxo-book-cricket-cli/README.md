# 🏏 Book Cricket CLI

This Python program simulates a simple cricket batting session where a user inputs runs for each ball, and the program randomly decides if a wicket falls based on a basic logic system. It’s an interactive and fun way to understand loops, conditionals, and randomization in Python!

---

## 🎯 Features

- Simulates batting for a user-defined number of balls.  
- Accepts only valid runs: `0, 1, 2, 4, 6`.  
- Randomly decides if the batsman is **out** based on a "bowler’s random number".  
- Displays a score board after every ball.  
- Ends the innings automatically when all wickets fall.

---

## 🧮 How It Works

1. The user inputs the **total number of balls** (must be a multiple of 6).  
2. For each ball:
   - The user enters the runs scored.  
   - A random number (bowler’s outcome) is generated.  
   - If both match and are non-zero → **Wicket falls!**  
   - Otherwise, runs are added to the total score.  
3. Once all wickets fall, the game stops automatically.

---

## 🧑‍💻 Example Run

Enter number of balls: 12
Enter runs scored on ball 1: 2
Enter runs scored on ball 2: 6
Enter runs scored on ball 3: 4
Enter runs scored on ball 4: 1
Enter runs scored on ball 5: 2
Enter runs scored on ball 6: 0
...
| 2 | - |
| 8 | - |
| X | W |
| 9 | - |
...

---

## ⚙️ Requirements

- Python 3.x  
- `random` (standard library)

---

## 🚀 Run the Program

1. Save the script as `book_cricket.py`.  
2. Open a terminal or command prompt.  
3. Run the following command:

```bash
python book_cricket.py
```

## Notes
- The number of balls must be a multiple of 6 (to simulate overs).
- Wickets fall when the batsman’s run equals the bowler’s random number (excluding zero).
- The total number of wickets is limited to balls // 3.

---

## 💡 Future Enhancements
1. Add multiple overs and players.
2. Track player names and individual scores.
3. Include random commentary for fun.
4. Display final score and strike rate summary.

---
Author : annuuxoxo
Language: Python 🐍
License: MIT

