"""Provides database storage"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session, sessionmaker
from .config import config

__all__ = ['Session', 'Column', 'Integer', 'String', 'ForeignKey', 'relationship', 'Boolean',
           'DateTime', 'DatabaseObject', 'Members', 'VerboseLogs']


class CtxSession(Session):
    """Allows sessions to be used as context managers and asynchronous context managers."""
    def __enter__(self):
        return self

    async def __aenter__(self):
        return self

    def __exit__(self, err_type, err, tb):
        if err_type is None:
            self.commit()
        else:
            self.rollback()
        return False

    async def __aexit__(self, err_type, err, tb):
        return self.__exit__(err_type, err, tb)


DatabaseObject = None


def db_init(db_url):
    """Initializes the database connection"""
    global Session
    global DatabaseObject
    engine = sqlalchemy.create_engine(db_url)
    DatabaseObject = declarative_base(bind=engine, name='DatabaseObject')
    DatabaseObject.__table_args__ = {'extend_existing': True}  # allow use of the reload command with db cogs
    Session = sessionmaker(bind=engine, class_=CtxSession)


db_init(config['db_url'])


class Members(DatabaseObject):
    __tablename__ = 'students'
    student_id = Column(String, primary_key=True)
    name = Column(String)
    signed_in = Column(Boolean, default=False)
    sign_in_time = Column(DateTime, nullable=True)
    minutes = Column(Integer, default=0)


class VerboseLogs(DatabaseObject):
    __tablename__ = 'verboselogs'
    student_id = Column(String, primary_key=True)
    signing_in = Column(Boolean, primary_key=True)
    current_datetime = Column(DateTime, primary_key=True)


DatabaseObject.metadata.create_all()
