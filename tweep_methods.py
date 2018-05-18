#!/usr/bin/python3
from tweepy import OAuthHandler, API

consumer_key = 'WRi2oHuGFml3AHUH9J5FDCAws'
consumer_secret = 'fpLdAvU8PejMPWPkCyMrztj5npiQwNBq4q0pEsFwcGNT7OY8FN'
access_token_key = '2493721946-15B9t1SNUwugOF3uCdbfroJKJkuTyKj9J8uF3vN'
access_token_secret = 'q6NQMaEhNQn7jN2uckZ3pWF1DUHrXmrE2azePnlkU8bhv'
auth = OAuthHandler(consumer_key, consumer_secret)


def search_tweets(id, access_token_key, access_token_secret, keywords=[]):
    auth.set_access_token(access_token_key, access_token_secret)
    api = API(auth)
    tweets = api.search(q=keywords[0]) # just one keyword for now
    retweet = api.retweet(tweets[0].id)
    print(retweet.text.encode('utf-8'))

def get_retweets(id, access_token_key, access_token_secret):
    
search_tweets(0, access_token_key, access_token_secret, ['san francisco']) 
