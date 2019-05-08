from timetracker import db


def add_user(member_id, name):
    with db.Session() as session:
        session.add(db.Members(user_id=member_id, name=name))
        session.commit()


def run_console():
    while True:
        add_user(input("Please input the member ID to use: "), input("Please input the user's name: "))
