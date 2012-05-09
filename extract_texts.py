import pickle

tweets_file = open('tweets.pkl')
tweets = pickle.load(tweets_file)
tweets_file.close()

for tweet in tweets:
  print tweet['text'].encode('utf8')


