import getpass
from .config import config
from .commands import runconsole


def start():
    while True:
        try:
            code = input("Please enter the user ID to sign in: ")
            if code == "su":
                password = getpass.getpass()
                if password == config['superuser_password']:
                    runconsole()
                else:
                    print("Incorrect password!")
        except KeyboardInterrupt:
            print("You must be superuser to do that!")
        except EOFError:
            print("You must be superuser to do that!")
