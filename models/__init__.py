'''
    Package initializer
'''

from models.database import DBStorage
from models.user import User, Base
# creating db session
storage = DBStorage()
# creating db file and table if not alredy created
storage.reload()
