#!/usr/bin/python
# coding: utf-8

from twitter import Twitter
import pickle

twitter = Twitter(domain='search.twitter.com')

query = '@kuronekounion -RT'

r = twitter.search(q=query)
next_max_id = r['max_id']
exist_count = 0
tweets = []
while(len(r['results']) != 0):
  for tweet in r['results']:
    next_max_id = min(next_max_id, tweet['id'] - 1)
    tweets.append(tweet)
    
  r = twitter.search(q=query, max_id=next_max_id)

tweets_file = open('tweets.pkl', 'wb')
pickle.dump(tweets, tweets_file)
tweets_file.close()

