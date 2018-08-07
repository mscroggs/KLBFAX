import twitter
import config

class NoTwitter(BaseException):
    pass

def login():
    try:
        return twitter.Twitter(auth=twitter.OAuth(config.twitter_access_key,
            config.twitter_access_secret, config.twitter_consumer_key, config.twitter_consumer_secret))
    except:
        raise NoTwitter

def search(q):
    twapi = login()

    results = twapi.search.tweets(q=q, result_type="recent", tweet_mode="extended")
    return results["statuses"]
