import requests
import json
import os

"""Nope!"""
ACCESS_TOKEN = os.environ.get('FACEBOOK_TOKEN')

base_url = 'https://graph.facebook.com/me'

# 10 likes for 10 friends query
fields = 'id,name,friends.limit(10).fields(likes.limit(10))'

url = '%s?fields=%s&access_token=%s' % (base_url, fields, ACCESS_TOKEN)
content = requests.get(url).json()

print(json.dumps(content, indent=1))
