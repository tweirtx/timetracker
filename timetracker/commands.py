import datetime
import smtplib
from . import add_users
from .config import config
from .db import *
from . import signer
from . import web


def report():
    for config_item in config.keys():
        if "email" in config_item:
            if "CHANGEME" in config[config_item]:
                print("Email not configured!")
                return
    emailer = smtplib.SMTP(host=config['email_from_server'])
    emailer.ehlo()
    emailer.starttls()
    emailer.login(config['email_from_address'], config['email_from_password'])
    msg = smtplib.email.message.EmailMessage()
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload("<html>\n" + web.report() + "\n</html>")
    msg['subject'] = "TimeTracker Report " + str(datetime.date.today())
    msg['From'] = f"TimeTracker <{config['email_from_address']}>"
    emailer.send_message(msg, to_addrs=[config['email_to_address']])
    print("Email sent!")


def signout():
    count = 0
    with Session() as session:
        members = session.query(Members).filter_by(signed_in=True)
        for mem in members:
            print(signer.sign(mem.user_id))
            count += 1
    return "Successfully signed out {} members!".format(count)


def edit():
    with Session() as session:
        user = input("Please enter the user ID you would like to edit: ")
        result = session.query(Members).filter_by(user_id=user).one_or_none()
        if result is None:
            print("That user ID does not exist!")
            return
        else:
            action = input("Please type the editing mode you would like to use. "
                           "You may choose add, subtract, or absolute: ")
            if action == "add":
                amount = int(input("Please input the number of minutes you would like to add to their time: "))
                result.minutes += amount
            elif action == "subtract":
                amount = int(input("Please input the number of minutes you would like to subtract from their time: "))
                result.minutes -= amount
            elif action == "absolute":
                amount = int(input("Please input the number of minutes you would like to set their time to: "))
                result.minutes = amount
            else:
                print("Invalid mode specifier!")
                return
    print("Edit successfully saved!")


def exitme():
    exit(0)


def check():
    with Session() as session:
        user = input("Please enter the user ID you would like to check: ")
        result = session.query(Members).filter_by(user_id=user).one_or_none()
        if result is None:
            print("That user ID does not exist!")
            return
        else:
            hours = result.minutes / 60
            print(f"{result.name} has {hours} hours on record!")


available_commands = {'signout': signout, 'adduser': add_users.run_console, 'edit': edit,
                      'return': "call break later", 'exit': exitme, 'autoreport': report, 'check': check}
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
