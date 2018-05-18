'''
    Sets the timer for querying the database and making retweets
'''
import time
from models import storage as db
import random
import tweepy

consumer_key = 'WRi2oHuGFml3AHUH9J5FDCAws'
consumer_secret = 'fpLdAvU8PejMPWPkCyMrztj5npiQwNBq4q0pEsFwcGNT7OY8FN'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

def search_tweets(access_token_key, access_token_secret, keywords):
    auth.set_access_token(access_token_key, access_token_secret)
    api = tweepy.API(auth)
    tweets = api.search(q=keywords[0]) # just one keyword for now
    retweet = api.retweet(tweets[random.randint(0,15)].id)

while True:
    users = db.query_active_users()
    try:
        for user in users:
            search_tweets(user.get('access_token_key'), user.get('access_token_secret'), user.get('keywords'))
    except tweepy.error.TweepError:
        pass
    time.sleep(69)
