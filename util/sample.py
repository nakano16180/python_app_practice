from pathlib import Path
import shutil
import os

def delete_dir(dir_path):
    shutil.rmtree(dir_path)

def create_dir(dir_name, file_name):
    ## parents=Trueとして、親ディレクトリがない場合は同時に作成
    Path(dir_name).mkdir(parents=True, exist_ok=True)
    Path(dir_name + file_name).touch()

def create_dir2(dir_name):
    if os.path.exists(dir_name):
        delete_dir(dir_name)
    os.makedirs(dir_name)


create_dir("test/test2/", "test.txt")
create_dir("test/test2/test3/", "test2.txt")
os.makedirs("test/test2/test")

def move_dir(in_dir, out_dir):
    if os.path.exists(out_dir):
        delete_dir(out_dir)
    shutil.move(in_dir, out_dir)

if input("continue? [y/n]:") == "y":
    move_dir("test/test2/", "test/test3/")