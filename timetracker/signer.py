from .config import config
from .db import *


def sign(user_id):
    return user_id + " detected"  # Will say signed in/signed out once that function actually works
