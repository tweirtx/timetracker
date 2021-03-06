from timetracker import db, signer, add_users
import time


def run():
    add_users.add_user("test01", "Test01")
    add_users.add_user("test02", "Test02")
    time.sleep(1)
    with db.Session() as session:
        result = signer.sign("test01")
        #print(result)
        if result == "Successfully signed Test01 in" and session.query(db.Members).\
                filter_by(user_id='test01', signed_in=True).one_or_none():
            print("Sign-in test01 success")
        else:
            print("ERROR: Sign-in test01 failed!")
            exit(1)

    time.sleep(1)

    with db.Session() as session:
        result = signer.sign("test01")
        #print(result)
        time.sleep(1)
        query_result = session.query(db.Members).filter_by(user_id='test01', signed_in=False).one_or_none()
        #print(query_result)
        #print("test01 exists in DB: ", session.query(db.Members).filter_by(user_id='test01', signed_in=False).one_or_none())
        if result == "Successfully signed Test01 out" and query_result:
            print("Sign-out test01 success")
        else:
            print("ERROR: Sign-out test01 failed!")
            exit(1)

        time.sleep(1)

    signer.sign("test01")

    time.sleep(1)

    with db.Session() as session:
        result = signer.sign("test02")
        #print(result)
        if result == "Successfully signed Test02 in" and session.query(db.Members).\
                filter_by(user_id='test02', signed_in=True).one_or_none():
            print("Sign-in test02 success")
        else:
            print("ERROR: Sign-in test02 failed!")
            exit(1)

    time.sleep(1)

    with db.Session() as session:

        result = signer.sign("000000")
        #print(result)
        if result == "Successfully signed out 2 members!" and session.query(db.Members). \
                filter_by(user_id='test01', signed_in=False).one_or_none() and session.query(db.Members). \
                filter_by(user_id='test02', signed_in=False).one_or_none():
            print("Sign all out success")
        else:
            print("ERROR: Sign all out failed!")
            exit(1)
        print("Ending")
    print("Tests passed!")
