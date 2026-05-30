#!/usr/bin/env python3
# 2026/05/30 coded by chatgpt, and modified

import tkinter as tk

root = tk.Tk()

root.overrideredirect(True)
root.attributes("-topmost", True)
root.attributes("-alpha", 0.2)

width = 100
height = 200

root.geometry(f"{width}x{height}+100+100")

canvas = tk.Canvas(
    root,
    bg="red",
    highlightthickness=0,
    bd=0
)
canvas.pack(fill="both", expand=True)

mode = None
start_x = start_y = 0
start_w = width
start_h = height

EDGE = 15


def button_press(event):
    global mode, start_x, start_y, start_w, start_h

    start_x = event.x_root
    start_y = event.y_root

    start_w = root.winfo_width()
    start_h = root.winfo_height()

    if event.x >= start_w - EDGE:
        mode = "resize_width"
    elif event.y >= start_h - EDGE:
        mode = "resize_height"
    else:
        mode = "move"


def motion(event):
    global start_x, start_y

    dx = event.x_root - start_x
    dy = event.y_root - start_y

    if mode == "move":
        x = root.winfo_x() + dx
        y = root.winfo_y() + dy
        root.geometry(f"+{x}+{y}")

        start_x = event.x_root
        start_y = event.y_root

    elif mode == "resize_width":
        w = max(20, start_w + dx)
        root.geometry(f"{w}x{root.winfo_height()}")

    elif mode == "resize_height":
        h = max(2, start_h + dy)
        root.geometry(f"{root.winfo_width()}x{h}")


canvas.bind("<Button-1>", button_press)
canvas.bind("<B1-Motion>", motion)

root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()
