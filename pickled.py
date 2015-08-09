#!/usr/bin/python

import twitter
import pickle
import time



# Twitter API keys go here
CONSUMER_KEY = 'X35pBx2WqXUxZdY4Z6hu5X4ey'
CONSUMER_SECRET = 'nzB47ZcVKcyeaQPyjey9JS8D48Ciio2Hppoj71qeBIHcIjqZ7N'

OAUTH_TOKEN = '2165157360-MobIczcZ14ZbEwsFqmP2TvQv8IFnvkXogAbE8j2'
OAUTH_TOKEN_SECRET = 'Jsm97f8xjlkHUAydzCsgW6a8ujJzLm9YhgWsqOU38QDmY'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

q = 'prayfor' 
count = 30
'''
tweet_texts = []
tweet_mentions = []
tweet_hashtags = []
tweet_bios = []
'''
search_results = twitter_api.search.tweets(q=q, count=count)
statuses = search_results['statuses']

'''
# save relevant data
tweet_texts += [status['text'] for status in statuses]
tweet_mentions += [mention['screen_name'] for status in statuses
                       for mention in status['entities']['user_mentions']]
tweet_hashtags += [hashtag['text'] for status in statuses
                       for hashtag in status['entities']['hashtags']]
tweet_bios += [status['upickle.dump(all_media, open(path+'%s_ig_%s.p' % (used_tag,curret_time),'wb'))ser']['description'] for status in statuses 
                       if status['user']['description']]
'''

curret_time = time.asctime(time.localtime(time.time()))
for ch in [' ',':']:
	if ch in curret_time:
		curret_time = curret_time.replace(ch,'_')

path = '/Users/Jiwon/Desktop/socialdataanalysis/final/'
pickle.dump(statuses, open(path+'%s_%s.p' % (q,curret_time),'wb'))




