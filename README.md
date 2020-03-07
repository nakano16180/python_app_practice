## Python App Practice

### use virtualenv

```
$ cd python_app_practice/
$ virtualenv -p python3.6 .venv
$ source .venv/bin/activate
```

### python_db.py

#### setup
1. create database

```
$ docker run -v /var/lib/psql --name psql_data busybox
$ docker run --volumes-from psql_data --name psql -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres:9.6

$ docker exec -it psql bash
```

```
# psql -h localhost -U postgres

postgres=# create database pydb_practice;
postgres=# \q

# exit
```

2. python setup

```
$ pip3 install psycopg2
```

#### run

```
$ docker start psql
$ python3 python_db.py

$ docker stop psql
```

### sqlite_practice.py

```
$ mkdir database
$ python3 sqlite_practice.py
```
### crud.py
basic crud app

```
$ python3 crud.py
```
### custom_cmd.py
example for argumentparser

```
$ python3 custom_cmd.py input.txt output.txt
```
### doc_manage.py

```
$ mkdir template/
$ echo 'This is template' > temp.txt

$ python3 doc_manage.py
```