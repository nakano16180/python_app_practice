from datetime import datetime
from pathlib import Path
import shutil
import os

def create_dir(dir_name, file_name):
    ## parents=Trueとして、親ディレクトリがない場合は同時に作成
    Path(dir_name).mkdir(parents=True, exist_ok=True)
    Path(dir_name + file_name).touch()

def delete_dir(dir_path):
    shutil.rmtree(dir_path)

def clear_dir(dir_path):
    shutil.rmtree(dir_path)
    os.mkdir(dir_path)

def move_dir(in_dir, out_dir):
    if os.path.exists(out_dir):
        delete_dir(out_dir)
    shutil.move(in_dir, out_dir)


def makedir_path_by_time():
    # y/m/d/h-m-s.txt
    date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    date = date.split(' ')

    dir_path = date[0]
    file_name = '-'.join(date[1].split(':'))
    return dir_path, file_name

if __name__ == "__main__" :
    create_dir("test/test2/", "test.txt")
    create_dir("test/test2/test3/", "test2.txt")
    os.makedirs("test/test2/test")

    if input("continue? [y/n]:") == "y":
        move_dir("test/test2/", "test/test3/")