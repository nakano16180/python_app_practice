#!/usr/bin/env python3
import sys, os
import datetime
import tkinter as tk
from tkinter import messagebox 

n = 0
before = 0
add_count = 0
TodoDB = {}
Todo_Contents = []
data_dir = "Todo"
fileName = "data.csv"

new_contents = {}
Check_list = []
CheckVal = []


def read_task():
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
                Todo_Contents.append(contents.strip())
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

    Todo_Contents.remove(Todo_Contents[0])

def disp_task():
    global n

    for i in range(len(Todo_Contents)):
        task = Todo_Contents[i]
        
        b1 = tk.BooleanVar()
        b1.set(False)

        b = tk.Checkbutton(text=task, variable=b1)
        b.place(x=5, y=20*i+50)
        n += 1

        CheckVal.append(b1)
        Check_list.append(b)
    
def add_task(event):
    global add_count, Check_list, CheckVal, Todo_Contents
    content = EditBox.get()
    Todo_Contents.append(content)
    
    t_key = datetime.datetime.now()
    new_contents[t_key] = content
    
    add_count += 1

    for i in range(len(Check_list)):    
        Check_list[i].destroy()
        
    Check_list = []
    CheckVal = []
    disp_task()

def save_task():
    with open(data_dir +"/"+ fileName, "a") as file:
        for key in sorted(new_contents.keys()):
            now = key
            file_title = "add file"
            file_contents = new_contents[key]
            data = ','.join([now.isoformat(), file_title, file_contents])
            file.write(data+'\n')

def check_delete(event):
    global Check_list, CheckVal
    new_count = 0
    res = messagebox.askquestion(title='delete', message='削除しますか')
    if res == 'yes':
        for i in range(len(CheckVal)):
            if CheckVal[i].get() == False:
                Todo_Contents.append(Todo_Contents[i])
                new_count += 1
        for i in range(len(Check_list)):
            Todo_Contents.remove(Todo_Contents[0])
            Check_list[i].destroy()
        
        Check_list = []
        CheckVal = []
        disp_task()        


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Todo")
    root.geometry("400x300")

# read task data ###################################################
    read_task()
    disp_task()
    before = n
####################################################################
    EditBox = tk.Entry(root, width=10)
    EditBox.place(x=5, y=5)

    Button1 = tk.Button(root, text="add task", width=20)
    Button1.bind("<Button-1>", add_task)
    Button1.place(x=90, y=5)

    Button2 = tk.Button(root, text="delete", width=15)
    Button2.bind("<Button-1>", check_delete)
    Button2.place(x=265, y=5)

    root.mainloop()
    save_task()
    
    if(0 < add_count):
        print("add following task to list")
        for key in sorted(new_contents.keys()):
            print (new_contents[key])
    