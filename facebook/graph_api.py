from __future__ import print_function
import facebook
import requests
import json
import os

"""Nope!"""
ACCESS_TOKEN = os.environ.get('FACEBOOK_TOKEN')


if __name__ == '__main__':
    """Use requests"""
    # base_url = 'https://graph.facebook.com/me'

    # # 10 likes for 10 friends query
    # fields = 'id,name,friends.limit(10).fields(likes.limit(10))'

    # url = '%s?fields=%s&access_token=%s' % (base_url, fields, ACCESS_TOKEN)
    # content = requests.get(url).json()

    # print(json.dumps(content, indent=1))

    """
    Use Facebook-sdk package
    NOTE: This requires switching to a Python 2 environment
    (As of May 2015)
    """

    def prettyprint(object):
        print(json.dumps(object, indent=1))

    graph = facebook.GraphAPI(ACCESS_TOKEN)
    lines = '-' * 10

    print(lines)
    print('Me')
    print(lines)
    prettyprint(graph.get_object('me'))
    print()

    print(lines)
    print('Friends')
    print(lines)
    prettyprint(graph.get_connections('me', 'friends'))
    print()

    print(lines)
    print('Social web')
    print(lines)
    prettyprint(graph.request('search', {'q': 'social web', 'type': 'page'}))
