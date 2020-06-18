import tweepy
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def timeline(api):
    logger.info('retreiving timeline....')
    timeline = api.home_timeline()
    for tweet in timeline:
        print(f'{tweet.user.name} said {tweet.text}')
