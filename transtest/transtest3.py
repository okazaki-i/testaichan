#!/usr/bin/env python3
# https://qiita.com/Tadataka_Takahashi/items/1e807387cb4f4e33927b

import tkinter as tk
from tkinter import colorchooser
from PIL import Image, ImageTk
import json
import random

class StickyNote(tk.Toplevel):
    def __init__(self, master, x, y, color, text=""):
        super().__init__(master)
        self.master = master
        self.overrideredirect(True)
        self.attributes("-alpha", 0.5)  # 透過度を0.9に設定（より不透明に）
        self.attributes("-topmost", True)

        self.geometry(f"200x200+{x}+{y}")
        self.color = color

        self.create_widgets()
        self.setup_drag()
        
        if text:
            self.text_widget.insert(tk.END, text)

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=200, height=200, highlightthickness=0)
        self.canvas.pack()

        self.update_background()

        self.text_widget = tk.Text(self, wrap=tk.WORD, bg=self.color, fg="black", font=("Arial", 12), bd=0)
        self.text_widget.place(x=10, y=10, width=180, height=160)

        self.color_button = tk.Button(self, text="色変更", command=self.change_color)
        self.color_button.place(x=10, y=175, width=50, height=20)

        self.close_button = tk.Button(self, text="閉じる", command=self.close)
        self.close_button.place(x=140, y=175, width=50, height=20)

    def update_background(self):
        self.background = Image.new("RGBA", (200, 200), self.color)
        self.background = ImageTk.PhotoImage(self.background)
        self.canvas.create_image(0, 0, anchor="nw", image=self.background)

    def change_color(self):
        color = colorchooser.askcolor(color=self.color)[1]
        if color:
            self.color = color
            self.update_background()
            self.text_widget.config(bg=self.color)

    def close(self):
        self.master.notes.remove(self)
        self.destroy()

    def setup_drag(self):
        self.bind("<ButtonPress-1>", self.start_drag)
        self.bind("<B1-Motion>", self.on_drag)

    def start_drag(self, event):
        self._drag_start_x = event.x
        self._drag_start_y = event.y

    def on_drag(self, event):
        x = self.winfo_x() - self._drag_start_x + event.x
        y = self.winfo_y() - self._drag_start_y + event.y
        self.geometry(f"+{x}+{y}")

    def get_data(self):
        return {
            "x": self.winfo_x(),
            "y": self.winfo_y(),
            "color": self.color,
            "text": self.text_widget.get("1.0", tk.END).strip()
        }

class StickyNoteApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sticky Note App")
        self.geometry("200x100")

        self.notes = []
        self.create_widgets()
        self.load_notes()

    def create_widgets(self):
        tk.Button(self, text="新規付箋", command=self.create_note).pack(pady=10)
        tk.Button(self, text="自動配列", command=self.auto_arrange).pack(pady=10)

    def create_note(self, x=None, y=None, color=None, text=""):
        if x is None or y is None:
            x = random.randint(0, self.winfo_screenwidth() - 200)
            y = random.randint(0, self.winfo_screenheight() - 200)
        if color is None:
            color = f"#{random.randint(0, 0xFFFFFF):06x}"
        note = StickyNote(self, x, y, color, text)
        self.notes.append(note)

    def auto_arrange(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        rows = int((len(self.notes) ** 0.5) // 1 + 1)
        cols = (len(self.notes) + rows - 1) // rows
        width = screen_width // cols
        height = screen_height // rows

        for i, note in enumerate(self.notes):
            row = i // cols
            col = i % cols
            x = col * width
            y = row * height
            note.geometry(f"+{x}+{y}")

    def save_notes(self):
        data = [note.get_data() for note in self.notes]
        with open("notes.json", "w") as f:
            json.dump(data, f)

    def load_notes(self):
        try:
            with open("notes.json", "r") as f:
                data = json.load(f)
            for note_data in data:
                self.create_note(
                    note_data.get("x", 100),
                    note_data.get("y", 100),
                    note_data.get("color", "#FFFF00"),
                    note_data.get("text", "")
                )
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print("Invalid JSON file. Starting with no notes.")
        except Exception as e:
            print(f"An error occurred while loading notes: {e}")

    def on_closing(self):
        self.save_notes()
        self.destroy()

if __name__ == "__main__":
    app = StickyNoteApp()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
