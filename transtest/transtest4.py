#!/usr/bin/env python3
# https://tech-branch.9999ch.com/archives/857

from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x300")
root.config(bg="white")
root.attributes("-transparentcolor", "white")

s = ttk.Style()
s.configure('Frame1.TFrame', background='red')
content = ttk.Frame(root, padding=(3,3,12,12))
name = ttk.Entry(content)
content.grid(column=0, row=0, sticky=(N, S, E, W), pady=0, padx=0)
name.grid(column=0, row=1, sticky=(N, S, E, W), pady=0, padx=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=1000)
content.columnconfigure(1, weight=1)
content.columnconfigure(2, weight=1)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)
