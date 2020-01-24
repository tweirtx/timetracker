import getpass
from .config import config
from .commands import runconsole
from . import signer


def start():
    while True:
        try:
            user = input("Please enter the user ID to sign in: ")
            if user == "su":
                password = getpass.getpass()
                if password == config['superuser_password']:
                    runconsole()
                else:
                    print("Incorrect password!")
            else:
                print(signer.sign(user))
        except KeyboardInterrupt:
            print("You must be superuser to do that!")
        except EOFError:
            print("You must be superuser to do that!")
