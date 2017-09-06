import tweepy
from credentialsBot1 import keys
from time import sleep

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q="#luxurybags").items():
    try:

        api.create_favorite(tweet.id)
        print("I liked @" + tweet.user.screen_name)
        tweet.user.follow()
        print("followed @" + tweet.user.screen_name)
        sleep(600)

    except tweepy.TweepError as e:
        print(e.reason)
        sleep(10)
