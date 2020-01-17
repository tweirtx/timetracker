# Multi-client mode
If you are interested in running multiple sign-in/out instances, you must set up integration to
an external database. PostgreSQL, MySQL, and Microsoft SQL Server are officially tested and
supported. Other database systems that SQLAlchemy supports may work, but are not officially
supported/tested by TimeTracker and not guaranteed to work.

PostgreSQL is the recommended database system if you want to get started with multi-station support but have no
existing DB infrastructure.

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
This is by far the most complex to set up, however people may choose to do so.

* Open Microsoft SQL Server Management Studio and connect to your SQL Server instance you wish to use.
* Create a new database called timetracker. You can leave the options as default.
* Create a new login (under the Security section) called timetracker. Check SQL Server authentication and set the 
password to timetracker (or of your choosing, however you must update the connection string). Be sure to uncheck 
 Enforce Password Policy.
* Expand the database you created and right click on Security. Click on New User and enter timetracker in the login name section.
* Right click on the timetracker database and click Properties. Click on Permissions and then click on the
timetracker user. Grant the Alter and Create Table permissions.

The db_url schema for postgres is as follows: ```mssql+pymssql://user:password@host_ip_or_domain/db_name```.
So assuming you use the defaults provided by my instructions, your URL would be 
```"mssql+pyobdc://timetracker:timetracker@localhost/timetracker?driver=SQL+Server"```.
