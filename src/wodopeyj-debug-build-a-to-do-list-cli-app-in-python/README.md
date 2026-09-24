# FocusBoard: To-Do List CLI App

FocusBoard is a local-first command-line task manager with priorities, categories, due dates, notes, search, and progress statistics. It keeps the simple workflow of a beginner todo app while giving each task enough detail to stay useful.

## Features

- Add tasks with a title, category, priority, due date, and notes
- View and search tasks by title or category
- Automatically identify open, done, and overdue tasks
- Edit, complete, reopen, or delete tasks by ID
- View a dashboard with completion and overdue statistics
- Save tasks locally in `tasks.json`

## Requirements

- Python 3.7 or later
- No external packages

## Running the App

From the repository root, run:

```bash
cd src/wodopeyj-debug-build-a-to-do-list-cli-app-in-python
python todo.py
```

On some systems, use `python3 todo.py` instead.

## Menu

| Option | Action |
| --- | --- |
| `1` | Add a task |
| `2` | View all tasks or search by title/category |
| `3` | Delete a task after confirmation |
| `4` | Edit a task |
| `5` | Complete or reopen a task |
| `6` | Exit and save |
| `7` | Show the dashboard |

## Project Structure

```text
todo.py         # Main FocusBoard CLI application
tasks.json      # Local task storage, created after the first save
README.md       # Project documentation
```