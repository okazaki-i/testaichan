#!/usr/bin/env python3
# 2026/05/30 coded by chatgpt, and modified

import tkinter

EDGE = 15
START_GEOMETRY = "100x200+500-500"

root = tkinter.Tk()
root.withdraw()
window = None
canvas = None
mode = None; start_x = 0; start_y = 0; start_w = 100; start_h = 200


def create_window( geometry ):
    global window, canvas

    window = tkinter.Toplevel( root )
    window.overrideredirect( True )  #ウィンドウマネージャによる装飾を無効
    window.attributes( "-topmost", True )  #常に最前面に表示、VcXsrvだとWindowsアプリの下から出ない
    window.attributes( "-alpha", 0.2 )  #ウィンドウの透明度、機能しない
    window.geometry( geometry )  #初期配置と大きさ

    canvas = tkinter.Canvas( window, bg="red", highlightthickness=0, bd=0 )
    canvas.pack( fill="both", expand=True )
    canvas.bind( "<Button-1>", button_press )
    canvas.bind( "<B1-Motion>", motion )
    window.bind( "q", lambda e: root.destroy() )
    window.lift()
    window.focus_force()


def recreate_window():
    global window

    geometry = START_GEOMETRY
    if window is not None:
        geometry = window.geometry()
        window.destroy()

    create_window( geometry )


def button_press( event ):
    global mode, start_x, start_y, start_w, start_h

    start_x = event.x_root; start_y = event.y_root
    start_w = window.winfo_width(); start_h = window.winfo_height()
    if event.x >= start_w - EDGE:
        mode = "resize_width"
    elif event.y >= start_h - EDGE:
        mode = "resize_height"
    else:
        mode = "move"

    recreate_window()


def motion( event ):
    global start_x, start_y

    dx = event.x_root - start_x; dy = event.y_root - start_y
    if mode == "move":
        x = window.winfo_x() + dx; y = window.winfo_y() + dy
        window.geometry( f"+{x}+{y}" )
        start_x = event.x_root; start_y = event.y_root

    elif mode == "resize_width":
        w = max( 20, start_w + dx )
        window.geometry( f"{w}x{window.winfo_height()}" )

    elif mode == "resize_height":
        h = max( 5, start_h + dy )
        window.geometry( f"{window.winfo_width()}x{h}" )


create_window( START_GEOMETRY )
root.mainloop()
