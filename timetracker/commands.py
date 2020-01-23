import smtplib
from . import add_users
from .db import *
from .signer import sign


def report():
    print("fridge")


def signout():
    count = 0
    with Session() as session:
        members = session.query(Members).filter_by(signed_in=True)
        for mem in members:
            print(sign(mem.user_id))
            count += 1
    return "Successfully signed out {} members!".format(count)


def edit():
    print("asdf")


def exitme():
    exit(0)


def runconsole():
    print("Superuser mode entered!")
    available_commands = {'signout': signout, 'adduser': add_users.run_console, 'edit': edit,
                          'return': return "Superuser exited", 'exit': exitme, 'autoreport': report}
