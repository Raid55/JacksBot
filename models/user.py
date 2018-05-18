#!/usr/bin/python
'''
    Defines the User class
'''
import uuid, os
from datetime import datetime
from sqlalchemy import Integer, String, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User:
    '''
        The user class which will instantiate a user with an id, timestamp, and 
        keywords string
    '''

    def __init__(self, *args, **kwargs):
        '''
            Instantiate a User object
        '''
        __tablename__ = 'users'
        user_id = Column(String(128), nullable=False)
        keywords = Column(String(256), nullable=False)
        auth_key = Column(String(128), nullable=False)
        consumer_key = Column(String(128), nullable=False)
        consumer_secret = Column(String(128), nullable=False)
        access_token_key = Column(String(128), nullable=False)
        access_token_secret = Column(String(128), nullable=False)
