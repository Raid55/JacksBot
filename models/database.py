'''
   Create a timed query of database
'''
# import time, os, flask
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlite3 import dbapi2 as sqlite
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from models.user import User, Base


class DBStorage:
    ''' Read from and write to DB '''
    __engine = None
    __session = None

    def __init__(self):
        '''
            DBStorage Contructor 
        '''
        self.__engine = create_engine(
        "sqlite+pysqlite:///jacksbot.db",
        native_datetime=True,
        module=sqlite,
        pool_pre_ping=True, echo=False)

    def query_active_users(self):
        '''
            Retrieve all user objects from db
        '''
        res = [o for o in self.__session.query(User).filter(
                User.is_active == 1
        )]
        if res:
            return [{
		        'twit_user_name': u.user_name,
		        'twit_user_id': u.user_id,
		        'access_token_key': u.access_token_key,
		        'access_token_secret': u.access_token_secret,
		        'keywords': u.keywords.split('|')
            } for u in res ]
        else:
            return None



    def add_user(self, obj):
        '''
            Add new User to database
        '''
        self.__session.add(obj)
        self.__session.commit()


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
