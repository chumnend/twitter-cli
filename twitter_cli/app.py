import tweepy
from bots.auto_reply import auto_reply
from bots.fav_retweet import fav_retweet
from bots.follow_back import follow_back
from config import create_api

def run():
    api = create_api()
    
    auto_reply(api, ['Python', 'Tweepy'], "Please reach us via DM")
    # fav_retweet(api, ['Python', 'Tweepy'])
    # follow_back(api)

if __name__ == '__main__':
    run()
