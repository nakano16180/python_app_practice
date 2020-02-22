## Python App Practice

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