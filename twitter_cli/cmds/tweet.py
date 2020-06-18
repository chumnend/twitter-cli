import tweepy
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def tweet(api, msg):
    logger.info('creating tweet...')
    api.update_status(msg)
    logger.info('tweet sent')
