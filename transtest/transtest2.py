#!/usr/bin/env python3
# https://www.ishikawasekkei.com/index.php/2020/06/09/python-tkinter-gui-programing-transparent-canvas/

import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Transparent Canvas Challenge!")
        self.geometry("500x300")

        self.top = tk.Toplevel()
        self.top.wm_attributes("-topmost", True)
        self.top.overrideredirect(True)
        self.top.geometry("500x300")
        self.top.forward = tk.Canvas(self.top, background="white")
        self.top.forward.pack(fill=tk.BOTH, expand=True)
        self.top.forward.create_oval(50,50,450,250,fill="lightblue")
        self.top.wm_attributes("-transparentcolor", "white")
        
        self.back = tk.Canvas(self, background="white")
        self.back.pack(fill=tk.BOTH, expand=True)
        self.back.create_rectangle(50,50,450,250)
        self.back.create_rectangle(100,100,400,200)
        self.bind('<Configure>', self.change)
        self.back.bind("<Unmap>", self.unmap)
        self.back.bind("<Map>", self.map)
        self.bind("<1>", self.draw1)
        self.bind("<3>", self.draw3)
        self.top.bind("<1>", self.draw1)
        self.top.bind("<3>", self.draw3)
        
    def draw1(self, event):
        self.top.forward.create_oval(event.x, event.y, event.x + 30, event.y + 30)
        
    def draw3(self, event):
        self.back.create_rectangle(event.x, event.y, event.x + 30, event.y + 30)

    def unmap(self, event):
        self.top.withdraw()

    def map(self, event):
        self.lift()
        self.top.wm_deiconify()
        self.top.attributes("-topmost", True)
        
    def change(self, event):
        x, y = self.back.winfo_rootx(), self.back.winfo_rooty()
        w, h = self.winfo_width(), self.winfo_height()
        self.top.geometry(f"{w}x{h}+{x}+{y}")
        
if __name__ == "__main__":
    application = Application()
    application.mainloop()
