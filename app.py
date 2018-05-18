#!/usr/bin/python3
'''
Module for API for website majoidea.holberton.us
'''
import os
from flask_oauth import OAuth
from flask import Flask, request, jsonify, redirect, url_for, abort, session, g, flash, render_template, make_response
from flask_oauth import OAuth

# configuration
SECRET_KEY = 'development key'
DEBUG = True
host = '0.0.0.0'
port = 5000

# start up app 
app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()

# setting up twitter auth
twitter = oauth.remote_app('twitter',
    base_url='https://api.twitter.com/1.1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',

    consumer_key=os.getenv('KEY'),
    consumer_secret=os.getenv('SECRET')
)
 

@twitter.tokengetter
def get_twitter_token(token=None):
    if session.has_key('twitter_token'):
        del session['twitter_token']
    return session.get('twitter_token')

@app.route('/')
def index():
    access_token = session.get('access_token')
    print(access_token, "HERE")
    if access_token is None:
        return redirect(url_for('login'))

    access_token = access_token[0]
 
    return render_template('index.html')
 

@app.route('/login')
def login():
    print(url_for('auth',
        next=request.args.get('next') or request.referrer or None))
    return twitter.authorize(callback=url_for('auth',
        next=request.args.get('next') or request.referrer or None))

@app.route('/logout')
def logout():
    session.pop('screen_name', None)
    flash('You were signed out')
    return redirect(request.referrer or url_for('index'))

@app.route('/auth')
@twitter.authorized_handler
def auth(res):
    next_url = request.args.get('next') or url_for('index')
    if res is None:
        flash('You denied the request to sign in.')
        return redirect(next_url)

    print("res: ", res)
    print("session: ", session)
    access_token = res['oauth_token']
    session['access_token'] = access_token
    session['screen_name'] = res['screen_name']

    session['twitter_token'] = (
        res['oauth_token'],
        res['oauth_token_secret']
    )

    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    '''
    Method to be called if the page does not exist
    '''
    return make_response(jsonify({"error": "Page not found"}), 404)

@app.route('/status', strict_slashes=False)
def status():
    '''
    Method to ensure the status of the website deployment
    '''

    return jsonify({"status":"OK"})


if __name__ == '__main__':
    app.run(host=host, port=port)
