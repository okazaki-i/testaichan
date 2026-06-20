#!/usr/bin/env python3
# http://maetec.co.jp/maetec2/tk_p0004-18.html

import tkinter as tk
root = tk.Tk()
root.geometry('300x200+100+100')
labelframe = tk.LabelFrame(root, bg='yellow',
        text='labelframe', labelanchor='n')
labelframe.place(x=0, y=0, width=200, height=150)
labelframe_0 = tk.LabelFrame(root, bg='pink',
        text='labelframe_0', labelanchor='n',
        container=True)
labelframe_0.place(x=20, y=20, width=200, height=160)
sub = tk.Toplevel(root, bg='red', use=labelframe_0.winfo_id())
labelframe_1 = tk.LabelFrame(sub, bg='green',
        text='labelframe_1', labelanchor='n')
labelframe_1.place(x=20, y=20, width=100, height=100)
root.update()
#sub.wm_attributes('-transparentcolor', 'green')  #windows版tkの機能らしい
sub.overrideredirect(True)  #linuxでの代替（全体半透明）？ VcXsrvでは機能しない
sub.wm_attributes('-alpha', 0.8)
root.wm_deiconify()
root.mainloop()
