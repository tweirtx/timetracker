from . import db, signer
import time


def run():
    with db.Session() as session:

        session.add(db.Members(user_id="test01", name="Test01"))
        session.add(db.Members(user_id="test02", name="Test02"))
        session.commit()

        time.sleep(1)

        if signer.sign("test01") == "Successfully signed Test01 in" and session.query(db.Members).\
                filter_by(user_id='test01', signed_in=True).one_or_none():
            print("Sign-in test01 success")
        else:
            print("ERROR: Sign-in test01 failed!")
            exit(1)

        time.sleep(1)

        if signer.sign("test01") == "Successfully signed Test01 out" and session.query(db.Members).\
                filter_by(user_id='test01', signed_in=0).one_or_none():
            print("Sign-out test01 success")
        elif signer.sign("test01") == "Successfully signed Test01 out" and session.query(db.Members).\
                filter_by(user_id='test01', signed_in=False).one_or_none():
            print("Sign-out test01 success")
        else:
            print("ERROR: Sign-out test01 failed!")
            exit(1)

        time.sleep(1)

        signer.sign("test01")

        time.sleep(1)

        if signer.sign("test02") == "Successfully signed Test02 in" and session.query(db.Members).\
                filter_by(user_id='test02', signed_in=True).one_or_none():
            print("Sign-in test02 success")
        else:
            print("ERROR: Sign-in test02 failed!")
            exit(1)

        time.sleep(1)

        if signer.sign("000000") == "Successfully signed out 2 members!" and session.query(db.Members). \
                filter_by(user_id='test01', signed_in=False).one_or_none() and session.query(db.Members). \
                filter_by(user_id='test02', signed_in=False).one_or_none():
            print("Sign all out success")
        else:
            print("ERROR: Sign all out failed!")
            exit(1)
    print("Tests passed!")
