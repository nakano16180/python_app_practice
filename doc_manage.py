import pprint
import datetime
import os
import shutil

def read_data(data_path):
    if not os.path.exists(data_path):
        print("Can't read data. please check data name.")
    else:
        with open(data_path, "r") as file:
            data = file.readlines()
            pprint.pprint(data)
            return data

def read_tag(data):
    for data_line in data:
        if '### ' in data_line:
            print('tag3', data_line)
        elif '## ' in data_line:
            print('tag2', data_line)
        elif '# ' in data_line:
            print('tag1', data_line)

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