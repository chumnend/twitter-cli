import tweepy
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def auto_reply(api, keywords, reply):
    since_id = 1
    while True:
        logger.info('retrieving mentions')
        new_since_id = since_id
        for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
            new_since_id = max(tweet.id, new_since_id)
            if tweet.in_reply_to_status_id is not None:
                continue
            
            if any(keyword in tweet.text.lower() for keyword in keywords):
                logger.info(f"Answering to {tweet.user.name}")
    
                if not tweet.user.following:
                    tweet.user.follow()
    
                api.update_status(
                    status=reply,
                    in_reply_to_status_id=tweet.id,
                )
        
        since_id = new_since_id
        logger.info('Waiting...')
        time.sleep(60)
