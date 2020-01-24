import smtplib
from . import add_users
from .db import *
from . import signer


def report():
    print("fridge")


def signout():
    count = 0
    with Session() as session:
        members = session.query(Members).filter_by(signed_in=True)
        for mem in members:
            print(signer.sign(mem.user_id))
            count += 1
    return "Successfully signed out {} members!".format(count)


def edit():
    print("asdf")


def exitme():
    exit(0)


available_commands = {'signout': signout, 'adduser': add_users.run_console, 'edit': edit,
                      'return': "call break later", 'exit': exitme, 'autoreport': report}
command_string = "Available commands: \n"
for command_name in available_commands.keys():
    command_string += command_name + "\n"


def runconsole():
    print("Superuser mode entered!")
    while True:
        print(command_string)
        command = input("Please enter your chosen command: ")
        if command == "return":
            break
        try:
            available_commands[command]()
        except KeyError:
            print("Invalid command!")
        print("\n")
