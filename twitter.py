import tweepy


class Twitter:
    def __init__(self, config):
        self.config = config.get()
        self.auth = tweepy.OAuthHandler(self.config['consumerKey'], self.config['consumerKeySecret'])
        self.auth.set_access_token(self.config['accessToken'], self.config['accessTokenSecret'])
        self.api = tweepy.API(self.auth)

    def getLastTimelinePost(self):
        for tweet in tweepy.Cursor(self.api.user_timeline).items(1):
            return tweet.text

    def postOnTimeline(self, text):
        self.api.update_status(text)

    def __str__(self):
        return self.getLastTimelinePost()
