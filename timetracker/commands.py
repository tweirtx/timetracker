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
