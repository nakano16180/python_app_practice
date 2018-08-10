#!/usr/bin/env python3

import sys
import tkinter as tk
import tkinter.messagebox

root = tk.Tk()
root.title("Software Title")
root.geometry("400x300")

def DeleteEntryValue(event):
    EditBox.delete(0, tk.END)

def check(event):
    global Val
    text = ""
    
    if Val.get() == True:
        text += "項目1はチェックされています\n"
    else:
        text += "項目1はチェックされていません\n"

    tk.messagebox.showinfo('info', text)

EditBox = tk.Entry(width=50)
EditBox.insert(tk.END, "test")
EditBox.pack()

Button = tk.Button(text="check", width=50)
Button.bind("<Button-1>", check)
Button.pack()

Val = tk.BooleanVar()
Val.set(True)

CheckBox = tk.Checkbutton(text="項目１", variable=Val)
CheckBox.pack()

root.mainloop()