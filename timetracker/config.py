
import os
import json

config = {
    'db_url': 'sqlite:///timetracker.db',
    'superuser_password': "000000",
    'minimum_hours': 0,
    "email_to_address": "CHANGEME",
    "email_from_address": "CHANGEME",
    "email_from_server": "CHANGEME",
    "email_from_password": "NOTASECRET"
}
config_file = 'config.json'

if os.path.isfile(config_file):
    with open(config_file) as f:
        config.update(json.load(f))

if config.get("signout_code"):
    config['superuser_password'] = config.get("signout_code")
    print("Notice: config updated automatically!")
    config.pop("signout_code")

with open('config.json', 'w') as f:
    json.dump(config, f, indent='\t')
