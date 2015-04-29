import twitter
import os

"""
Code used in conjunction with
Mining the Social Web book
"""

"""Nope!"""
CONSUMER_KEY = os.environ.get('TWIT_CON_KEY')
CONSUMER_SECRET = os.environ.get('TWIT_CON_SECRET')
OAUTH_TOKEN = os.environ.get('TWIT_O_TOKEN')
OAUTH_TOKEN_SECRET = os.environ.get('TWIT_O_SECRET')

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

for trends in world_trends['trends']:
    print(trends['name'])
