from . import web
from . import console
from . import test
import argparse


argparser = argparse.ArgumentParser()
argparser.add_argument("--web", help="Starts the web server instead of using console interaction.", action='store_true')
argparser.add_argument("--test", help="Runs the test suite", action='store_true')
args = argparser.parse_args()
if args.web:
    web.start()
elif args.test:
    test.run()
else:
    console.start()
