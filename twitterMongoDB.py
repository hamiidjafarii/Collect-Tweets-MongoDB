import configparser
import tweepy
from pymongo import MongoClient

config = configparser.ConfigParser()
config.read('config.ini')

CONSUMER_KEY = config['twitter']['CONSUMER_KEY']
CONSUMER_SECRET = config['twitter']['CONSUMER_SECRET']
ACCESS_KEY = config['twitter']['ACCESS_KEY']
ACCESS_SECRET = config['twitter']['ACCESS_SECRET']


def twitter_OAuth(consumer_key,consumer_secret,access_key,access_secret):
    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key,access_secret)
    api = tweepy.API(auth)
    return api

api = twitter_OAuth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

client = MongoClient
client = MongoClient('mongodb localhost connection')
db = client.Twitter 
tweet_collection = db.tweetsdb
save_to_db = True 

query = 'Your query'
max_items = 100
tweets = tweepy.Cursor(api.search_tweets, q = query ,tweet_mode = 'extended').items(max_items)

while True:
        try:
            data = tweets.next()
        except StopIteration:
            break
        jsoned_data = data._json
        tweet = {
            'Date': jsoned_data['created_at'], 
            'User Name': jsoned_data['user']['screen_name'],
            'tweet_id': jsoned_data['id'],
            'Tweets': jsoned_data['full_text'],
            'Hashtags': jsoned_data['entities']['hashtags'],
            'likes': jsoned_data['favorite_count'],
            'Retweets': jsoned_data['retweet_count'],
            'Followers': jsoned_data['user']['followers_count'],
            'Location': jsoned_data['user']['location'],
            'Joined':jsoned_data['user']['created_at'],
            'Extra Data':jsoned_data
        }

        up_sert = tweet_collection.find_one({'tweet_id': tweet['tweet_id']})
        if up_sert is None:
            tweet_collection.insert_one(tweet)
        else:
            print("Tweet is found skipping...")
