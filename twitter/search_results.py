import twitter
import os
import json
from collections import Counter
from prettytable import PrettyTable
from matplotlib import pyplot as plt

"""Nope!"""
CONSUMER_KEY = os.environ.get('TWIT_CON_KEY')
CONSUMER_SECRET = os.environ.get('TWIT_CON_SECRET')
OAUTH_TOKEN = os.environ.get('TWIT_O_TOKEN')
OAUTH_TOKEN_SECRET = os.environ.get('TWIT_O_SECRET')

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

query = "#Syria"

count = 100

search_results = twitter_api.search.tweets(q=query, count=count)

statuses = search_results['statuses']


def lexical_diversity(tokens):
    """Checks lexical diversity of input text"""
    return 1.0 * len(set(tokens)) / len(tokens)


def average_words(statuses):
    """Check average words in statuses"""
    total_words = sum([len(s.split()) for s in statuses])
    return 1.0 * total_words / len(statuses)

if __name__ == '__main__':
    # for _ in range(5):
    #     print('Length of statuses', len(statuses))
    #     try:
    #         next_results = search_results['search_metadata']['next_results']
    #     except KeyError:
    #         break

    #     kwargs = dict([kv.split('=') for kv in next_results[1:].split('&')])
    #     search_results = twitter_api.search.tweets(**kwargs)
    #     statuses += search_results['statuses']

    # print(json.dumps(statuses[0], indent=1))
    status_texts = [status['text'] for status in statuses]

    screen_names = [user_mention['screen_name']
                    for status in statuses for user_mention in status['entities']['user_mentions']]

    # Next two are lower-case to normalize the results
    hash_tags = [hashtag['text'].lower()
                 for status in statuses for hashtag in status['entities']['hashtags']]
    words = [w.lower() for t in status_texts for w in t.split()]

    # print('Sample data sets:')
    # print(json.dumps(status_texts[0:5], indent=1))
    # print(json.dumps(screen_names[0:5], indent=1))
    # print(json.dumps(hash_tags[0:5], indent=1))
    # print(json.dumps(words[0:5], indent=1))

    print('\nFrequency distributions:')

    for label, data in (('Word', words),
                        ('Screen Name', screen_names),
                        ('Hash tag', hash_tags)):
        # Text table
        pt = PrettyTable(field_names=[label, 'Count'])
        c = Counter(data)
        [pt.add_row(kv) for kv in c.most_common()[:10]]
        pt.align[label], pt.align['Count'] = 'l', 'r'  # Column alignment
        print(pt)

    print('\nLexical diversity')
    print('Words:', lexical_diversity(words))
    print('Screen names:', lexical_diversity(screen_names))
    print('Hash tags:', lexical_diversity(hash_tags))
    print('\nAverage words')
    print(average_words(status_texts))

    print('\nRetweets')
    retweets = [
        (status['retweet_count'],
         status['retweeted_status']['user']['screen_name'],
         status['text'])
        for status in statuses if 'retweeted_status' in status
    ]

    pt = PrettyTable(field_names=['Count', 'Scren Name', 'Text'])
    [pt.add_row(row) for row in sorted(retweets, reverse=True)[:5]]
    pt.max_width['Text'] = 50
    pt.align = 'l'
    print(pt)

    word_counts = sorted(Counter(words).values(), reverse=True)

    # Word count graph
    # plt.loglog(word_counts)
    # plt.ylabel('Frequency')
    # plt.xlabel('Word Rank')
    # plt.show()

    # Retweet histogram
    counts = [count for count, _, _ in retweets]
    plt.hist(counts)
    plt.title('Retweets')
    plt.xlabel('Bins (number of retweets)')
    plt.ylabel('Number of tweets in bin')

    plt.show()
