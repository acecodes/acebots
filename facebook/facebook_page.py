from __future__ import print_function
import facebook
import requests
import json
import os

"""Nope!"""
ACCESS_TOKEN = os.environ.get('FACEBOOK_TOKEN')

graph = facebook.GraphAPI(ACCESS_TOKEN)


def prettyprint(object):
    print(json.dumps(object, indent=1))

"""Graph API interaction the Mining the Social Web site"""
mtsw_id = '146803958708175'

if __name__ == '__main__':
    prettyprint(graph.get_object(mtsw_id))
