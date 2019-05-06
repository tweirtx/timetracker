# Multi-client mode
If you are interested in running multiple sign-in/out instances, you must set up integration to
an external database. PostgreSQL, MySQL, and Microsoft SQL Server are officially tested and
supported. Other database systems that SQLAlchemy supports may work, but are not officially
supported/tested by TimeTracker and not guaranteed to work.

## Modify the config file
Open TimeTracker's `config.json` and modify the database URL according to your DB backend's schema.
See below for details.

## PostgreSQL
Setup is extremely easy for postgres. Open a psql shell and run the following commands:
```
CREATE DATABASE timetracker;
CREATE USER timetracker PASSWORD 'timetracker';
```
The db_url schema for postgres is as follows: ```postgres://user:password@host_ip_or_domain/db_name```.
So assuming you use the defaults provided by my instructions, your URL would be 
```postgres://timetracker:timetracker@host_ip_or_domain/timetracker```.

## MySQL
Open a mysql shell and run the following commands:
```
CREATE DATABASE IF NOT EXISTS timetracking;
USE timetracking;
CREATE USER timetracker IDENTIFIED BY 'timetracker';
GRANT ALL ON timetracking.students TO timetracker;
GRANT ALL ON timetracking.verboselogs TO timetracker;
```
The db_url schema for postgres is as follows: ```mysql://user:password@host_ip_or_domain/db_name```.
So assuming you use the defaults provided by my instructions, your URL would be 
```mysql://timetracker:timetracker@host_ip_or_domain/timetracking```.

## Microsoft SQL Server
I'll write this up once I download the petabyte of SQL Server tools.