import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

# --- Configuration ---
ARRAY_SIZE = 50
MIN_VALUE = 10
MAX_VALUE = 300
BAR_WIDTH = 10
DELAY_MS = 10 # Initial visualization delay in milliseconds

# --- Color Constants ---
COLOR_DEFAULT = 'blue'
COLOR_COMPARE = 'red'
COLOR_SWAP = 'green'
COLOR_SORTED = 'purple'

class SortingVisualizerApp:
    """
    A Tkinter application to visualize various sorting algorithms.
    """
    def __init__(self, master):
        self.master = master
        master.title("Python Sorting Visualizer")

        self.data = self._generate_data(ARRAY_SIZE, MIN_VALUE, MAX_VALUE)
        self.is_sorting = False
        self.speed = tk.DoubleVar(value=DELAY_MS)

        self._setup_ui()
        self._draw_bars()

    def _generate_data(self, size, min_val, max_val):
        """Generates a list of unique random integers."""
        return random.sample(range(min_val, max_val + 1), size)

    def _setup_ui(self):
        """Sets up the main GUI elements."""
        
        # Main Frame for controls
        control_frame = ttk.Frame(self.master, padding="10 10 10 10")
        control_frame.pack(fill='x')

        # Algorithm Selection
        ttk.Label(control_frame, text="Algorithm:").grid(row=0, column=0, padx=5, pady=5)
        self.algo_var = tk.StringVar(value='Bubble Sort')
        algos = ['Bubble Sort', 'Insertion Sort']
        ttk.Combobox(control_frame, textvariable=self.algo_var, values=algos, width=15, state="readonly").grid(row=0, column=1, padx=5, pady=5)

        # Speed Slider
        ttk.Label(control_frame, text="Speed (ms):").grid(row=0, column=2, padx=5, pady=5)
        self.speed_scale = ttk.Scale(control_frame, from_=1, to_=500, orient="horizontal", variable=self.speed, length=200, command=self._update_speed_label)
        self.speed_scale.grid(row=0, column=3, padx=5, pady=5)
        self.speed_label = ttk.Label(control_frame, text=f"{DELAY_MS} ms")
        self.speed_label.grid(row=0, column=4, padx=5, pady=5)

        # Buttons
        ttk.Button(control_frame, text="Start Sort", command=self.start_sort, style='TButton').grid(row=1, column=0, padx=5, pady=5, sticky='w')
        ttk.Button(control_frame, text="New Array", command=self.new_array, style='TButton').grid(row=1, column=1, padx=5, pady=5, sticky='w')

        # Visualization Area
        self.canvas_width = ARRAY_SIZE * (BAR_WIDTH + 2) + 20
        self.canvas_height = MAX_VALUE + 50
        self.canvas = tk.Canvas(self.master, width=self.canvas_width, height=self.canvas_height, bg="lightgrey")
        self.canvas.pack(padx=10, pady=10)

    def _update_speed_label(self, val):
        """Updates the speed label next to the slider."""
        self.speed_label.config(text=f"{int(float(val))} ms")

    def new_array(self):
        """Generates and draws a new random array."""
        if self.is_sorting:
            messagebox.showinfo("Wait", "Please wait for the current sort to finish.")
            return

        self.data = self._generate_data(ARRAY_SIZE, MIN_VALUE, MAX_VALUE)
        self._draw_bars()

    def _draw_bars(self, highlight=None, highlight_color=COLOR_DEFAULT, sorted_indices=None):
        """
        Draws the array elements as vertical bars on the canvas.
        Highlight is a list of indices to color, or an index.
        """
        self.canvas.delete("all")
        if sorted_indices is None:
            sorted_indices = set()
            
        if isinstance(highlight, int):
            highlight = [highlight]
        elif highlight is None:
            highlight = []

        for i, height in enumerate(self.data):
            x0 = 10 + i * (BAR_WIDTH + 2)
            y0 = self.canvas_height - height - 10 # Invert for top-down drawing
            x1 = x0 + BAR_WIDTH
            y1 = self.canvas_height - 10

            color = COLOR_DEFAULT
            if i in sorted_indices:
                color = COLOR_SORTED
            elif i in highlight:
                color = highlight_color

            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline='black')

        self.master.update_idletasks()

    def start_sort(self):
        """Initiates the sorting process based on the selected algorithm."""
        if self.is_sorting:
            return

        self.is_sorting = True
        algo_name = self.algo_var.get()
        
        # Reset colors before starting
        self._draw_bars()

        if algo_name == 'Bubble Sort':
            steps_generator = self._bubble_sort_generator()
        elif algo_name == 'Insertion Sort':
            steps_generator = self._insertion_sort_generator()
        else:
            messagebox.showerror("Error", "Selected algorithm not implemented.")
            self.is_sorting = False
            return
            
        self._animate_sort(steps_generator)

    def _animate_sort(self, steps_generator, sorted_indices=None):
        """Drives the visualization using the generator."""
        if sorted_indices is None:
            sorted_indices = set()

        try:
            # Get the next state from the generator
            indices, action = next(steps_generator) 
            
            if action == 'compare':
                color = COLOR_COMPARE
            elif action == 'swap':
                color = COLOR_SWAP
            elif action == 'sorted_segment':
                # Mark a segment (or a single element) as sorted
                for i in indices:
                    sorted_indices.add(i)
                color = COLOR_SORTED # Use a dedicated color for the last action
                
            self._draw_bars(highlight=indices, highlight_color=color, sorted_indices=sorted_indices)
            
            # Schedule the next animation step
            delay = int(self.speed.get())
            self.master.after(delay, self._animate_sort, steps_generator, sorted_indices)

        except StopIteration:
            # Sort finished
            # Mark all bars as sorted
            for i in range(len(self.data)):
                sorted_indices.add(i)
            self._draw_bars(sorted_indices=sorted_indices)
            
            self.is_sorting = False
            messagebox.showinfo("Complete", f"{self.algo_var.get()} finished sorting!")

    # --- Sorting Algorithm Implementations (using generators) ---

    def _bubble_sort_generator(self):
        """Bubble Sort implementation as a generator."""
        n = len(self.data)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                # 1. Yield comparison step
                yield [j, j + 1], 'compare'
                
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    swapped = True
                    # 2. Yield swap step
                    yield [j, j + 1], 'swap'

            # 3. Mark the largest element (n - i - 1) as sorted
            yield [n - i - 1], 'sorted_segment'

            if not swapped:
                # If no two elements were swapped, array is sorted
                for k in range(n - i - 1): # Mark remaining as sorted
                    yield [k], 'sorted_segment'
                return
        
        # Final element (index 0) is sorted when the loop completes
        yield [0], 'sorted_segment'
        
    def _insertion_sort_generator(self):
        """Insertion Sort implementation as a generator."""
        n = len(self.data)
        for i in range(1, n):
            key = self.data[i]
            j = i - 1
            
            # Mark the element being positioned as highlighted
            yield [i], 'compare'

            while j >= 0 and self.data[j] > key:
                # 1. Yield comparison step
                yield [j, j + 1], 'compare'
                
                self.data[j + 1] = self.data[j]
                j -= 1
                
                # 2. Yield swap/shift step (showing the element moving)
                yield [j + 2, j + 1], 'swap'

            self.data[j + 1] = key
            
            # 3. Mark current element insertion point
            yield [j + 1], 'sorted_segment'

if __name__ == '__main__':
    root = tk.Tk()
    app = SortingVisualizerApp(root)
    root.mainloop()

