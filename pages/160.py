from page import Page

class Horoscope(Page):
    def __init__(self,page_num):
        super(Horoscope, self).__init__(page_num)
        self.title = "Horoscope"

    def background(self):
        import urllib2
        import json
        response = urllib2.urlopen("http://a.knrz.co/horoscope-api/current")
        self.horo = json.load(response)

    def generate_content(self):
        from functions import klb_replace
        import config
        from random import shuffle

        self.add_title("Horoscope",font="size4")
        shuffle(self.horo)
        for scope in self.horo:
            self.add_newline()
            self.add_title(klb_replace(scope["sign"]),fg="RED",bg="WHITE",font="size4")
            self.add_wrapped_text(klb_replace(scope["prediction"]))
            self.add_newline()

muirheadpage = Horoscope("160")
