#!/usr/bin/env python3
# 2026/05/30 coded by chatgpt, and modified

import os
import shutil
import subprocess
import tkinter

WINDOW_TITLE = "pointer_ruler"

root = tkinter.Tk()
root.title( WINDOW_TITLE )
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

POWERSHELL_SCRIPT = r'''
Add-Type -Namespace Win32 -Name NativeMethods -MemberDefinition @"
    public delegate bool EnumWindowsProc(System.IntPtr hWnd, System.IntPtr lParam);

    [System.Runtime.InteropServices.DllImport("user32.dll")]
    public static extern bool EnumWindows(EnumWindowsProc lpEnumFunc, System.IntPtr lParam);

    [System.Runtime.InteropServices.DllImport("user32.dll", CharSet = System.Runtime.InteropServices.CharSet.Unicode)]
    public static extern int GetWindowText(System.IntPtr hWnd, System.Text.StringBuilder text, int count);

    [System.Runtime.InteropServices.DllImport("user32.dll")]
    public static extern bool SetWindowPos(System.IntPtr hWnd, System.IntPtr hWndInsertAfter, int x, int y, int cx, int cy, uint flags);
"@

$title = $env:POINTER_RULER_WINDOW_TITLE
$topMost = [System.IntPtr](-1)
$flags = 0x0001 -bor 0x0002 -bor 0x0010 -bor 0x0040
$callback = [Win32.NativeMethods+EnumWindowsProc]{
    param([System.IntPtr]$hWnd, [System.IntPtr]$lParam)

    $text = [System.Text.StringBuilder]::new(256)
    [void][Win32.NativeMethods]::GetWindowText($hWnd, $text, $text.Capacity)
    if ($text.ToString() -eq $title) {
        [void][Win32.NativeMethods]::SetWindowPos($hWnd, $topMost, 0, 0, 0, 0, $flags)
    }
    return $true
}
[void][Win32.NativeMethods]::EnumWindows($callback, [System.IntPtr]::Zero)
'''


def find_powershell():
    powershell = shutil.which( "powershell.exe" )
    if powershell is not None:
        return powershell

    powershell = "/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe"
    if os.path.exists( powershell ):
        return powershell

    return None


def raise_windows_window():
    powershell = find_powershell()
    if powershell is None:
        return

    env = os.environ.copy()
    env["POINTER_RULER_WINDOW_TITLE"] = WINDOW_TITLE
    try:
        subprocess.Popen(
            [
                powershell,
                "-WindowStyle",
                "Hidden",
                "-NoProfile",
                "-NonInteractive",
                "-Command",
                POWERSHELL_SCRIPT,
            ],
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except OSError:
        pass


def raise_window( focus=False ):
    root.lift()
    if focus:
        root.focus_force()
    root.attributes( "-topmost", False )
    root.attributes( "-topmost", True )
    raise_windows_window()

def button_press( event ):
    global mode, start_x, start_y, start_w, start_h

    raise_window( True )
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
root.after( 200, raise_window )
root.after( 1000, raise_window )
root.mainloop()
