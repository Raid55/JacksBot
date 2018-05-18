#!/usr/bin/python
'''
    Defines the User class
'''
import uuid, os
from datetime import datetime
from sqlalchemy import Integer, String, Column, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    '''
        The user class which will instantiate a user with an id, timestamp, and 
        keywords string
    '''
    __tablename__ = 'users'
    user_id = Column(String(128), nullable=False, primary_key=True)
    user_name = Column(String(224), nullable=False)
    keywords = Column(Text, nullable=False)
    access_token_key = Column(String(128), nullable=False)
    access_token_secret = Column(String(128), nullable=False)
    is_active = Column(Integer, nullable=False)
    total_rt = Column(Integer, nullable=True)
