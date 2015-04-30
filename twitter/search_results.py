import twitter
import os
import json

"""Nope!"""
CONSUMER_KEY = os.environ.get('TWIT_CON_KEY')
CONSUMER_SECRET = os.environ.get('TWIT_CON_SECRET')
OAUTH_TOKEN = os.environ.get('TWIT_O_TOKEN')
OAUTH_TOKEN_SECRET = os.environ.get('TWIT_O_SECRET')

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

query = "#FlyNavy"

count = 100

search_results = twitter_api.search.tweets(q=query, count=count)

statuses = search_results['statuses']

for _ in range(5):
    print('Length of statuses', len(statuses))
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError:
        break

    kwargs = dict([kv.split('=') for kv in next_results[1:].split('&')])
    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']

print(json.dumps(statuses[0], indent=1))
