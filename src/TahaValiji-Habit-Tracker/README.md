# 🧭 Habit Tracker (Python + Excel)

A simple **Habit Tracker** built with **Python** and **Pandas** that helps you monitor your daily habits month by month using an Excel sheet.

---

## 🧠 Features

- ✅ Add or mark daily habits  
- 📊 Automatically generates monthly reports  
- 🔄 Auto-creates an Excel file (`HabitTracker.xlsx`) if it doesn’t exist  
- 🕒 Tracks last run time via a timestamp file (`last_run.txt`)  
- 🧹 Option to reset the current month’s data  

---

## 📁 Files Created

| File Name | Description |
|------------|--------------|
| `HabitTracker.xlsx` | Stores all habits and monthly tracking data |
| `last_run.txt` | Saves the last program run time |

---

## ⚙️ Requirements

Make sure you have Python installed (version 3.7 or above).

Then install the required package using:
```bash
pip install pandas openpyxl
