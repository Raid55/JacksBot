'''
    Sets the timer for querying the database and making retweets
'''
from sched import scheduler
import time
from models.storage import DBStorage
from models.tweep_methods import search_tweets


# Open Database
db = DBStorage()
db.reload()

while True:
    main_entry()
    time.sleep(3600)
    
def main_entry():
    ''' Initiates everything based on timer '''
    users = db.query_active_users()

    for user in users:
        search_tweets(user.access_token_key, user.access_token_secret, user.keywords)

    db.close()

    return schedule.queue
