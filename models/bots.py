'''
    Sets the timer for querying the database and making retweets
'''
from sched import scheduler
import time
from models.storage import DBStorag
from models.tweep_methods import search_tweets


# Open Database
db = DBStorage()
db.reload()

# Set scheduler to query user data and send tweets
schedule = scheduler(time.time, time.sleep)
schedule.enter(3600, 1, main_entry)
schedule.run()
    
def main_entry():
    ''' Initiates everything based on timer '''
    users = db.query_active_users()

    for user in users:
        keywords = user.keywords.replace('|', ' ').split()
        search_tweets(user.access_token_key, user.access_token_secret, keywords)

    db.close()

    return schedule.queue
