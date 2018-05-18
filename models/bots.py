'''
    Sets the timer for querying the database and making retweets
'''
import time
from models.storage import DBStorage
import random
import tweepy
from models.storage import DBStorage


consumer_key = 'WRi2oHuGFml3AHUH9J5FDCAws'
consumer_secret = 'fpLdAvU8PejMPWPkCyMrztj5npiQwNBq4q0pEsFwcGNT7OY8FN'
access_token_key = '2493721946-15B9t1SNUwugOF3uCdbfroJKJkuTyKj9J8uF3vN'
access_token_secret = 'q6NQMaEhNQn7jN2uckZ3pWF1DUHrXmrE2azePnlkU8bhv'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = API(auth)


while True:
    # Open Database
    db = DBStorage()
    db.reload()
    try:
        search_tweets(0, access_token_key, access_token_secret, ['holberton'])
    except tweepy.error.TweepError:
        pass
    time.sleep(3600)


def main_entry():
    ''' Initiates everything based on timer '''
    users = db.query_active_users()
    for user in users:
        search_tweets(user.get('access_token_key'), user.get('access_token_secret'), user.get('keywords'))
    tweets = api.search(q=keywords[0]) # just one keyword for now
    retweet = api.retweet(tweets[random.randint(0,15)].id)
    db.close()