# 💰 Expense and Lending Management System

> A Python-based console application to **track monthly expenses, manage money lent to others, and calculate balances automatically** — powered by **pandas** and Excel/CSV integration.

---

## 🧠 Project Overview

This project is a **personal finance management tool** that helps you:
- Record expenses by category (like Food, Travel, Bills, etc.)
- Keep track of money lent to friends or family
- Manage repayments and update your available balance automatically

All data is stored in:
- `DEM.xlsx` → for monthly expenses  
- `DEMLended.csv` → for lent money tracking  
- `last_run.txt` → to log your last program use  

The system is fully **interactive** and **beginner-friendly**, ideal for learning how to use **pandas** for data handling in real-world scenarios.

---

## ✨ Features

- 🧾 Add and view monthly categorized expenses  
- 💵 Track money lent to others with date and category  
- 🔁 Update records when money is returned  
- 📊 Automatically calculate total expenses and remaining balance  
- 🕒 Maintain last-run timestamps for activity tracking  

---

## 🧰 Tech Stack

| Component | Description |
|------------|--------------|
| **Language** | Python 3.x |
| **Libraries Used** | pandas, datetime, os |
| **Storage Files** | Excel (`DEM.xlsx`) and CSV (`DEMLended.csv`) |
| **Platform** | Windows / Linux / macOS |

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/Expense-Lending-Manager.git
cd Expense-Lending-Manager
