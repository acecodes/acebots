from __future__ import print_function
from prettytable import PrettyTable
from collections import Counter
from operator import itemgetter

import facebook
import requests
import json
import os

"""Nope!"""
ACCESS_TOKEN = os.environ.get('FACEBOOK_TOKEN')


def prettyprint(object):
    print(json.dumps(object, indent=1))

graph = facebook.GraphAPI(ACCESS_TOKEN)
lines = '-' * 10

if __name__ == '__main__':
    """Use requests"""
    # base_url = 'https://graph.facebook.com/me'

    # 10 likes for 10 friends query
    # fields = 'id,name,friends.limit(10).fields(likes.limit(10))'

    # url = '%s?fields=%s&access_token=%s' % (base_url, fields, ACCESS_TOKEN)
    # content = requests.get(url).json()

    # print(json.dumps(content, indent=1))

    """
    Use Facebook-sdk package
    NOTE: This requires switching to a Python 2 environment
    (As of May 2015)
    """

    # print(lines)
    # print('Me')
    # print(lines)
    # prettyprint(graph.get_object('me'))
    # print()

    # print(lines)
    # print('Friends')
    # print(lines)
    # prettyprint(graph.get_connections('me', 'friends'))
    # print()

    # print(lines)
    # print('Social web')
    # print(lines)
    # prettyprint(graph.request('search', {'q': 'social web', 'type': 'page'}))

    # Explore likes from my social network

    friends = graph.get_connections('me', 'friends')['data']
    likes = {friend['name']: graph.get_connections(friend['id'], 'likes')['data']
             for friend in friends}

    # print(likes)

    # Analyze and count frequency of friend likes

    # Specific likes
    # friends_likes = Counter([like['name']
    #                          for friend in likes
    #                            for like in likes[friend]
    #                                if like.get('name')])

    # pt = PrettyTable(field_names=['Name', 'Frequency'])
    # pt.align['Name'], pt.align['Frequency'] = 'l', 'r'

    # [pt.add_row(fl) for fl in friends_likes.most_common(10)]

    # Like categories

    # friends_likes_categories = Counter([like['category']
    #                                     for friend in likes
    #                                     for like in likes[friend]])

    # pt = PrettyTable(field_names=['Category', 'Frequency'])
    # pt.align['Category'], pt.align['Frequency'] = 'l', 'r'

    # [pt.add_row(flc) for flc in friends_likes_categories.most_common(10)]

    # print('\nTop 10 likes amongst friends')
    # print(pt)

    # Number of likes per friend

    num_likes_by_friend = {friend: len(likes[friend]) for friend in likes}

    pt = PrettyTable(field_names=['Friend', 'Number of Likes'])
    pt.align['Friend'], pt.align['Number of Likes'] = 'l', 'r'
    [pt.add_row(nlbf)
     for nlbf in sorted(num_likes_by_friend.items(),
                        key=itemgetter(1),
                        reverse=True)]

    print('Number of likes per friend')
    print(pt)
