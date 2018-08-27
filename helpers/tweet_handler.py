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

def search(q, count=100):
    twapi = login()

    results = twapi.search.tweets(q=q, result_type="recent", tweet_mode="extended", count=count)
    return results["statuses"]

def user_timeline(user, count=100):
    twapi = login()

    results = twapi.statuses.user_timeline(screen_name=user, result_type="recent", tweet_mode="extended", count=count)
    return results
