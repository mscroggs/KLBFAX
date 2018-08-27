from page import Page

class TwitterPage(Page):
    def __init__(self, page_num, n, tpage=None):
        if tpage is None:
            self.tpage = self
            self.main = True
        else:
            self.tpage = tpage
            self.main = False
        self.start_n = n
        super(TwitterPage, self).__init__(page_num)
        self.title = "#emfcamp"

        if n == 0:
            self.importance = 5
            self.index_num = "210-259"
            self.title = "Twitter"
            self.lines = []
        else:
            self.importance = 2
            self.in_index = False

    def generate_content(self):
        from helpers import tweet_handler

        self.add_title("#emfcamp",font="size4")
        self.move_cursor(y=3,x=70)
        self.add_text("Page "+str(self.start_n+1)+"/10",fg="BLUE",bg="YELLOW")
        self.add_newline()
        try:
            results = tweet_handler.search("emfcamp")
        except tweet_handler.NoTwitter:
            self.add_text("Twitter login failed...")
            return

        if self.main:
            self.lines = []
            for tweet in results:
                if "retweeted_status" not in tweet:
                    self.lines.append([("@" + tweet["user"]["screen_name"] + " ", "YELLOW"),
                                       (" ".join(tweet["created_at"].split(" ")[:4]), "BLUE")])
                    text = tweet["full_text"]
                    while "http" in text:
                        tsp = text.split("http",1)
                        text = tsp[0] + "<url>"
                        if " " in tsp[1]:
                            text += tsp[1].split(" ",1)[1]

                    for i in range(0,len(text),80):
                        self.lines.append([(text[i:i+80], "WHITE")])
                    self.lines.append([])

        for line in self.tpage.lines[21*self.start_n:21*(self.start_n+1)]:
            for text,col in line:
                self.add_text(text, fg=col)
            self.add_newline()

class TwitterSinglePage(Page):
    def __init__(self, page_num, username):
        super(TwitterSinglePage, self).__init__(page_num)
        self.importance = 2
        self.title = "@"+username
        self.in_index = False
        self.username = username

    def background(self):
        from helpers import tweet_handler
        self.results = tweet_handler.user_timeline(self.username, count=20)


    def generate_content(self):
        self.add_title("    "+self.title,font="size4bold", fg="BLACK", bg="CYAN")
        self.print_image("c----cccc--\n"
                         "cc--ccccccc\n"
                         "cccccccccc-\n"
                         "ccccccccc--\n"
                         "-cccccccc--\n"
                         "--cccccc---\n"
                         "--ccccc----\n"
                         "cccccc-----")
        for tweet in self.results:
            if "retweeted_status" not in tweet:
                self.add_text("@" + tweet["user"]["screen_name"] + " ", fg="YELLOW")
                self.add_text(" ".join(tweet["created_at"].split(" ")[:4]), fg="BLUE")
                text = tweet["full_text"]
                while "http" in text:
                    tsp = text.split("http",1)
                    text = tsp[0] + "<url>"
                    if " " in tsp[1]:
                        text += tsp[1].split(" ",1)[1]
                self.add_newline()
                self.add_wrapped_text(text)
                self.add_newline()
                self.add_newline()



tpage = TwitterPage("210",0)
tpage1 = TwitterPage("211",1,tpage)
tpage2 = TwitterPage("212",2,tpage)
tpage3 = TwitterPage("213",3,tpage)
tpage4 = TwitterPage("214",4,tpage)
tpage5 = TwitterPage("215",5,tpage)
tpage6 = TwitterPage("216",6,tpage)
tpage7 = TwitterPage("217",7,tpage)
tpage8 = TwitterPage("218",8,tpage)
tpage9 = TwitterPage("219",9,tpage)

tpage10 = TwitterSinglePage("220","PolybiusBiotech")
tpage11 = TwitterSinglePage("221","emffax")
tpage12 = TwitterSinglePage("222","emfwebcam")
tpage13 = TwitterSinglePage("223","EMFCampMusic")
tpage14 = TwitterSinglePage("224","EMFDeliveries")
tpage15 = TwitterSinglePage("225","emfcountdown")
tpage16 = TwitterSinglePage("226","emfbeeb")
tpage17 = TwitterSinglePage("227","emffilmfest")
tpage18 = TwitterSinglePage("228","therobotarms")
tpage19 = TwitterSinglePage("229","EMFMedical")
tpage20 = TwitterSinglePage("230","emfcamp")
tpage21 = TwitterSinglePage("231","EMFInfoDesk")
tpage21.importance = 5
tpage22 = TwitterSinglePage("232","emfnoc")
tpage23 = TwitterSinglePage("233","emfctf")
tpage24 = TwitterSinglePage("234","emfhams")
tpage25 = TwitterSinglePage("235","scotconsulate")
tpage26 = TwitterSinglePage("236","emfweather")
tpage27 = TwitterSinglePage("237","emf_weather")
tpage28 = TwitterSinglePage("238","emfcoffee")
tpage29 = TwitterSinglePage("239","jonty")
tpage30 = TwitterSinglePage("240","russss")
tpage31 = TwitterSinglePage("241","marksteward")
tpage32 = TwitterSinglePage("242","dpslwk")
tpage33 = TwitterSinglePage("243","btscroggs")
tpage34 = TwitterSinglePage("244","flangey")
tpage35 = TwitterSinglePage("245","milliways2342")
tpage36 = TwitterSinglePage("246","timrterrible")
tpage37 = TwitterSinglePage("247","sde1000")
tpage38 = TwitterSinglePage("248","benjamincpu")
tpage39 = TwitterSinglePage("249","dominicgs")
tpage40 = TwitterSinglePage("250","MatBurnham")
tpage41 = TwitterSinglePage("251","londonhackspace")
tpage42 = TwitterSinglePage("252","HSNOTTS")
tpage43 = TwitterSinglePage("253","ClubMate_UK")
tpage44 = TwitterSinglePage("254","tomscott")
tpage45 = TwitterSinglePage("255","DrLucyRogers")
tpage46 = TwitterSinglePage("256","mscroggs")
tpage47 = TwitterSinglePage("257","mathslogicbot")
tpage48 = TwitterSinglePage("258","I_AM_A_CAT_BOT")
tpage49 = TwitterSinglePage("259","AnnoyingCliche")
