#!/usr/bin/env python3
"""Tkinter canvas drawing program."""

import tkinter

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
PEN_WIDTH = 4
ERASER_WIDTH = 24
PEN_COLORS = ("black", "red")
BACKGROUND_COLOR = "white"


class DrawingApp:
    """Simple drawing canvas with pen, eraser, and color toggle."""

    def __init__(self) -> None:
        self.root = tkinter.Tk()
        self.root.title("Tkinter Drawing Canvas")

        self.pen_color_index = 0
        self.last_pen_position = None
        self.last_eraser_position = None

        self.status_label = tkinter.Label(self.root, anchor="w")
        self.status_label.pack(fill="x")

        self.canvas = tkinter.Canvas(
            self.root,
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
            bg=BACKGROUND_COLOR,
        )
        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<Button-1>", self.start_pen)
        self.canvas.bind("<B1-Motion>", self.draw_pen)
        self.canvas.bind("<ButtonRelease-1>", self.stop_pen)
        self.canvas.bind("<Button-2>", self.toggle_pen_color)
        self.canvas.bind("<Button-3>", self.start_eraser)
        self.canvas.bind("<B3-Motion>", self.draw_eraser)
        self.canvas.bind("<ButtonRelease-3>", self.stop_eraser)

        self.update_status()

    def current_pen_color(self) -> str:
        """Return the currently selected pen color."""
        return PEN_COLORS[self.pen_color_index]

    def update_status(self) -> None:
        """Show the current operation guide and pen color."""
        self.status_label.configure(
            text=(
                f"Left drag: pen ({self.current_pen_color()}) / "
                "Right drag: eraser / Middle click: toggle black and red"
            )
        )

    def start_pen(self, event: tkinter.Event) -> None:
        """Start drawing with the pen."""
        self.last_pen_position = (event.x, event.y)

    def draw_pen(self, event: tkinter.Event) -> None:
        """Draw a line from the previous pointer position to the current one."""
        if self.last_pen_position is None:
            self.start_pen(event)
            return

        x, y = self.last_pen_position
        self.canvas.create_line(
            x,
            y,
            event.x,
            event.y,
            fill=self.current_pen_color(),
            width=PEN_WIDTH,
            capstyle=tkinter.ROUND,
            smooth=True,
        )
        self.last_pen_position = (event.x, event.y)

    def stop_pen(self, event: tkinter.Event) -> None:
        """Stop drawing with the pen."""
        self.last_pen_position = None

    def start_eraser(self, event: tkinter.Event) -> None:
        """Start erasing by drawing with the canvas background color."""
        self.last_eraser_position = (event.x, event.y)

    def draw_eraser(self, event: tkinter.Event) -> None:
        """Erase a line from the previous pointer position to the current one."""
        if self.last_eraser_position is None:
            self.start_eraser(event)
            return

        x, y = self.last_eraser_position
        self.canvas.create_line(
            x,
            y,
            event.x,
            event.y,
            fill=BACKGROUND_COLOR,
            width=ERASER_WIDTH,
            capstyle=tkinter.ROUND,
            smooth=True,
        )
        self.last_eraser_position = (event.x, event.y)

    def stop_eraser(self, event: tkinter.Event) -> None:
        """Stop erasing."""
        self.last_eraser_position = None

    def toggle_pen_color(self, event: tkinter.Event) -> str:
        """Toggle the pen color between black and red."""
        self.pen_color_index = 1 - self.pen_color_index
        self.update_status()
        return "break"

    def run(self) -> None:
        """Run the Tkinter main loop."""
        self.root.mainloop()


if __name__ == "__main__":
    DrawingApp().run()
