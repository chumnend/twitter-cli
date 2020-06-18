import tweepy
from config import create_api
from bots.auto_reply import auto_reply
from bots.fav_retweet import fav_retweet
from bots.follow_back import follow_back
from cmds.find_user import find_user
from cmds.timeline import timeline
from cmds.tweet import tweet

from cmd import Cmd
from argparse import ArgumentParser

class TwitterCLI(Cmd):
    api = create_api()
    me = api.me()
    
    prompt = 'tw_cli> '
    intro = f'hello, {me.name}! type ? to see options'
    
    # --- commands ---
    def do_tweet(self, inp):
        '''
        post tweet to your twitter account
        
        EXAMPLE: tweet "Hello From Twitter CLI"
        '''
        msg = inp.strip('""').strip("'").strip()
        tweet(self.api, msg)
    def do_find(self, inp):
        '''
        find a user by name
        
        EXAMPLE: find "nicholaschumney"
        '''
        user_name = inp.strip('""').strip("'").strip()
        find_user(self.api, user_name)
    def do_timeline(self, inp):
        '''
        get most recent 20 tweets on timeline
        '''
        timeline(self.api)
        
    # --- bots ---
    def do_auto_reply(self, inp):
        '''
        runs twitter bot to auto replay with keyword(s). All keyword should be 
        prefixed with 'kw:', or else the key word will not be registered.
        
        EXAMPLE: auto_reply kw:python kw:"I love python" r:"I do too!"
        '''
        keywords = []
        reply = ''
        
        for x in inp.split():
            if(x[0:3] == 'kw:'):
                keywords.append(x[3:])
            elif(x[0:2] == 'r:'):
                reply = x[2:]
                
        if len(keywords) == 0 or len(reply) == 0:
            print('requires at least one keyword and one reply. use "help auto_reply" to check usage.')
            return

        auto_reply(self.api, keywords, reply)
    def do_fav_retweet(self, inp):
        '''
        run twitter bot to favourite tweets with keyword(s)
        EXAMPLE: run_favretweet kw:python kw:"I love python"
        NOTE: can be multiple keywords with prefix kw:
        '''
        keywords = []
        for x in inp.split():
            if(x[0:3] == 'kw:'):
                keywords.append(x[3:])
        
        if len(keywords) == 0:
            print('requires at least one keyword. use "help fav_retweet" to check usage.')
            return
                
        fav_retweet(self.api, keywords)
    def do_follow_back(self, inp):
        '''
        run twitter bot to followback all followers
        EXAMPLE: follow_back
        '''
        follow_back(self.api)
    
    def do_exit(self, inp):
        '''exit the application. Shorthand: ctrl-D x q'''
        print('Goodbye')
        return True
        
    do_EOF = do_exit
    
    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
        
        print('command not found. type ? to see commands.')

if __name__ == '__main__':
    TwitterCLI().cmdloop()
