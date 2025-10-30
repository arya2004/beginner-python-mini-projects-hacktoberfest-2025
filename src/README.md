# Dijkstra's Pathfinding Visualizer (Python & Tkinter)

This project is a **self-contained pathfinding visualizer** built entirely in Python using the **Tkinter** library. It demonstrates **Dijkstra's algorithm** in action — finding the shortest path between two points on a grid while navigating around user-defined barriers.

---

## Features

- **Interactive Grid**: Click on cells to set the **Start**, **End**, and **Barriers**.
- **Dijkstra's Algorithm**: Uses a **priority queue** (`heapq`) for efficient node selection.
- **Step-by-Step Visualization**: Watch the algorithm explore and find the shortest path in real time.
- **Simple GUI**: Uses only **Tkinter**, included with standard Python installations.

---

## Setup & Running

### Requirements

No external dependencies — just **Python 3** with the standard library.

### Steps

**Run** the script from your terminal:

```bash
python main.py
```

That's it! The GUI window will open and you're ready to visualize.

---

## How to Use

### 1. **Select Mode**

Use the buttons at the top to choose what to place:

- 🟦 **Start Node**
- 🟥 **End Node**
- ⬛ **Barrier** _(default)_

### 2. **Place Nodes**

- Click on an empty cell to place the **Start** (blue) or **End** (red) node — only one of each allowed.
- Click on empty cells to place **barriers** (black). Clicking again removes them.

### 3. **Run the Algorithm**

Click **"Run Dijkstra's"** to begin visualization:

- **Cyan cells** → nodes visited during exploration.
- **Yellow cells** → final shortest path.

### 4. **Reset**

Click **"Reset Grid"** to clear everything and start over.

---

## Core Logic Overview

The grid is internally represented as a **2D list** of integers, each indicating the state of a cell.

| State Value | Meaning                 | Color  |
| ----------- | ----------------------- | ------ |
| 0           | Unvisited               | White  |
| 1           | Barrier                 | Black  |
| 2           | Start Node              | Blue   |
| 3           | End Node                | Red    |
| 4           | Visited (during search) | Cyan   |
| 5           | Path (reconstructed)    | Yellow |

The algorithm uses a **min-heap (priority queue)** to always expand the node with the smallest known distance, ensuring the path found is the true shortest path.

---

## Behind the Scenes

- **Data Structures:** Lists and dictionaries to manage distances and neighbors.
- **Heapq:** Provides O(log n) extraction of the minimum-distance node.
- **Tkinter Canvas:** Used to draw the grid and dynamically color cells during execution.

---

## References

- [Dijkstra's Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
