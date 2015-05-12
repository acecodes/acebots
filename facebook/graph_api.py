from __future__ import print_function
from prettytable import PrettyTable
from collections import Counter
from operator import itemgetter

import facebook
import requests
import json
import os
import networkx as nx

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

    # num_likes_by_friend = {friend: len(likes[friend]) for friend in likes}

    # pt = PrettyTable(field_names=['Friend', 'Number of Likes'])
    # pt.align['Friend'], pt.align['Number of Likes'] = 'l', 'r'
    # [pt.add_row(nlbf)
    #  for nlbf in sorted(num_likes_by_friend.items(),
    #                     key=itemgetter(1),
    #                     reverse=True)]

    # print('Number of likes per friend')
    # print(pt)

    # Likes in common with friends
    # my_likes = [like['name'] for like in graph.get_connections('me', 'likes')['data']]

    # pt = PrettyTable(field_names=['Name'])
    # pt.align = 'l'
    # [pt.add_row((ml,)) for ml in my_likes]
    # print('\nMy likes')
    # print(pt)

    # friends_likes = Counter([like['name']
    #                      for friend in likes
    #                        for like in likes[friend]
    #                            if like.get('name')])

    # common_likes = list(set(my_likes) & set(friends_likes))

    # pt2 = PrettyTable(field_names=['Name'])
    # pt2.align = 'l'
    # [pt2.add_row((cl,)) for cl in common_likes]
    # print('\nMy common likes with friends')
    # print(pt2)

    # Construct graph of mutual friends with NetworkX
    # friends = [(friend['id'], friend['name'],)
    #            for friend in graph.get_connections('me', 'friends')['data']]

    # url = 'https://graph.facebook.com/me/mutualfriends/%s?access_token=%s'

    # mutual_friends = {}

    # # May take a while, as this spawns a new request for each iteration
    # for friend_id, friend_name in friends:
    #     r = requests.get(url % (friend_id, ACCESS_TOKEN,))
    #     response_data = json.loads(r.content)['data']
    #     mutual_friends[friend_name] = [data['name'] for data in response_data]

    # nxg = nx.Graph()

    # [nxg.add_edge('me', mf) for mf in mutual_friends]
    # [nxg.add_edge(f1, f2) for f1 in mutual_friends for f2 in mutual_friends[f1]]

    # print(nxg)

    # Find cliques (graph theory cliques, not actual cliques) in mutual friendships
    nxg = nx.Graph()
    cliques = [c for c in nx.find_cliques(nxg)]

    num_cliques = len(cliques)

    clique_sizes = [len(c) for c in cliques]
    max_clique_size = max(clique_sizes)
    avg_clique_size = sum(clique_sizes) / num_cliques

    max_cliques = [c for c in cliques if len(c) == max_clique_size]

    num_max_cliques = len(max_cliques)

    max_clique_sets = [set(c) for c in max_cliques]
    friends_in_all_max_cliques = list(reduce(lambda x, y: x.intersection(y),
                                      max_clique_sets))
