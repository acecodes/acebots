import json

"""
Sample data: global trends from 4/29/2015 @ 5:43 PM
"""

sample_trend_data = [{'locations': [{'woeid': 1, 'name': 'Worldwide'}], 'trends': [{'query': '%22Gran+Hermano%22', 'name': 'Gran Hermano', 'promoted_content': None, 'url': 'http://twitter.com/search?q=%22Gran+Hermano%22'}, {'query': '%23%D9%85%D8%B5%D8%B7%D9%84%D8%AD%D8%A7%D8%AA_%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D9%87_%D9%84%D8%A7%D8%AA%D8%AC%D8%AF%D9%87%D8%A7_%D8%A8%D8%A7%D9%84%D8%B9%D8%A7%D9%84%D9%85', 'name': '#مصطلحات_سعوديه_لاتجدها_بالعالم', 'promoted_content': None, 'url': 'http://twitter.com/search?q=%23%D9%85%D8%B5%D8%B7%D9%84%D8%AD%D8%A7%D8%AA_%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D9%87_%D9%84%D8%A7%D8%AA%D8%AC%D8%AF%D9%87%D8%A7_%D8%A8%D8%A7%D9%84%D8%B9%D8%A7%D9%84%D9%85'}, {'query': '%23BatallasLaVoz', 'name': '#BatallasLaVoz', 'promoted_content': None, 'url': 'http://twitter.com/search?q=%23BatallasLaVoz'}, {'query': '%23%D9%84%D9%88_%D8%A7%D9%84%D9%82%D8%AA%D9%84_%D8%AD%D9%84%D8%A7%D9%84_%D9%83%D9%86%D8%AA_%D9%82%D8%AA%D9%84%D8%AA', 'name': '#لو_القتل_حلال_كنت_قتلت', 'promoted_content': None, 'url': 'http://twitter.com/search?q=%23%D9%84%D9%88_%D8%A7%D9%84%D9%82%D8%AA%D9%84_%D8%AD%D9%84%D8%A7%D9%84_%D9%83%D9%86%D8%AA_%D9%82%D8%AA%D9%84%D8%AA'}, {'query': 'Paran%C3%A1', 'name': 'Paraná', 'promoted_content': None, 'url': 'http://twitter.com/search?q=Paran%C3%A1'}, {'query': '%23GoodbyeRevenge', 'name': '#GoodbyeRevenge', 'promoted_content': None, 'url': 'http://twitter.com/search?q=%23GoodbyeRevenge'}, {'query': '%23MeChamullaronCon', 'name': '#MeChamullaronCon', 'promoted_content': None, 'url': 'http://twitter.com/search?q=%23MeChamullaronCon'}, {'query': 'MahomiesAreExcitedForDirtyWork', 'name': 'MahomiesAreExcitedForDirtyWork', 'promoted_content': None, 'url': 'http://twitter.com/search?q=MahomiesAreExcitedForDirtyWork'}, {'query': '%22Nigel+Pearson%22', 'name': 'Nigel Pearson', 'promoted_content': None, 'url': 'http://twitter.com/search?q=%22Nigel+Pearson%22'}, {'query': '%22Union+Square%22', 'name': 'Union Square', 'promoted_content': None, 'url': 'http://twitter.com/search?q=%22Union+Square%22'}], 'created_at': '2015-04-30T00:34:38Z', 'as_of': '2015-04-30T00:39:24Z'}]


"""
Sample data: First item in #FlyNavy search results from 4/29/2015 @ 6:00 PM
"""

