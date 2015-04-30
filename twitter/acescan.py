import twitter
import os
import json

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

print(json.dumps(world_trends, indent=1))
print(json.dumps(us_trends, indent=1))

world_trends_set = set([trend['name'] for trend in world_trends[0]['trends']])
us_trends_set = set([trend['name'] for trend in us_trends[0]['trends']])

common_trends = world_trends_set.intersection(us_trends_set)

print(common_trends)
