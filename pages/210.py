from page import Page
import url_handler
class TwitterPage(Page):
    def __init__(self, page_num):
        super(TwitterPage, self).__init__(page_num)
        self.title = "#emfcamp"

    def background(self):
        pass

    def generate_content(self):
        import twitter
        import config
        twapi = twitter.Twitter(auth=twitter.OAuth(config.twitter_access_key,
            config.twitter_access_secret, config.twitter_consumer_key, config.twitter_consumer_secret))

        results = twapi.search.tweets(q="#emfcamp", result_type="recent", count=15)
        self.add_title("#emfcamp")
        for tweet in results["statuses"]:
            self.add_text("@" + tweet["user"]["screen_name"] + " ", fg="YELLOW")
            self.add_wrapped_text(tweet["text"])
            self.add_newline()
            self.add_newline()


tpage = TwitterPage("210")