sample_search_result_data = {
 "in_reply_to_user_id": 'null',
 "truncated": 'false',
 "favorite_count": 0,
 "created_at": "Wed Apr 29 20:55:28 +0000 2015",
 "text": "What's it like to cat 6Gs off a carrier? Find out in \u2605\u2605\u2605\u2605\u2605SOLO VIETNAM #mustread http://t.co/HNw6PZtB4Z #veterans #flynavy",
 "in_reply_to_screen_name": 'null',
 "retweet_count": 0,
 "geo": 'null',
 "in_reply_to_status_id_str": 'null',
 "contributors": 'null',
 "coordinates": 'null',
 "possibly_sensitive": 'false',
 "place": 'null',
 "id_str": "593518987931029504",
 "id": 593518987931029504,
 "favorited": 'false',
 "in_reply_to_user_id_str": 'null',
 "retweeted": 'false',
 "source": "<a href=\"http://www.hootsuite.com\" rel=\"nofollow\">Hootsuite</a>",
 "in_reply_to_status_id": 'null',
 "user": {
  "notifications": 'false',
  "profile_background_color": "C0DEED",
  "contributors_enabled": 'false',
  "profile_location": 'null',
  "location": "Dallas, Texas",
  "profile_link_color": "0084B4",
  "created_at": "Sat May 12 15:33:48 +0000 2012",
  "protected": 'false',
  "is_translator": 'false',
  "url": "http://t.co/cQSRxUDdHM",
  "default_profile_image": 'false',
  "geo_enabled": 'false',
  "profile_text_color": "333333",
  "followers_count": 3374,
  "name": "Jeanette Vaughan",
  "profile_image_url_https": "https://pbs.twimg.com/profile_images/378800000528689962/1eb6e7072407fdc6ac906b16ae7995bc_normal.jpeg",
  "profile_image_url": "http://pbs.twimg.com/profile_images/378800000528689962/1eb6e7072407fdc6ac906b16ae7995bc_normal.jpeg",
  "default_profile": 'false',
  "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/612326783/7rhu1zikunexf2qugrd9.png",
  "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/612326783/7rhu1zikunexf2qugrd9.png",
  "friends_count": 3668,
  "listed_count": 127,
  "favourites_count": 5,
  "profile_sidebar_border_color": "C0DEED",
  "id_str": "578157367",
  "is_translation_enabled": 'false',
  "id": 578157367,
  "statuses_count": 18541,
  "profile_use_background_image": 'true',
  "verified": 'false',
  "description": "Salacious babybooming writer of award winning FLYING SOLO #trilogy. #NOLA fan, foodie, wine lover, nurse and sheep farmer! #flynavy http://t.co/VbMUaNeiFa",
  "profile_background_tile": 'true',
  "profile_sidebar_fill_color": "DDEEF6",
  "utc_offset": -18000,
  "follow_request_sent": 'false',
  "screen_name": "VaughanJeanette",
  "profile_banner_url": "https://pbs.twimg.com/profile_banners/578157367/1412660633",
  "entities": {
   "description": {
    "urls": [
     {
      "display_url": "amzn.to/VzXMJq",
      "expanded_url": "http://amzn.to/VzXMJq",
      "indices": [
       132,
       154
      ],
      "url": "http://t.co/VbMUaNeiFa"
     }
    ]
   },
   "url": {
    "urls": [
     {
      "display_url": "jeanettevaughan.com",
      "expanded_url": "http://www.jeanettevaughan.com",
      "indices": [
       0,
       22
      ],
      "url": "http://t.co/cQSRxUDdHM"
     }
    ]
   }
  },
  "time_zone": "Mexico City",
  "following": 'false',
  "lang": "en"
 },
 "entities": {
  "hashtags": [
   {
    "text": "mustread",
    "indices": [
     71,
     80
    ]
   },
   {
    "text": "veterans",
    "indices": [
     104,
     113
    ]
   },
   {
    "text": "flynavy",
    "indices": [
     114,
     122
    ]
   }
  ],
  "user_mentions": [],
  "urls": [
   {
    "display_url": "amzn.to/13yngWm",
    "expanded_url": "http://amzn.to/13yngWm",
    "indices": [
     81,
     103
    ],
    "url": "http://t.co/HNw6PZtB4Z"
   }
  ],
  "symbols": []
 },
 "metadata": {
  "iso_language_code": "en",
  "result_type": "recent"
 },
 "lang": "en"
}

print('\nTweets are accessed via the "text" key:')
print(sample_search_result_data['text'], '\n')

print('This tweet was retweeted {} times.'.format(
    sample_search_result_data['retweet_count']))

print('Was this retweeted by the author?',
      sample_search_result_data['retweeted'])
