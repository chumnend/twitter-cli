import tweepy
import logging
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
    
    def on_status(self, tweet):
        logger.info(f'processing tweet id {tweet.id}')
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            return 
        
        if not tweet.favorited:
            try:
                tweet.favourite()
            except Exception as e:
                logger.error("Error on fav", exc_info=None)
        
        if not tweet.retweeted:
            try:
                tweet.retweet()
            except Exception as e:
                logger.error('Error on fav and retweet', exc_info=None)
    
    def on_error(self, status):
        logger.error(status)

def fav_retweet(api, keywords):
    listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, listener)
    stream.filter(track=keywords, languages=['en'])
