import os
import shutil
from pathlib import Path
import datetime
import pprint

# 1. argparseをインポート
import argparse

# 2. パーサを作る
parser = argparse.ArgumentParser(description='このプログラムの説明（なくてもよい）')

# 3. parser.add_argumentで受け取る引数を追加していく
# 必須の引数を追加
parser.add_argument('arg1', help='この引数の説明（なくてもよい）')
parser.add_argument('arg2', help='foooo')

# オプション引数（指定しなくても良い引数）を追加
parser.add_argument('--arg3')

parser.add_argument('--test', help='run test')


# よく使う引数なら省略形があると使う時に便利
parser.add_argument('-a', '--arg4')

parser.add_argument('-i', '--input', help='input file')
parser.add_argument('-d', '--dir', help='input dir')

parser.add_argument('-o', '--output', help='output dir')
parser.add_argument('-rm', '--remove', help='remove file')


def check_dir(path):
    temp = path.split('/') 

    if not temp[-1] == '':
        temp.append('')

    return '/'.join(temp)


def create_template_file(dir_path):
    os.makedirs(dir_path, exist_ok=True)
    date = datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S')
    print(date)
    print("target: ", dir_path + date + '.txt')

    shutil.copyfile("./template/temp.txt", dir_path + date + '.txt')

def remove_dir(dir_path):
    shutil.rmtree(dir_path)


################################################################################
# 4. 引数を解析
args = parser.parse_args()

if args.arg1 :
    print('arg1: ', args.arg1)
if args.arg2 :
    print('arg2: ', args.arg2)
if args.arg3 :
    print('arg3: ', args.arg3)
if args.arg4 :
    print('arg4: ', args.arg4)

if args.input:
    print('input: ', args.input)

if args.dir:
    print('input: ', args.dir)

if args.output:
    print(args.output)
    path = check_dir(args.output)
    create_template_file("test/template2/")
