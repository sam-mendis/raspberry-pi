import sys
import os

from tkinter import *

root = Tk()


def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)


frame_s = Frame(root)
frame_s.grid()


inputlabel = Label(frame_s, text="Manual Input",
                   font=" Times 16", width=14, bd=1, relief="solid")
inputlabel.grid(row=0, column=0, columnspan=2)
templabel = Label(
    frame_s, text="Temp/\N{DEGREE SIGN}C", font=" Times 12", width=7, height=1)
templabel.grid(row=2, column=1)

e_temp = Entry(frame_s, font=" Times 12", width=7, bd=1, relief="solid")
e_temp.grid(row=3, column=1)
restart = Button(frame_s, text="Restart", command=restart)
restart.grid(row=4)

root.mainloop()
