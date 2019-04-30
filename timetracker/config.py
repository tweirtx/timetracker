
import os
import json

config = {
    'db_url': 'sqlite:///timetracker.db',
    'signout_code': 0,
    'minimum_hours': 0
}
config_file = 'config.json'

if os.path.isfile(config_file):
    with open(config_file) as f:
        config.update(json.load(f))


with open('config.json', 'w') as f:
    json.dump(config, f, indent='\t')
