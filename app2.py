#!/usr/bin/env python3

import sys
import tkinter as tk
import tkinter.messagebox

root = tk.Tk()
root.title("Software Title")
root.geometry("400x300")

Label_list = []
Check_list = []
CheckVal = []
n = 0

def DeleteEntryValue(event):
    EditBox.delete(0, tk.END)

def check(event):
    for i in range(len(CheckVal)):
        if CheckVal[i].get() == True:
            label = tk.Label(text="項目1はチェックされています\n")
            label.place(x=100, y=20*i+50)
        else:
            label = tk.Label(text="項目1はチェックされていません\n")
            label.place(x=100, y=20*i+50)

        Label_list.append(label)

def make_box(event):
    global n
    content = EditBox.get()
    
    b1 = tk.BooleanVar()
    b1.set(False)

    b = tk.Checkbutton(text=content, variable=b1)
    b.place(x=5, y=20*n+50)
    n += 1

    CheckVal.append(b1)
    Check_list.append(b)


Button1 = tk.Button(root, text="make button", width=20)
Button1.bind("<Button-1>", make_box)
Button1.place(x=90, y=5)

Button2 = tk.Button(root, text="get check ", width=15)
Button2.bind("<Button-1>", check)
Button2.place(x=265, y=5)

EditBox = tk.Entry(root, width=10)
EditBox.place(x=5, y=5)

root.mainloop()