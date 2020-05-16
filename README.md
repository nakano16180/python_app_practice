## Python App Practice

### use virtualenv

```
$ cd python_app_practice/
$ pipenv install
```
### app3.py
sample for tkinter

```
$ pipenv run python3 app3.py
```
### crud.py
basic crud app

```
$ python3 crud.py
```
### custom_cmd.py
example for argumentparser

```
$ pipenv run python3 custom_cmd.py input.txt output.txt
```
### doc_manage.py

```
$ mkdir template/
$ echo 'This is template' > temp.txt

$ pipenv run python3 doc_manage.py
```

### todo_cli.py
タスクを追加
```
$ pipenv run python3 todo_cli.py todo_add
```
タスクを表示
```
$ pipenv run python3 todo_cli.py todo_list
```
タスク完了
```
$ pipenv run python3 todo_cli.py todo_done task
```