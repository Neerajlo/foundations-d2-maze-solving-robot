
import tkinter as tk
from tkinter import ttk, messagebox
import time

from src.maze import Maze
from src.maze_generator import generate_maze
from src.bfs import bfs
from src.solver import dfs, astar, reactive_astar
from src.dstar_lite import DStarLite


# ============================================================
# MAZELAB - THEME
# ============================================================

BG = "#0B1120"
PANEL = "#151F32"
PANEL_LIGHT = "#1D2A40"

ACCENT = "#3B82F6"
GREEN = "#22C55E"
ORANGE = "#F59E0B"
RED = "#EF4444"
PURPLE = "#A78BFA"

TEXT = "#F1F5F9"
MUTED = "#94A3B8"

WALL = "#263449"
OPEN = "#F8FAFC"
EXPLORED = "#93C5FD"
PATH = "#22C55E"


class MazeVisualizer:

    def __init__(self, root):

        self.root = root
        self.root.title("MazeLab | Intelligent Pathfinding Simulator")
        self.root.geometry("1280x900")
        self.root.minsize(1000, 700)
        self.root.configure(bg=BG)

        self.rows = 10
        self.cols = 10
        self.seed = 42

        self.maze = None

        self.events = []
        self.event_index = 0

        self.after_id = None
        self.running = False
        self.paused = False

        self.current_cell = None
        self.cell_size = 0
        self.offset_x = 0
        self.offset_y = 0

        self.setup_styles()
        self.setup_ui()
        self.generate_maze()

        self.root.bind("<Configure>", self.on_resize)
        self.root.protocol("WM_DELETE_WINDOW", self.close_application)

    # ========================================================
    # STYLES
    # ========================================================

    def setup_styles(self):

        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "TCombobox",
            fieldbackground=PANEL_LIGHT,
            background=PANEL_LIGHT,
            foreground=TEXT,
            arrowcolor=TEXT,
            padding=7
        )

        style.map(
            "TCombobox",
            fieldbackground=[("readonly", PANEL_LIGHT)],
            foreground=[("readonly", TEXT)]
        )

    # ========================================================
    # MAIN INTERFACE
    # ========================================================

    def setup_ui(self):

       

        # ---------------- HEADER ----------------

        header = tk.Frame(self.root, bg=BG)
        header.pack(fill="x", padx=25, pady=(18, 16))

        header.grid_columnconfigure(0, weight=1)
        header.grid_columnconfigure(1, weight=0)
        header.grid_columnconfigure(2, weight=1)

        # Centered title
        title_area = tk.Frame(header, bg=BG)
        title_area.grid(row=0, column=1)

        tk.Label(
            title_area,
            text="MAZELAB",
            font=("Segoe UI", 32, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(anchor="center")

        tk.Label(
            title_area,
            text="INTELLIGENT PATHFINDING SIMULATOR",
            font=("Segoe UI", 10, "bold"),
            fg=ACCENT,
            bg=BG
        ).pack(anchor="center", pady=(2, 0))

        # Status on the right
        self.header_status = tk.Label(
            header,
            text="● READY",
            font=("Segoe UI", 10, "bold"),
            fg=GREEN,
            bg=PANEL,
            padx=18,
            pady=10
        )

        self.header_status.grid(
            row=0,
            column=2,
            sticky="e"
        )



        # ---------------- MAIN CONTENT ----------------

        main = tk.Frame(self.root, bg=BG)
        main.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=5
        )

        main.grid_columnconfigure(0, weight=0)
        main.grid_columnconfigure(1, weight=1)
        main.grid_rowconfigure(0, weight=1)

        # ---------------- SIDEBAR ----------------

        sidebar = tk.Frame(
            main,
            bg=PANEL,
            width=275
        )

        sidebar.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 14)
        )

        sidebar.grid_propagate(False)

        tk.Label(
            sidebar,
            text="SIMULATION CONTROLS",
            font=("Segoe UI", 11, "bold"),
            fg=TEXT,
            bg=PANEL
        ).pack(anchor="w", padx=18, pady=(20, 15))

        self.add_label(sidebar, "PATHFINDING ALGORITHM")

        self.algorithm = ttk.Combobox(
            sidebar,
            values=[
                "BFS",
                "DFS",
                "A*",
                "Reactive A*",
                "D* Lite"
            ],
            state="readonly"
        )

        self.algorithm.current(0)
        self.algorithm.pack(
            fill="x",
            padx=18,
            pady=(5, 13)
        )

        self.add_label(sidebar, "MAZE DIMENSIONS")

        self.size = ttk.Combobox(
            sidebar,
            values=[
                "10 x 10",
                "20 x 20",
                "30 x 30"
            ],
            state="readonly"
        )

        self.size.current(0)
        self.size.pack(
            fill="x",
            padx=18,
            pady=(5, 13)
        )

        self.add_label(sidebar, "SIMULATION ACTIONS")

        self.make_button(
            sidebar,
            "Generate New Maze",
            ACCENT,
            self.generate_maze
        ).pack(fill="x", padx=18, pady=4)

        self.make_button(
            sidebar,
            "▶   Start Simulation",
            "#15803D",
            self.start
        ).pack(fill="x", padx=18, pady=4)

        self.make_button(
            sidebar,
            "Ⅱ   Pause / Resume",
            "#B7791F",
            self.pause
        ).pack(fill="x", padx=18, pady=4)

        self.make_button(
            sidebar,
            "↻   Reset Simulation",
            "#B45353",
            self.reset
        ).pack(fill="x", padx=18, pady=4)

        # ---------------- SPEED CONTROL ----------------

        tk.Label(
            sidebar,
            text="ANIMATION SPEED",
            font=("Segoe UI", 9, "bold"),
            fg=TEXT,
            bg=PANEL
        ).pack(anchor="w", padx=18, pady=(15, 2))

        speed_header = tk.Frame(sidebar, bg=PANEL)
        speed_header.pack(fill="x", padx=18)

        tk.Label(
            speed_header,
            text="Slow",
            fg=MUTED,
            bg=PANEL,
            font=("Segoe UI", 8)
        ).pack(side="left")

        self.speed_value = tk.Label(
            speed_header,
            text="120 ms",
            fg=ACCENT,
            bg=PANEL,
            font=("Segoe UI", 9, "bold")
        )
        self.speed_value.pack(side="right")

        self.speed = tk.Scale(
            sidebar,
            from_=60,
            to=350,
            orient="horizontal",
            resolution=10,
            command=self.update_speed,
            bg=PANEL,
            fg=TEXT,
            troughcolor=PANEL_LIGHT,
            highlightthickness=0,
            activebackground=ACCENT,
            showvalue=False,
            bd=0
        )

        self.speed.set(120)
        self.speed.pack(fill="x", padx=15)

        # ---------------- LEGEND ----------------

        tk.Label(
            sidebar,
            text="VISUALIZATION LEGEND",
            font=("Segoe UI", 10, "bold"),
            fg=TEXT,
            bg=PANEL
        ).pack(
            anchor="w",
            padx=18,
            pady=(12, 8)
        )

        legend_items = [
            ("Start", "#2563EB"),
            ("Goal", ORANGE),
            ("Wall", WALL),
            ("Open", OPEN),
            ("Explored", EXPLORED),
            ("Final path", PATH),
            ("Robot", PURPLE)
        ]

        legend_grid = tk.Frame(sidebar, bg=PANEL)
        legend_grid.pack(fill="x", padx=14)

        for index, (label, color) in enumerate(legend_items):

            row = index // 2
            col = index % 2

            item = tk.Frame(
                legend_grid,
                bg=PANEL
            )

            item.grid(
                row=row,
                column=col,
                sticky="w",
                padx=4,
                pady=5
            )

            tk.Label(
                item,
                text="  ",
                bg=color,
                width=2
            ).pack(side="left", padx=(0, 5))

            tk.Label(
                item,
                text=label,
                font=("Segoe UI", 8),
                fg=MUTED,
                bg=PANEL
            ).pack(side="left")

        # ---------------- RIGHT AREA ----------------

        right = tk.Frame(main, bg=BG)

        right.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        # ---------------- MAZE PANEL ----------------

        maze_panel = tk.Frame(
            right,
            bg=PANEL
        )

        maze_panel.pack(
            fill="both",
            expand=True
        )

        maze_header = tk.Frame(
            maze_panel,
            bg=PANEL
        )

        maze_header.pack(
            fill="x",
            padx=20,
            pady=13
        )

        tk.Label(
            maze_header,
            text="MAZE ENVIRONMENT",
            font=("Segoe UI", 12, "bold"),
            fg=TEXT,
            bg=PANEL
        ).pack(side="left")

        self.maze_info = tk.Label(
            maze_header,
            text="10 × 10",
            font=("Segoe UI", 9, "bold"),
            fg=ACCENT,
            bg=PANEL
        )

        self.maze_info.pack(side="right")

        self.canvas = tk.Canvas(
            maze_panel,
            bg="#E2E8F0",
            highlightthickness=0
        )

        self.canvas.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

        # ---------------- METRICS ----------------

        tk.Label(
            right,
            text="PERFORMANCE METRICS",
            font=("Segoe UI", 11, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(
            anchor="w",
            pady=(13, 8)
        )

        stats = tk.Frame(right, bg=BG)
        stats.pack(fill="x")

        for column in range(3):
            stats.grid_columnconfigure(column, weight=1)

        self.path_value = self.create_stat(
            stats,
            "PATH LENGTH",
            "—",
            0
        )

        self.nodes_value = self.create_stat(
            stats,
            "NODES EXPANDED",
            "—",
            1
        )

        self.time_value = self.create_stat(
            stats,
            "EXECUTION TIME",
            "—",
            2
        )

        # ---------------- STATUS BAR ----------------

        self.status = tk.Label(
            right,
            text="Ready. Select an algorithm and start.",
            font=("Segoe UI", 9),
            fg=MUTED,
            bg=PANEL,
            anchor="w",
            padx=14,
            pady=10
        )

        self.status.pack(
            fill="x",
            pady=(10, 0)
        )

        # ---------------- FOOTER ----------------

        tk.Label(
            self.root,
            text=(
                "MAZELAB  |  BFS  •  DFS  •  A*  •  "
                "REACTIVE A*  •  D* LITE"
            ),
            font=("Segoe UI", 8, "bold"),
            fg="#64748B",
            bg=BG
        ).pack(pady=(7, 10))

    # ========================================================
    # UI HELPERS
    # ========================================================

    def add_label(self, parent, text):

        tk.Label(
            parent,
            text=text,
            font=("Segoe UI", 8, "bold"),
            fg=MUTED,
            bg=PANEL
        ).pack(anchor="w", padx=18)

    def make_button(self, parent, text, color, command):

        return tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg="white",
            activebackground=color,
            activeforeground="white",
            relief="flat",
            borderwidth=0,
            cursor="hand2",
            font=("Segoe UI", 9, "bold"),
            padx=10,
            pady=10
        )

    def create_stat(self, parent, title, value, column):

        card = tk.Frame(
            parent,
            bg=PANEL,
            padx=13,
            pady=12
        )

        card.grid(
            row=0,
            column=column,
            sticky="nsew",
            padx=5
        )

        tk.Label(
            card,
            text=title,
            font=("Segoe UI", 8, "bold"),
            fg=MUTED,
            bg=PANEL
        ).pack(anchor="w")

        value_label = tk.Label(
            card,
            text=value,
            font=("Segoe UI", 18, "bold"),
            fg=TEXT,
            bg=PANEL
        )

        value_label.pack(
            anchor="w",
            pady=(5, 0)
        )

        return value_label

    def update_speed(self, value):

        self.speed_value.config(
            text=f"{int(float(value))} ms"
        )

    # ========================================================
    # MAZE GENERATION
    # ========================================================

    def generate_maze(self):

        self.stop_animation()

        selected = self.size.get()

        if selected == "20 x 20":
            self.rows = self.cols = 20

        elif selected == "30 x 30":
            self.rows = self.cols = 30

        else:
            self.rows = self.cols = 10

        grid = generate_maze(
            self.rows,
            self.cols,
            self.seed
        )

        self.seed += 1

        self.maze = Maze(
            grid,
            start=(0, 0),
            goal=(self.rows - 1, self.cols - 1)
        )

        self.events = []
        self.event_index = 0
        self.current_cell = None

        self.maze_info.config(
            text=f"{self.rows} × {self.cols}"
        )

        self.clear_metrics()

        self.set_status(
            "New maze generated successfully."
        )

        self.draw_maze()

    # ========================================================
    # DRAW MAZE
    # ========================================================

    def draw_maze(self):

        if self.maze is None:
            return

        self.canvas.delete("all")

        canvas_width = max(
            self.canvas.winfo_width(),
            300
        )

        canvas_height = max(
            self.canvas.winfo_height(),
            300
        )

        padding = 15

        self.cell_size = min(
            (canvas_width - 2 * padding) / self.cols,
            (canvas_height - 2 * padding) / self.rows
        )

        grid_width = self.cell_size * self.cols
        grid_height = self.cell_size * self.rows

        self.offset_x = (
            canvas_width - grid_width
        ) / 2

        self.offset_y = (
            canvas_height - grid_height
        ) / 2

        # Draw grid.
        for row in range(self.rows):

            for col in range(self.cols):

                x1 = self.offset_x + col * self.cell_size
                y1 = self.offset_y + row * self.cell_size

                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                value = self.maze.grid[row][col]

                color = WALL if value == 1 else OPEN

                if (row, col) == self.maze.start:
                    color = "#2563EB"

                elif (row, col) == self.maze.goal:
                    color = ORANGE

                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline="#CBD5E1",
                    width=0.6
                )

        # Draw exploration and final path.
        for event_type, cell in self.events[:self.event_index]:

            if cell in (
                self.maze.start,
                self.maze.goal
            ):
                continue

            row, col = cell

            x1 = self.offset_x + col * self.cell_size
            y1 = self.offset_y + row * self.cell_size

            color = (
                EXPLORED
                if event_type == "visited"
                else PATH
            )

            self.canvas.create_rectangle(
                x1,
                y1,
                x1 + self.cell_size,
                y1 + self.cell_size,
                fill=color,
                outline="#CBD5E1",
                width=0.6
            )

        # Draw moving robot.
        if self.current_cell is not None:

            self.draw_robot(self.current_cell)

        # Draw start and goal labels.
        for cell, color, label in [
            (self.maze.start, "#2563EB", "S"),
            (self.maze.goal, ORANGE, "G")
        ]:

            row, col = cell

            x1 = self.offset_x + col * self.cell_size
            y1 = self.offset_y + row * self.cell_size

            if self.cell_size >= 18:

                self.canvas.create_text(
                    x1 + self.cell_size / 2,
                    y1 + self.cell_size / 2,
                    text=label,
                    fill="white",
                    font=(
                        "Segoe UI",
                        max(7, int(self.cell_size * 0.35)),
                        "bold"
                    )
                )

    # ========================================================
    # ROBOT DRAWING
    # ========================================================

    def draw_robot(self, cell):

        row, col = cell

        x1 = self.offset_x + col * self.cell_size
        y1 = self.offset_y + row * self.cell_size

        center_x = x1 + self.cell_size / 2
        center_y = y1 + self.cell_size / 2

        radius = max(
            5,
            self.cell_size * 0.34
        )

        # Robot antenna.
        self.canvas.create_line(
            center_x,
            center_y - radius,
            center_x,
            center_y - radius - 4,
            fill=PURPLE,
            width=2
        )

        self.canvas.create_oval(
            center_x - 2,
            center_y - radius - 7,
            center_x + 2,
            center_y - radius - 3,
            fill=ORANGE,
            outline=ORANGE
        )

        # Robot body.
        self.canvas.create_oval(
            center_x - radius,
            center_y - radius,
            center_x + radius,
            center_y + radius,
            fill=PURPLE,
            outline="white",
            width=2
        )

        # Robot eyes.
        eye_size = max(
            1.5,
            self.cell_size * 0.055
        )

        self.canvas.create_oval(
            center_x - radius * 0.4 - eye_size,
            center_y - eye_size,
            center_x - radius * 0.4 + eye_size,
            center_y + eye_size,
            fill="white",
            outline=""
        )

        self.canvas.create_oval(
            center_x + radius * 0.4 - eye_size,
            center_y - eye_size,
            center_x + radius * 0.4 + eye_size,
            center_y + eye_size,
            fill="white",
            outline=""
        )

    # ========================================================
    # WINDOW RESIZING
    # ========================================================

    def on_resize(self, event):

        if event.widget == self.root and self.maze:

            self.draw_maze()

    # ========================================================
    # RUN ALGORITHMS
    # ========================================================

    def start(self):

        if self.maze is None:
            return

        self.stop_animation()

        self.events = []
        self.event_index = 0
        self.current_cell = None

        selected = self.algorithm.get()

        self.set_status(
            f"Executing {selected}..."
        )

        self.root.update_idletasks()

        start_time = time.perf_counter()

        try:

            if selected == "BFS":
                result = bfs(self.maze)

            elif selected == "DFS":
                result = dfs(self.maze)

            elif selected == "A*":
                result = astar(self.maze)

            elif selected == "Reactive A*":
                result = reactive_astar(self.maze)

            else:
                planner = DStarLite(self.maze)
                result = planner.plan()

        except Exception as error:

            messagebox.showerror(
                "Algorithm Error",
                str(error)
            )

            self.set_status(
                "Algorithm execution failed."
            )

            return

        elapsed = (
            time.perf_counter() - start_time
        )

        path_length = result.get(
            "actual_distance",
            result.get("path_length", 0)
        )

        nodes = result.get(
            "nodes_expanded",
            0
        )

        success = result.get(
            "success",
            False
        )

        # Update metric cards.
        self.path_value.config(
            text=str(path_length)
        )

        self.nodes_value.config(
            text=str(nodes)
        )

        self.time_value.config(
            text=f"{elapsed:.5f}s"
        )

        if not success:

            self.header_status.config(
                text="● NO PATH",
                fg=RED
            )

            self.set_status(
                "No valid path found."
            )

            self.draw_maze()
            return

        # Add actual explored cells.
        if "visited_order" in result:

            for cell in result["visited_order"]:

                self.events.append(
                    ("visited", cell)
                )

        # Add actual returned path.
        if "path" in result:

            for cell in result["path"]:

                self.events.append(
                    ("path", cell)
                )

        # Reactive A* does not currently return
        # a movement history or visited order.
        if selected == "Reactive A*":

            replans = result.get(
                "replan_count",
                0
            )

            obstacles = result.get(
                "obstacles_discovered",
                0
            )

            self.header_status.config(
                text="● COMPLETED",
                fg=GREEN
            )

            self.set_status(
                f"Reactive A* completed | "
                f"Replans: {replans} | "
                f"Obstacles discovered: {obstacles}. "
                "Movement animation is not yet available."
            )

            self.draw_maze()
            return

        if not self.events:

            self.header_status.config(
                text="● COMPLETED",
                fg=GREEN
            )

            self.set_status(
                "Execution completed. No animation data returned."
            )

            self.draw_maze()
            return

        self.running = True
        self.paused = False

        # Robot begins at start.
        self.current_cell = self.maze.start

        self.header_status.config(
            text="● RUNNING",
            fg=ORANGE
        )

        self.set_status(
            f"Animating {selected}..."
        )

        self.draw_maze()
        self.animate()

    # ========================================================
    # ANIMATION
    # ========================================================

    def animate(self):

        if not self.running or self.paused:
            return

        if self.event_index >= len(self.events):

            self.running = False

            self.current_cell = self.maze.goal

            self.header_status.config(
                text="● COMPLETED",
                fg=GREEN
            )

            self.set_status(
                "Pathfinding completed successfully!"
            )

            self.draw_maze()
            return

        event_type, cell = self.events[
            self.event_index
        ]

        # Move robot only during final path animation.
        if event_type == "path":

            self.current_cell = cell

        self.event_index += 1

        self.draw_maze()

        delay = int(
            self.speed.get()
        )

        self.after_id = self.root.after(
            delay,
            self.animate
        )

    # ========================================================
    # PAUSE / RESUME
    # ========================================================

    def pause(self):

        if not self.running:
            return

        self.paused = not self.paused

        if self.paused:

            if self.after_id:

                self.root.after_cancel(
                    self.after_id
                )

                self.after_id = None

            self.set_status(
                "Simulation paused."
            )

        else:

            self.set_status(
                "Simulation resumed."
            )

            self.animate()

    # ========================================================
    # RESET
    # ========================================================

    def reset(self):

        self.stop_animation()

        self.events = []
        self.event_index = 0
        self.current_cell = None

        self.clear_metrics()

        self.set_status(
            "Simulation reset."
        )

        self.draw_maze()

    def stop_animation(self):

        self.running = False
        self.paused = False

        if self.after_id:

            self.root.after_cancel(
                self.after_id
            )

            self.after_id = None

        self.header_status.config(
            text="● READY",
            fg=GREEN
        )

    # ========================================================
    # METRICS AND STATUS
    # ========================================================

    def clear_metrics(self):

        self.path_value.config(text="—")
        self.nodes_value.config(text="—")
        self.time_value.config(text="—")

    def set_status(self, message):

        self.status.config(
            text=message
        )

    # ========================================================
    # CLOSE APPLICATION
    # ========================================================

    def close_application(self):

        self.stop_animation()
        self.root.destroy()


# ============================================================
# APPLICATION ENTRY POINT
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = MazeVisualizer(root)

    root.mainloop()
