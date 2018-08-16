#!/usr/bin/env python3
import sys, os
import datetime
import tkinter as tk
import tkinter.messagebox

n = 0
TodoDB = {}
data_dir = "Todo"
fileName = "data.csv"

def read_task():
    data_dir = "Todo"
    fileName = "data.csv"

    if os.path.exists(data_dir):
        with open(data_dir +"/"+ fileName, "r") as file:
            lines = file.readline()
            while lines:
                time, title, contents = lines.split(',')
                record = {
                    'time'   : time,
                    'title'  : title,
                    'contents'   :  contents.strip()
                }
                TodoDB[time] = TodoDB.get(time, []) + [record]
                lines = file.readline()

    else:
        print("make file")
        os.makedirs(data_dir)
        with open(data_dir +"/"+ fileName, "w") as file:
            now = datetime.datetime.now()
            first_title = "new file"
            first_content = "make new file for the first time"
            data = ','.join([now.isoformat(),first_title,first_content])
            file.write(data+'\n')

def disp_task():
    global n
    b1 = tk.BooleanVar()
    b1.set(False)

    for time in sorted(TodoDB):
        task = TodoDB[time][0]
        content = task["contents"]
        b = tk.Checkbutton(text=content, variable=b1)
        b.place(x=5, y=20*n+50)
        n += 1


def make_box(event):
    global n
    content = EditBox.get()
    
    b1 = tk.BooleanVar()
    b1.set(False)

    b = tk.Checkbutton(text=content, variable=b1)
    b.place(x=5, y=20*n+50)
    n += 1

    with open(data_dir +"/"+ fileName, "a") as file:
        now = datetime.datetime.now()
        file_title = "add file"
        file_contents = content
        data = ','.join([now.isoformat(), file_title, file_contents])
        file.write(data+'\n')
        file.close()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Software Title")
    root.geometry("400x300")

# read task data ###################################################
    read_task()
    disp_task()
####################################################################

    Button1 = tk.Button(root, text="make button", width=20)
    Button1.bind("<Button-1>", make_box)
    Button1.place(x=90, y=5)

    EditBox = tk.Entry(root, width=10)
    EditBox.place(x=5, y=5)

    root.mainloop()