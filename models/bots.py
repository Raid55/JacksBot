#!/usr/bin/python
'''
   Create a timed query of database
'''
from sched import scheduler
import time, os, flask
from sqlite3 import dbapi2 as sqlite
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from models.user import User, Base


''' Instantiates the scheduler '''
timer = scheduler(time.time, time.sleep)

'''Set the timed query for every hour from instantiation and start timer '''
timer.enter(3600, 1, ''' NEED TO ENTER FUNCTION ''')
timer.run()

class DBStorage:
    ''' Read from and write to DB '''
    __engine = None
    __session = None

    def __init__(self):
        '''
            DBStorage Contructor 
        '''
        self.__engine = create_engine(
        ‘sqlite+pysqlite:///jacksbot.db’,
        native_datetime=True,
        module=sqlite,
        pool_pre_ping=True, echo=False)

def query_users(self, user_ids=[]):
    '''
        Retrieve all user objects from db
    '''


def add_user(self, obj):
    '''
        Add new User to database
    '''
    self.__session.add(obj)
    self.__session.commit()

def delete(self, obj=None):
    '''
        Delete User from db
    '''
    if obj:
        self.__session.delete(obj)

def reload(self):
    '''
        Create the db session
    '''
    Base.metadata.create_all(self.__engine)
    session_maker = sessionmaker(
        bind=self.__engine,
        expire_on_commit=False
    )
    self.__session = scoped_session(session_maker)

def close(self):
    '''
        Close the db session
    '''
    self.__session.close()