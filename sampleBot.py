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

twts = api.search(q='#luxurybags').items(1)

for s in twts:
    sn = s.user.screen_name
    m = '@%s...looks like I stumbled upon a fellow porn lover!'
        'These girls will meet if you live close!...' + AFFILIATE_LINK % (sn)
    s = api.update_status(m, s.id)
    sleep(2)

for bag in twts:


    sleep(5)


for tweet in tweepy.Cursor(api.search,
                            q='#luxurybags').items(1):
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        tweet.user.follow()
        print("followed the user")

        #sn = tweet.user.screen_name
        #m = '@%s...We talkin pugs???' % (sn)
        #tweet = api.update_status(m)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break

#list of specific strings we want to check for in Tweets
#t = ['cheese',
#    'Cheese!',
#    'cheddar',
#    'mozzarella',
#    'Cheese',
#    'CHEESE!',
#    'CHEESE']

#x = ['Love Pugs',
#    'love Pugs',
#    'Love pugs',
#    'LOVE PUGS',
#    'love PUGS',
#    'LOVE pugs'
#]
#for i in x:
    #if x == s.text:
#for i in t:
#    if i == s.text: