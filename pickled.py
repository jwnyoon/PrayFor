#!/usr/bin/python

import twitter
import pickle
import time



# Twitter API keys go here
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

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




