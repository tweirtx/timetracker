from . import db
from . import web
from . import console
import argparse
import json


# db.db_init(config.['db_url'])


argparser = argparse.ArgumentParser()
argparser.add_argument("--web", help="Starts the web server instead of using console interaction.", action='store_true')
args = argparser.parse_args()
if args.web:
    web.start()
else:
    console.start()
