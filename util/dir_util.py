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

def move_dir(dir1, out_dir):
    shutil.move(dir1, out_dir)


def makedir_path_by_time():
    # y/m/d/h-m-s.txt
    date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    date = date.split(' ')

    dir_path = date[0]
    file_name = '-'.join(date[1].split(':'))
    return dir_path, file_name
