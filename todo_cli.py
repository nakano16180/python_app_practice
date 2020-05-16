#!/usr/bin/env python3
import fire
import sys, os
import datetime
from pathlib import Path


class Todo_cli:

    _FILENAME = "./data.txt"

    def _divide_dict_key(self, dict_data, depth):
        if isinstance(dict_data, dict):
            for key in dict_data.keys():
                print(depth*"    "+str(key)+" : ")
                if isinstance(dict_data[key], dict):
                    self._divide_dict_key(dict_data[key], int(depth)+1)
                elif isinstance(dict_data[key], list):
                    if isinstance(dict_data[key][0], dict):
                        self._divide_dict_key(dict_data[key][0], int(depth)+1)
                else:
                    print((depth+1)*"    "+str(dict_data[key]))


    #Todo 新規作成・読み込み
    def _read_task(self):
        Contents = []
        if os.path.exists(self._FILENAME):
            with open(self._FILENAME, "r") as file:
                lines = file.readline()
                while lines:
                    Contents.append(lines.strip("\n"))
                    lines = file.readline()
            return Contents
        else:
            print("make file")
            Path(self._FILENAME).touch()
            return Contents

    def todo_add(self):
        todo = input("todo: ")
        deadline = input("deadline: ")
        created = datetime.datetime.now()

        record = {"todo": todo, "deadline": deadline, "createdAt": created}
        
        print(" ")
        self._divide_dict_key(record, 0)
        print(" ")
        isOK = input("OK? y/n: ")
        if isOK == "y":
            print("create record\n")
            with open(self._FILENAME, "a") as f:
                f.write(str(record)+"\n")
        else:
            print("please try again\n")
        
    def todo_list(self):
        for task in self._read_task():
            self._divide_dict_key(eval(task), 0)
            print('----------------------------------')

    def todo_done(self, todo):
        data = Path(self._FILENAME)
        data.unlink()
        Path(self._FILENAME).touch()
        for td in self._read_task():
            td2 = eval(td)
            if todo == td2["todo"]: 
                print("done task:", todo)
            else:
                with open(self._FILENAME, "a") as f:
                    f.write(str(td2)+"\n")



if __name__ == '__main__':
    fire.Fire(Todo_cli)