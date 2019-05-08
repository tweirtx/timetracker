from timetracker import web
from timetracker import console
from timetracker import test
from timetracker import add_users
import argparse


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--web", help="Starts the web server instead of using console interaction.", action='store_true')
    argparser.add_argument("--test", help="Runs the test suite", action='store_true')
    argparser.add_argument("--add-users", help="Start the user adding console", action='store_true')
    args = argparser.parse_args()
    if args.web:
        web.start()
    elif args.test:
        test.run()
    elif args.add_users:
        add_users.run_console()
    else:
        console.start()


if __name__ == '__main__':
    main()
