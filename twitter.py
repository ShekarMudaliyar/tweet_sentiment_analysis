import tweepy as tw
from textblob import TextBlob as tb

consumer_key = 'qtMKa6UoIjBjgnYlYrHreLySH'
consumer_sec = '7l72H4fn62grihpz8FaTI5OoOxbnWKdoUACU49uY2ma9WMNslt'

access_token = '723883080-lpZdG3rnW6MCSS9j8N9R9eLvFkDdJ7tBAHkLpn8c'
access_token_secret = 'vw8P6obsnQa7RKfZNBYxmNQZabPPxCGPnQfxtrIUMQ5cn'

auth = tw.OAuthHandler(consumer_key,consumer_sec)
auth.set_access_token(access_token,access_token_secret)

api = tw.API(auth)

public_tweet = api.search('Trump')

for tweet in public_tweet:
	print(tweet.text)
	anals = tb(tweet.text)
	print(anals.sentiment)
