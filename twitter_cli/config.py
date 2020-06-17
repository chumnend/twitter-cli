import os
import logging
import tweepy
from dotenv import load_dotenv

logger = logging.getLogger()

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '..', '.env'))

def create_api():
    api_key = os.environ.get('API_KEY')
    api_secret = os.environ.get('API_SECRET_KEY')
    access_token = os.environ.get('ACCESS_TOKEN')
    access_secret = os.environ.get('ACCESS_SECRET_TOKEN')

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error('Error creating API', exc_info=None)
        return None
        
    logger.info('API created')
    
    return api
