from page import Page
import url_handler

class Horoscope(Page):
    def __init__(self,page_num):
        super(Horoscope, self).__init__(page_num)
        self.title = "Horoscopes"

    def background(self):
        import json
        self.horo = url_handler.load_json("http://a.knrz.co/horoscope-api/current")
        for i,scope in enumerate(self.horo):
            self.horo[i]["prediction"] = "'".join(scope["prediction"].split(u"\u2019"))

    def generate_content(self):
        from functions import klb_replace
        import config
        from random import shuffle

        self.add_title("Horoscopes",font="size4")
        shuffle(self.horo)
        for scope in self.horo[:3]:
            self.add_newline()
            self.add_title(klb_replace(scope["sign"]),fg="RED",bg="WHITE",font="size4")
            self.add_wrapped_text(klb_replace(scope["prediction"]))
            self.add_newline()

muirheadpage = Horoscope("160")
