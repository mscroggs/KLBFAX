from page import Page
import url_handler

class TwitterPage(Page):
    def __init__(self, page_num):
        super(TwitterPage, self).__init__(page_num)
        self.title = "#emfcamp"

    def background(self):
        pass

    def generate_content(self):
        import tweet_handler

        self.add_title("#emfcamp")
        try:
            results = tweet_handler.search("emfcamp")
        except tweet_handler.NoTwitter:
            self.add_text("Twitter login failed...")
            return


        for tweet in results:
            self.add_text("@" + tweet["user"]["screen_name"] + " ", fg="YELLOW")
            self.add_text(" ".join(tweet["user"]["created_at"].split(" ")[:4]), fg="BLUE")
            self.add_newline()
            text = tweet["text"]
            while "http" in text:
                tsp = text.split("http",1)
                text = tsp[0] + "<url>"
                if " " in tsp[1]:
                    text += tsp[1].split(" ",1)[1]
            self.add_wrapped_text(text)
            self.add_newline()
            self.add_newline()

tpage = TwitterPage("210")
