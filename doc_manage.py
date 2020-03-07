import pprint
import datetime
import os
import shutil


def new_document():
    date = datetime.datetime.now().strftime('%Y-%m-%d %H%M%S')
    print(date)

    doc_dir = date.split(' ')[0]
    doc_file = date.split(' ')[1]

    dir_path = '/'.join(doc_dir.split('-'))
    print("doc_dir: ", dir_path)
    print("dock_file: ", doc_file)
    
    os.makedirs(dir_path, exist_ok=True)
    shutil.copyfile("./template/temp.txt", dir_path + '/' + doc_file + '.txt')

if __name__ == "__main__":
    print("CLI tools for Document")
    new_document()