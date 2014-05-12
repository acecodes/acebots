#! /usr/bin/python
import praw

user_agent = ('KarmaBreakdownBot version 1.0')
reddit = praw.Reddit(user_agent=user_agent)

# User to scan
username = 'Unidan' # Everyone's favorite biologist!
user = reddit.get_redditor(username)

# Item limit per request
thing_limit = 50
submission_generator = user.get_submitted(limit=thing_limit)

# Result dictionary
subs_karma = {}

for thing in submission_generator:
	subreddit = thing.subreddit.display_name
	subs_karma[subreddit] = (subs_karma.get(subreddit, 0) + thing.score)


if __name__ == '__main__':
	print('Karma breakdown for %s:' % (user))
	for items in sorted(subs_karma):
		print('%s | %i' % (items, subs_karma[items]))