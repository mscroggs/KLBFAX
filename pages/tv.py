from page import Page
from functions import replace
from helpers import url_handler

class TVPage(Page):
    def __init__(self, page_num, channel, feed, day):
        super(TVPage, self).__init__(page_num)
        self.title = day+"'s TV: "+channel
        self.in_index = False
        self.channel = channel
        self.page_num = page_num
        self.importance = 1
        self.feed = feed
        self.day = day
        pages.append([page_num,channel+" ("+day+")"])
        self.feed_type = None

    def generate_content(self):
        from time import strptime, strftime
        self.add_title(self.channel)
        self.move_cursor(x=80-len(self.day))
        self.add_text(self.day, bg="YELLOW", fg="BLUE")
        self.move_cursor(x=0)

        if self.feed_type == 1:
            start_times = list()
            start_times_formatted = list()
            titles = list()
            for item in self.feed['items']:
                start_times.append(strptime(item['published'],"%m/%d/%Y %I:%M:%S %p"))
                start_times_formatted.append(strftime("%H%M",strptime(item['published'],"%m/%d/%Y %I:%M:%S %p")))
                titles.append(item['title'] )

            for i in range(len(titles)):
                if i == len(titles)-1 or (int(strftime("%y%m%d%H%M",start_times[i+1])) > int(self.now().strftime("%y%m%d%H%M"))):
                    self.add_text(start_times_formatted[i],fg="GREEN")
                    self.add_text(" "+replace(titles[i]))
                    self.add_newline()

        if self.feed_type == 2:
            for prog in self.e.findall('programme'):
                if int(prog.find('end').text)>int(self.now().strftime("%H%M")) or int(prog.find('start').text)>int(self.now().strftime("%H%M")) or self.day != "Today":
                    self.add_text(prog.find('start').text,fg="GREEN")
                    self.add_text(" "+replace(prog.find('title').text))
                    self.add_newline()


    def background(self):
        from time import strptime, strftime
        import feedparser
        import datetime
        rss_dict = {"642": "http://www.iplayerconverter.co.uk/wu/2/date/" + strftime("%Y-%m-%d") + "/rss.aspx",
                    "692": "http://www.iplayerconverter.co.uk/wu/2/date/" + (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d") + "/rss.aspx",
                    "644": "http://www.iplayerconverter.co.uk/wu/4/date/" + strftime("%Y-%m-%d") + "/rss.aspx",
                    "694": "http://www.iplayerconverter.co.uk/wu/4/date/" + (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d") + "/rss.aspx"
                    }
        if self.page_num in rss_dict.keys():
            rss_url = rss_dict[self.page_num]
            self.feed = feedparser.parse(rss_url)
            self.feed_type = 1

        else:
            from xml.etree import ElementTree
            xml = url_handler.load(self.feed)
            self.e = ElementTree.fromstring(xml)
            self.feed_type = 2
pages = []
tv1 = TVPage("601","BBC1","http://bleb.org/tv/data/listings/0/bbc1.xml","Today")
tv1.importance = 3
tv2 = TVPage("602","BBC2","http://bleb.org/tv/data/listings/0/bbc2.xml","Today")
tv2.importance = 3
tv3 = TVPage("603","ITV","http://bleb.org/tv/data/listings/0/p_itv1.xml","Today")
tv4 = TVPage("604","Channel 4","http://bleb.org/tv/data/listings/0/ch4.xml","Today")
tv5 = TVPage("605","Channel 5","http://bleb.org/tv/data/listings/0/five.xml","Today")
tv6 = TVPage("606","ITV2","http://bleb.org/tv/data/listings/0/p_itv2.xml","Today")
tv7 = TVPage("607","S4C","http://bleb.org/tv/data/listings/0/s4c.xml","Today")
tv8 = TVPage("608","BBC4","http://bleb.org/tv/data/listings/0/bbc4.xml","Today")
tv9 = TVPage("609","Dave","http://bleb.org/tv/data/listings/0/dave.xml","Today")
tv10 = TVPage("610","More4","http://bleb.org/tv/data/listings/0/more4.xml","Today")
tv11 = TVPage("611","Film 4","http://bleb.org/tv/data/listings/0/film_four.xml","Today")
tv12 = TVPage("612","QVC","http://bleb.org/tv/data/listings/0/qvc.xml","Today")
tv13 = TVPage("613","E4","http://bleb.org/tv/data/listings/0/e4.xml","Today")
tv14 = TVPage("614","Challenge","http://bleb.org/tv/data/listings/0/challenge.xml","Today")
tv15 = TVPage("615","BBC News","http://bleb.org/tv/data/listings/0/bbc_news24.xml","Today")
tv16 = TVPage("616","BBC Parliament","http://bleb.org/tv/data/listings/0/bbc_parliament.xml","Today")

tv19 = TVPage("617","BBC1","http://bleb.org/tv/data/listings/1/bbc1.xml","Tomorrow")
tv20 = TVPage("618","BBC2","http://bleb.org/tv/data/listings/1/bbc2.xml","Tomorrow")
tv21 = TVPage("619","ITV","http://bleb.org/tv/data/listings/1/p_itv1.xml","Tomorrow")
tv22 = TVPage("620","Channel 4","http://bleb.org/tv/data/listings/1/ch4.xml","Tomorrow")
tv23 = TVPage("621","Channel 5","http://bleb.org/tv/data/listings/1/five.xml","Tomorrow")
tv24 = TVPage("622","ITV2","http://bleb.org/tv/data/listings/1/p_itv2.xml","Tomorrow")
tv25 = TVPage("623","S4C","http://bleb.org/tv/data/listings/1/s4c.xml","Tomorrow")
tv26 = TVPage("624","BBC4","http://bleb.org/tv/data/listings/1/bbc4.xml","Tomorrow")
tv27 = TVPage("625","Dave","http://bleb.org/tv/data/listings/1/dave.xml","Tomorrow")
tv28 = TVPage("626","More4","http://bleb.org/tv/data/listings/1/more4.xml","Tomorrow")
tv29 = TVPage("627","Film 4","http://bleb.org/tv/data/listings/1/film_four.xml","Tomorrow")
tv30 = TVPage("628","QVC","http://bleb.org/tv/data/listings/1/qvc.xml","Tomorrow")
tv31 = TVPage("629","E4","http://bleb.org/tv/data/listings/1/e4.xml","Tomorrow")
tv32 = TVPage("630","Challenge","http://bleb.org/tv/data/listings/1/challenge.xml","Tomorrow")
tv33 = TVPage("631","BBC News","http://bleb.org/tv/data/listings/1/bbc_news24.xml","Tomorrow")
tv34 = TVPage("632","BBC Parliament","http://bleb.org/tv/data/listings/1/bbc_parliament.xml","Tomorrow")


class TVIPage(Page):
    def __init__(self):
        super(TVIPage, self).__init__("600")
        self.title = "TV & Radio Index"
        self.importance = 1

    def generate_content(self):
        self.add_title("TV & Radio")

        for i,page in enumerate(pages):
            self.add_text(page[0], fg="RED")
            self.add_text(" "+page[1])
            if i%2==1:
                self.add_newline()
            else:
                self.move_cursor(x=38)

tp = TVIPage()
