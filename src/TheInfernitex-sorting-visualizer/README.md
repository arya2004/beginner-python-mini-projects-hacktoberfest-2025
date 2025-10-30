# Sorting Algorithm Visualizer (Python & Tkinter)

This project provides a simple, graphical tool to visualize how common sorting algorithms rearrange data step-by-step. It uses only **Tkinter**, which is part of the standard Python library.

---

## 🧩 Features

- **Algorithms:** Currently includes _Bubble Sort_ and _Insertion Sort_.
- **Dynamic Data:** Generates a new random array of bars for each run.
- **Step-by-Step Visualization:**

  - Red: Bars currently being compared
  - Green: Bars being swapped
  - Purple: Bars that are sorted

- **Speed Control:** A slider allows you to adjust the delay between visual updates (in milliseconds).

---

## ⚙️ Prerequisites

You need a working **Python 3** installation. No external libraries are required, since **Tkinter** is included with most standard Python distributions.

---

## 🚀 Installation and Running

Open a terminal and execute:

```bash
  python main.py
```

---

## 🧠 How to Use

1. **Select Algorithm:**
   Use the dropdown menu to choose between _Bubble Sort_ and _Insertion Sort_.

2. **Adjust Speed:**
   Use the slider to set the delay between visual updates (in milliseconds).

3. **Start / New Array:**

   - Click **New Array** to generate a new set of randomized bars.
   - Click **Start Sort** to begin visualization for the selected algorithm.

4. **Observe:**

   - **Red bars** → elements being compared
   - **Green bars** → elements being swapped
   - **Purple bars** → elements sorted

---

## 🧬 Technical Details

The visualization is achieved using Python's **generator functions**. Each sorting algorithm yields the current state — including indices being acted upon and the action type — back to the main GUI loop.

The GUI loop handles rendering by redrawing bars with appropriate colors, and uses `self.master.after(delay)` to schedule the next step based on the selected speed.

---

### 🖼 Example Visualization Flow

```text
[Randomized bars] → [Comparisons (red)] → [Swaps (green)] → [Sorted (purple)]
```

---

**Author:** Your Name Here
**Language:** Python 3
**Library:** Tkinter (Standard Library)
