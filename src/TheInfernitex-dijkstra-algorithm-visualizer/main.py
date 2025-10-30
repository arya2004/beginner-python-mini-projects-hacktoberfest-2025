import tkinter as tk
from tkinter import messagebox
from collections import deque
import heapq # Used for the Priority Queue in Dijkstra's

# Configuration for the Grid and Visualization
ROWS = 20
COLS = 20
CELL_SIZE = 30
VISUALIZATION_DELAY_MS = 25

# Color constants for the grid cells
COLOR_DEFAULT = "white"
COLOR_BARRIER = "black"
COLOR_START = "blue"
COLOR_END = "red"
COLOR_VISITED = "cyan"
COLOR_PATH = "yellow"

class DijkstraVisualizer:
    """
    A Tkinter-based application to visualize Dijkstra's pathfinding algorithm.
    """
    def __init__(self, master):
        self.master = master
        master.title("Dijkstra's Visualizer")

        self.grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.start_node = None
        self.end_node = None
        self.is_running = False

        # 0: UNVISITED, 1: BARRIER, 2: START, 3: END, 4: VISITED, 5: PATH
        self.state_map = {
            0: COLOR_DEFAULT,
            1: COLOR_BARRIER,
            2: COLOR_START,
            3: COLOR_END,
            4: COLOR_VISITED,
            5: COLOR_PATH
        }

        self.create_widgets()
        self.draw_grid()

    def create_widgets(self):
        """Creates the control frame and buttons."""
        self.controls_frame = tk.Frame(self.master, padx=10, pady=10, bg="#f0f0f0")
        self.controls_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Label(self.controls_frame, text="Click to set:").pack(side=tk.LEFT, padx=5)

        # Start Node Button
        self.start_btn = tk.Button(self.controls_frame, text="Start Node", command=lambda: self.set_mode(2), bg=COLOR_START, fg="white")
        self.start_btn.pack(side=tk.LEFT, padx=5)
        
        # End Node Button
        self.end_btn = tk.Button(self.controls_frame, text="End Node", command=lambda: self.set_mode(3), bg=COLOR_END, fg="white")
        self.end_btn.pack(side=tk.LEFT, padx=5)
        
        # Barrier Button
        self.barrier_btn = tk.Button(self.controls_frame, text="Barrier", command=lambda: self.set_mode(1), bg=COLOR_BARRIER, fg="white")
        self.barrier_btn.pack(side=tk.LEFT, padx=5)

        # Run Button
        self.run_btn = tk.Button(self.controls_frame, text="Run Dijkstra's", command=self.run_dijkstra, bg="#4CAF50", fg="white")
        self.run_btn.pack(side=tk.LEFT, padx=15)
        
        # Reset Button
        self.reset_btn = tk.Button(self.controls_frame, text="Reset Grid", command=self.reset_grid, bg="#FF9800", fg="white")
        self.reset_btn.pack(side=tk.LEFT, padx=5)

        # Current Mode Display
        self.mode_label = tk.Label(self.controls_frame, text="Mode: Barrier", bg="#f0f0f0")
        self.mode_label.pack(side=tk.RIGHT, padx=5)
        
        self.current_mode = 1 # Default mode is barrier

    def set_mode(self, mode):
        """Sets the current cell placement mode."""
        self.current_mode = mode
        mode_text = {1: "Barrier", 2: "Start Node", 3: "End Node"}.get(mode, "Barrier")
        self.mode_label.config(text=f"Mode: {mode_text}")

    def draw_grid(self):
        """Initializes the grid display using frames."""
        self.grid_frame = tk.Frame(self.master, borderwidth=1, relief="solid")
        self.grid_frame.pack(padx=10, pady=10)

        self.cell_widgets = []
        for r in range(ROWS):
            row_widgets = []
            for c in range(COLS):
                cell = tk.Frame(
                    self.grid_frame, 
                    width=CELL_SIZE, 
                    height=CELL_SIZE, 
                    bg=self.state_map[self.grid[r][c]],
                    borderwidth=1, 
                    relief="solid"
                )
                cell.grid(row=r, column=c)
                
                # Bind click event
                cell.bind("<Button-1>", lambda event, r=r, c=c: self.on_cell_click(r, c))
                row_widgets.append(cell)
            self.cell_widgets.append(row_widgets)

    def on_cell_click(self, r, c):
        """Handles click events to place start, end, or barriers."""
        if self.is_running:
            return

        current_state = self.grid[r][c]
        
        if self.current_mode == 1: # Barrier Mode
            new_state = 0 if current_state == 1 else 1
            if new_state == 1 and (self.start_node == (r, c) or self.end_node == (r, c)):
                return # Cannot place barrier over start/end
            
            # If start/end is being removed, clear the respective reference
            if current_state == 2: self.start_node = None
            if current_state == 3: self.end_node = None
            
            self.grid[r][c] = new_state
            self.update_cell_color(r, c)

        elif self.current_mode == 2: # Start Node Mode
            if self.start_node:
                # Clear existing start node
                old_r, old_c = self.start_node
                self.grid[old_r][old_c] = 0
                self.update_cell_color(old_r, old_c)
            
            if (r, c) == self.end_node:
                return # Cannot place start over end
                
            self.start_node = (r, c)
            self.grid[r][c] = 2
            self.update_cell_color(r, c)

        elif self.current_mode == 3: # End Node Mode
            if self.end_node:
                # Clear existing end node
                old_r, old_c = self.end_node
                self.grid[old_r][old_c] = 0
                self.update_cell_color(old_r, old_c)

            if (r, c) == self.start_node:
                return # Cannot place end over start
                
            self.end_node = (r, c)
            self.grid[r][c] = 3
            self.update_cell_color(r, c)

    def update_cell_color(self, r, c, state=None):
        """Updates the color of a specific cell."""
        state = state if state is not None else self.grid[r][c]
        self.cell_widgets[r][c].config(bg=self.state_map[state])

    def reset_grid(self):
        """Resets the grid to the initial state."""
        self.is_running = False
        self.start_node = None
        self.end_node = None
        self.grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        
        for r in range(ROWS):
            for c in range(COLS):
                self.update_cell_color(r, c)
        
        self.master.update()

    def run_dijkstra(self):
        """
        Initializes and starts the Dijkstra's pathfinding process.
        """
        if self.is_running:
            return
            
        if not self.start_node or not self.end_node:
            messagebox.showerror("Error", "Please set both Start and End nodes.")
            return

        self.is_running = True
        
        # Reset visualization colors (keep barriers, start, end)
        for r in range(ROWS):
            for c in range(COLS):
                if self.grid[r][c] in [4, 5]: # Clear VISITED and PATH
                    self.grid[r][c] = 0
                    self.update_cell_color(r, c)

        # Dijkstra's Algorithm implementation
        start_r, start_c = self.start_node
        end_r, end_c = self.end_node

        # Priority Queue: (distance, row, col)
        pq = [(0, start_r, start_c)] 
        
        # Distance map: (row, col) -> distance
        distances = {(r, c): float('inf') for r in range(ROWS) for c in range(COLS)}
        distances[self.start_node] = 0

        # Parent map for path reconstruction: (row, col) -> (parent_row, parent_col)
        parents = {} 

        # List to store visualization steps
        self.visualization_steps = []
        
        # 4 directions: (dr, dc)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 

        while pq:
            # Get node with the smallest distance
            dist, r, c = heapq.heappop(pq)
            
            if dist > distances[(r, c)]:
                continue
                
            if (r, c) == self.end_node:
                # Goal reached! Reconstruct and visualize path
                self.reconstruct_path(parents)
                return

            if self.grid[r][c] == 0:
                self.visualization_steps.append(((r, c), 4)) # Mark as VISITED
                
            # Explore neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds and if not a barrier
                if 0 <= nr < ROWS and 0 <= nc < COLS and self.grid[nr][nc] != 1:
                    new_dist = dist + 1
                    
                    if new_dist < distances[(nr, nc)]:
                        distances[(nr, nc)] = new_dist
                        parents[(nr, nc)] = (r, c)
                        heapq.heappush(pq, (new_dist, nr, nc))

        # If loop finishes without reaching the end node
        self.is_running = False
        messagebox.showinfo("Result", "No path found to the End Node.")

    def reconstruct_path(self, parents):
        """
        Reconstructs the path from end to start using the parents map.
        Starts the visualization of the found path.
        """
        if self.end_node not in parents:
            messagebox.showinfo("Result", "No path found to the End Node.")
            self.is_running = False
            return

        path = deque()
        curr = self.end_node
        
        while curr in parents and curr != self.start_node:
            path.appendleft(curr)
            curr = parents[curr]
            
        # Add path visualization steps
        for r, c in path:
            if (r, c) != self.end_node: # Don't recolor the end node
                self.visualization_steps.append(((r, c), 5)) # Mark as PATH

        # Start the animated visualization
        self.visualize_step_by_step(0)

    def visualize_step_by_step(self, step_index):
        """
        Animates the search and path reconstruction based on stored steps.
        """
        if step_index < len(self.visualization_steps):
            (r, c), state = self.visualization_steps[step_index]
            
            # Only visualize if it's not start or end node (colors are fixed)
            if self.grid[r][c] not in [2, 3]: 
                self.grid[r][c] = state
                self.update_cell_color(r, c, state)
                
            # Schedule the next step
            self.master.after(VISUALIZATION_DELAY_MS, self.visualize_step_by_step, step_index + 1)
        else:
            self.is_running = False
            messagebox.showinfo("Complete", "Dijkstra's search complete and path displayed.")
            
if __name__ == '__main__':
    # Initialize the main Tkinter window
    root = tk.Tk()
    app = DijkstraVisualizer(root)
    # Start the Tkinter event loop
    root.mainloop()
