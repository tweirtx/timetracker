from .config import config
from .db import *
import datetime


def sign(user_id):
    if user_id == config['signout_code']:
        count = 0
        with Session() as session:
            members = session.query(Members).filter_by(signed_in=True)
            for mem in members:
                print(sign(mem.user_id))
                count += 1
        return "Successfully signed out {} members!".format(count)
    with Session() as session:
        mem = session.query(Members).filter_by(user_id=user_id).one_or_none()
        if not mem:
            return "Error: Member not found"
        if mem.signed_in:
            mem.minutes += ((datetime.datetime.now().timestamp() - mem.sign_in_time.timestamp()) / 60)
            mem.sign_in_time = None
            mem.signed_in = False
            session.commit()
            return "Successfully signed {} out".format(mem.name)
        if not mem.signed_in:
            mem.sign_in_time = datetime.datetime.now()
            mem.signed_in = True
            session.commit()
            return "Successfully signed {} in".format(mem.name)

    return user_id + " detected"  # Will say signed in/signed out once that function actually works
