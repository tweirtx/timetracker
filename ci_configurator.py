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
    config['db_url'] = "postgres://timetracker:timetracker@localhost/timetracker"
elif os.getenv('DB_TYPE') == "mysql":
    print("Configuring mysql")
    config['db_url'] = "mysql://timetracker:timetracker@localhost/timetracker"
else:
    print("I can't handle this!")


with open('config.json', 'w') as f:
    f.write(json.dumps(config))
