from .config import config
from .commands import signout
from .db import *
import datetime


def sign(user_id):
    if user_id == config['superuser_password']:
        signout()
    with Session() as session:
        mem = session.query(Members).filter_by(user_id=user_id).one_or_none()
        if not mem:
            return "Error: Member not found"
        elif mem.signed_in:
            mem.minutes += ((datetime.datetime.now().timestamp() - mem.sign_in_time.timestamp()) / 60)
            mem.sign_in_time = None
            mem.signed_in = False
            session.add(VerboseLogs(user_id=mem.user_id, signing_in=False, current_datetime=datetime.datetime.now()))
            session.commit()
            return "Successfully signed {} out".format(mem.name)
        elif not mem.signed_in:
            mem.sign_in_time = datetime.datetime.now()
            mem.signed_in = True
            session.add(VerboseLogs(user_id=mem.user_id, signing_in=True, current_datetime=datetime.datetime.now()))
            session.commit()
            return "Successfully signed {} in".format(mem.name)

    return user_id + " detected"  # Will say signed in/signed out once that function actually works
