CREATE DATABASE timetracking;
USE timetracking;
CREATE USER timetracker IDENTIFIED BY 'timetracker';
GRANT ALL ON timetracking TO timetracker;