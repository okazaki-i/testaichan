#!/usr/bin/env python3
'''
  pointer_ruler.py

  マウスボタンで以下の動作をする。
  - Button1ドラッグ  移動させる
  - Shift+Button1ドラッグ  拡大縮小させる
  - Button2          終了する
  - Button3          ウィンドウマネージャによる修飾の有効無効化を切り替える(VcXsrv用)

  2026/05/30 coded by chatgpt, and modified a lot by okazaki,i
'''

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


def button_press2( event ):
    '''終了させる
    （VcXsrvだとウィンドウマネージャによる修飾を無効にしていると
    キーイベントを受け取れないようである）'''
    root.destroy()

def button_press3( event ):
    '''Button3押下をTk内で止める
    （押下中にwithdrawすると、VcXsrvがWindows側へ同じボタン押下を渡すことがある）'''
    return "break"


def toggle_decorations():
    '''ウィンドウマネージャによる装飾が無効であれば有効に、有効であれば無効にする'''
    root.overrideredirect( not root.overrideredirect() ) #True/Falseの状態を逆にする
    root.withdraw(); root.deiconify() #うまく再描画させるため


def button_release3( event ):
    '''Button3を離した後でウィンドウマネージャによる装飾を切り替える
    （VcXsrvでウィンドウが背面から最前面に変えられないときの処置として、
    いったん有効にして最前面にさせるために用意している）'''
    root.after_idle( toggle_decorations )
    return "break"


def button_press1( event ):
    global mode, start_x, start_y, start_w, start_h

    start_x = event.x_root; start_y = event.y_root
    start_w = root.winfo_width(); start_h = root.winfo_height()
    shift_pressed = bool( event.state & 0x0001 )
    if shift_pressed and event.x >= start_w - EDGE and event.y >= start_h - EDGE:
        mode = "resize_width_height"
    elif shift_pressed and event.x >= start_w - EDGE:
        mode = "resize_width"
    elif shift_pressed and event.y >= start_h - EDGE:
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

    elif mode == "resize_width_height":
        w = max( 20, start_w + dx )
        h = max( 5, start_h + dy )
        root.geometry( f"{w}x{h}" )

    elif mode == "resize_width":
        w = max( 20, start_w + dx )
        root.geometry( f"{w}x{root.winfo_height()}" )

    elif mode == "resize_height":
        h = max( 5, start_h + dy )
        root.geometry( f"{root.winfo_width()}x{h}" )

    #print( f"in motion: {root.winfo_width()}x{root.winfo_height()}+{root.winfo_x()}+{root.winfo_y()}" )


canvas.bind( "<Button-2>", button_press2 ) #終了
canvas.bind( "<Button-3>", button_press3 ) #Button3押下をTk内で止める
canvas.bind( "<ButtonRelease-3>", button_release3 ) #ウィンドウマネージャによる修飾の有効無効化
canvas.bind( "<Button-1>", button_press1 ) #移動、Shift押下時は拡大縮小
canvas.bind( "<B1-Motion>", motion )
root.mainloop()
