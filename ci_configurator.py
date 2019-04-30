import subprocess
import os
import json

config = {
    'db_url': 'sqlite:///timetracker.db',
    'signout_code': "000000",
    'minimum_hours': 0
}

if os.getenv("DB_TYPE") == "sqlite":
    print("Nothing to do!")
elif os.getenv("DB_TYPE") == "postgres":
    print("Configuring postgres")
    subprocess.call('sudo -u postgres psql "CREATE USER timetracker; CREATE DATABASE timetracker;"')
    config['db_url'] = "postgres://timetracker:timetracker@localhost/timetracker"
    print("postgres is configured")
elif os.getenv('DB_TYPE') == "mysql":
    print("Configuring mysql")
else:
    print("I can't handle this!")

with open('config.json', 'w') as f:
    f.write(json.dumps(config))
