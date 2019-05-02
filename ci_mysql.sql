CREATE DATABASE IF NOT EXISTS timetracking;
USE timetracking;
CREATE USER timetracker IDENTIFIED BY 'timetracker';
GRANT ALL ON timetracking.students TO timetracker;
GRANT ALL ON timetracking.verboselogs TO timetracker;