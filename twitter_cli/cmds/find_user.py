import tweepy
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def find_user(api, user):
    logger.info(f'finding user {user}')
    user = api.get_user(user)

    print("User details:")
    print(user.name)
    print(user.description)
    print(user.location)
