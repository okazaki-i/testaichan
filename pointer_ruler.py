#!/usr/bin/env python3
# 2026/05/30 coded by chatgpt, and modified

import tkinter

root = tkinter.Tk()
root.overrideredirect( True )  #ウィンドウマネージャによる装飾を無効
root.attributes( "-topmost", True )  #常に最前面に表示、VcXsrvだとWindowsアプリの下から出ない
root.attributes( "-alpha", 0.2 )  #ウィンドウの透明度、機能しない

EDGE = 15
start_w = 100
start_h = 200
root.geometry( f"100x200+500-500" )  #初期配置と大きさ
canvas = tkinter.Canvas( root, bg="red", highlightthickness=0, bd=0 )
canvas.pack( fill="both", expand=True )

mode = None; start_x = 0; start_y = 0

def raise_window():
    root.lift()
    root.focus_force()
    root.attributes( "-topmost", False )
    root.attributes( "-topmost", True )

def button_press( event ):
    global mode, start_x, start_y, start_w, start_h

    raise_window()
    start_x = event.x_root; start_y = event.y_root
    start_w = root.winfo_width(); start_h = root.winfo_height()
    if event.x >= start_w - EDGE:
        mode = "resize_width"
    elif event.y >= start_h - EDGE:
        mode = "resize_height"
    else:
        mode = "move"


def motion( event ):
    global start_x, start_y

    dx = event.x_root - start_x; dy = event.y_root - start_y
    if mode == "move":
        x = root.winfo_x() + dx; y = root.winfo_y() + dy
        root.geometry( f"+{x}+{y}" )
        start_x = event.x_root; start_y = event.y_root

    elif mode == "resize_width":
        w = max( 20, start_w + dx )
        root.geometry( f"{w}x{root.winfo_height()}" )

    elif mode == "resize_height":
        h = max( 5, start_h + dy )
        root.geometry( f"{root.winfo_width()}x{h}" )


canvas.bind( "<Button-1>", button_press )
canvas.bind( "<B1-Motion>", motion )
root.bind( "q", lambda e: root.destroy() )
root.mainloop()
