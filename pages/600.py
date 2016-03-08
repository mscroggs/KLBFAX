import os
import re
from page import Page
from colours import colour_print
from printer import instance as printer

def escape(string):
    if string=="?":
        return "\?"
    return string

class TVPage(Page):
    def __init__(self, page_num, channel, feed, day):
        super(TVPage, self).__init__(page_num)
        self.title = day+"'s TV: "+channel
        self.in_index = False
        self.channel = channel
        self.page_num = page_num
        self.feed = feed
        self.day = day
        pages.append([page_num,channel+" ("+day+")"])

    def generate_content(self):
        import urllib2
        content = colour_print(printer.text_to_ascii(self.channel,fill=False))+self.colours.Foreground.YELLOW+self.colours.Background.BLUE+" "+self.day+self.colours.Foreground.DEFAULT+self.colours.Background.DEFAULT+"\n"
        rss_dict = {"642": "http://www.iplayerconverter.co.uk/wu/2/date/" + strftime("%Y-%m-%d") + "/rss.aspx",
                    "692": "http://www.iplayerconverter.co.uk/wu/2/date/" + (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d") + "/rss.aspx",
                    "644": "http://www.iplayerconverter.co.uk/wu/4/date/" + strftime("%Y-%m-%d") + "/rss.aspx",
                    "694": "http://www.iplayerconverter.co.uk/wu/4/date/" + (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d") + "/rss.aspx"
                    }
        if self.page_num in rss_dict.keys():
            import feedparser
            from time import strptime, strftime
            import datetime
            rss_url = rss_dict[self.page_num]
            
            feed = feedparser.parse(rss_url)
            start_times = list()
            start_times_formatted = list()
            titles = list()
            for item in feed['items']:
                start_times.append(strptime(item['published'],"%m/%d/%Y %I:%M:%S %p"))
                start_times_formatted.append(strftime("%H%M",strptime(item['published'],"%m/%d/%Y %I:%M:%S %p")))
                titles.append(item['title'] )

            for i in range(len(titles)):
                if i == len(titles)-1 or (int(strftime("%y%m%d%H%M",start_times[i+1])) > int(self.now().strftime("%y%m%d%H%M"))):
                    #if i != len(titles)-1:
                    #    print strftime("%y%m%d%H%M",start_times[i+1]) , int(self.now().strftime("%y%m%d%H%M")), (int(strftime("%y%m%d%H%M",start_times[i+1])) > int(self.now().strftime("%y%m%d%H%M")))
                    content += self.colours.Foreground.GREEN+start_times_formatted[i]+self.colours.Foreground.DEFAULT+" "+titles[i]+"\n"
            
        else:
            from xml.etree import ElementTree
            response = urllib2.urlopen(self.feed)
            xml = response.read()
            e = ElementTree.fromstring(xml)
            for prog in e.findall('programme'):
                if int(prog.find('end').text)>int(self.now().strftime("%H%M")) or int(prog.find('start').text)>int(self.now().strftime("%H%M")) or self.day != "Today":
                    content += self.colours.Foreground.GREEN+prog.find('start').text+self.colours.Foreground.DEFAULT+" "+prog.find('title').text+"\n"
            content = (self.colours.Foreground.BLUE+"New:"+self.colours.Foreground.DEFAULT).join(content.split("New:"))
        swaps = [
            ["Breakfast","Belgin Breakfast"],
            ["Not",u"\u00AC"],
            ["The One Show","The Olly Show"],
            ["Wright","Mart Wright"],
            ["Sport","Maths"],["Sportsday","Mathsday"],
            ["Jamie","Pietro"],
            ["Agents of S\.H\.I\.E\.L\.D\.","Mathematicians of U.C.L.K.L.B"],
            ["USA","KLB"],
            ["BBC","KLB"],
            ["A&E","KLB"],
            ["Builder","Constructor"],
            ["World","KLB"],
            ["Home","KLB"],
            ["Homes","KLBs"],
            ["Cwm","KLB"],
            ["Have I","Has Adam Townsend"],["I","Adam Townsend"],["Me","Adam Townsend"],
            ["You","Belgin"],
            ["Raymond","Belgin"],
            ["He","Adam"],["Him","Adam"],
            ["She","Anna"],["Her","Anna"],
            ["It","Scroggsbot"],
            ["We","The West Wingers"],["Us","The West Wingers"],
            ["They","The EastEnders"],["Them","The EastEnders"],
            ["Man","Olly"],["Men","Ollys"],
            ["News","News (presented by Sam Brown)"],
            ["Newyddion","Newyddion (a gyflwynwyd gan Sam Brown)"],
            ["Mother","Supervisor"],["Father","Supervisor"],
            ["8 out of 10","0.8"],
            ["Movie","chalkdust"],["Film","chalkdust"],["Family","chalkdust"],
            ["Castle","Mathematics Mezzanine"],
            ["Mrs Brown","Rafael"],
            ["Alan Carr","Olly Southwick"],
            ["Casualty","Causality"],
            ["Match","Maths"],
            ["Christmas","Oxmas"],
            ["Football","Maths"],["Rugby","Maths"],["Tennis","Maths"],["Golf","Maths"],
            ["Cycling","Maths"],["Athletics","Maths"],
            ["Wallace","Crazy Nico"],
            ["Politics","Mathematics"],
            ["Political","Mathematical"],
            ["Stacey","Huda"],
            ["Antiques","Statistics"],
            ["Santa","Huda"],
            ["Ben","Momchil"],
            ["Holly","Antonio"],
            ["Deal","Soheni"],
            ["The Tribe",self.colours.Background.RED+self.colours.Foreground.BLACK+"Pietro's Pick"+self.colours.Background.DEFAULT+self.colours.Foreground.DEFAULT+" The Tribe"],
            ["Teenage Mutant Ninja Turtles",self.colours.Background.RED+self.colours.Foreground.BLACK+"Belgin's Pick"+self.colours.Background.DEFAULT+self.colours.Foreground.DEFAULT+" Teenage Mutant Ninja Turtles"],
            ["X-Men Origins","X-Men Origins Seminar Room"],
            ["Bruce","Rafael"]
        ]
        punc = [" ","?","!",":","'",'"',"\n"]
        for swap in swaps:
            for p in punc:
                content = (" "+swap[1]+p).join(re.split("(?i) "+swap[0]+escape(p),content))
#            content = (" "+swap[1]+"?").join(re.split("(?i) "+swap[0]+"\?",content))
 #           content = (" "+swap[1]+"!").join(re.split("(?i) "+swap[0]+"!",content))
  #          content = (" "+swap[1]+":").join(re.split("(?i) "+swap[0]+":",content))
   #         content = (" "+swap[1]+"'").join(re.split("(?i) "+swap[0]+"'",content))
    #        content = (" "+swap[1]+"\n").join(re.split("(?i) "+swap[0]+"\n",content))
        self.content = content
pages = []
tv1 = TVPage("601","BBC1","http://bleb.org/tv/data/listings/0/bbc1.xml","Today")
tv2 = TVPage("602","BBC2","http://bleb.org/tv/data/listings/0/bbc2.xml","Today")
tv3 = TVPage("603","ITV","http://bleb.org/tv/data/listings/0/p_itv1.xml","Today")
tv4 = TVPage("604","Channel 4","http://bleb.org/tv/data/listings/0/ch4.xml","Today")
tv5 = TVPage("605","Channel 5","http://bleb.org/tv/data/listings/0/five.xml","Today")
tv6 = TVPage("606","ITV2","http://bleb.org/tv/data/listings/0/p_itv2.xml","Today")
tv7 = TVPage("608","S4C","http://bleb.org/tv/data/listings/0/s4c.xml","Today")
tv8 = TVPage("609","BBC4","http://bleb.org/tv/data/listings/0/bbc4.xml","Today")
tv9 = TVPage("612","Dave","http://bleb.org/tv/data/listings/0/dave.xml","Today")
tv10 = TVPage("614","More4","http://bleb.org/tv/data/listings/0/more4.xml","Today")
tv11 = TVPage("615","Film 4","http://bleb.org/tv/data/listings/0/film_four.xml","Today")
tv12 = TVPage("616","QVC","http://bleb.org/tv/data/listings/0/qvc.xml","Today")
tv13 = TVPage("628","E4","http://bleb.org/tv/data/listings/0/e4.xml","Today")
tv14 = TVPage("629","Challenge","http://bleb.org/tv/data/listings/0/challenge.xml","Today")
tv15 = TVPage("630","BBC News","http://bleb.org/tv/data/listings/0/bbc_news24.xml","Today")
tv16 = TVPage("631","BBC Parliament","http://bleb.org/tv/data/listings/0/bbc_parliament.xml","Today")
tv17 = TVPage("642","BBC Radio 2","R2","Today")
tv18 = TVPage("644","BBC Radio 4","R4","Today")

tv19 = TVPage("651","BBC1","http://bleb.org/tv/data/listings/1/bbc1.xml","Tomorrow")
tv20 = TVPage("652","BBC2","http://bleb.org/tv/data/listings/1/bbc2.xml","Tomorrow")
tv21 = TVPage("653","ITV","http://bleb.org/tv/data/listings/1/p_itv1.xml","Tomorrow")
tv22 = TVPage("654","Channel 4","http://bleb.org/tv/data/listings/1/ch4.xml","Tomorrow")
tv23 = TVPage("655","Channel 5","http://bleb.org/tv/data/listings/1/five.xml","Tomorrow")
tv24 = TVPage("656","ITV2","http://bleb.org/tv/data/listings/1/p_itv2.xml","Tomorrow")
tv25 = TVPage("658","S4C","http://bleb.org/tv/data/listings/1/s4c.xml","Tomorrow")
tv26 = TVPage("659","BBC4","http://bleb.org/tv/data/listings/1/bbc4.xml","Tomorrow")
tv27 = TVPage("662","Dave","http://bleb.org/tv/data/listings/1/dave.xml","Tomorrow")
tv28 = TVPage("664","More4","http://bleb.org/tv/data/listings/1/more4.xml","Tomorrow")
tv29 = TVPage("665","Film 4","http://bleb.org/tv/data/listings/1/film_four.xml","Tomorrow")
tv30 = TVPage("666","QVC","http://bleb.org/tv/data/listings/1/qvc.xml","Tomorrow")
tv31 = TVPage("678","E4","http://bleb.org/tv/data/listings/1/e4.xml","Tomorrow")
tv32 = TVPage("679","Challenge","http://bleb.org/tv/data/listings/1/challenge.xml","Tomorrow")
tv33 = TVPage("680","BBC News","http://bleb.org/tv/data/listings/1/bbc_news24.xml","Tomorrow")
tv34 = TVPage("681","BBC Parliament","http://bleb.org/tv/data/listings/1/bbc_parliament.xml","Tomorrow")
tv35 = TVPage("692","BBC Radio 2","R2","Tomorrow")
tv36 = TVPage("694","BBC Radio 4","R4","Tomorrow")


tv_page = Page("600")
tv_page.content = colour_print(printer.text_to_ascii("TV & Radio"))+"\n"
tv_page.title = "TV & Radio Index"
i=0
for page in pages:
    tv_page.content+=tv_page.colours.Foreground.RED+page[0]+tv_page.colours.Foreground.DEFAULT+" "+page[1]
    if i==1:
        tv_page.content += "\n"
    else:
        tv_page.content += " "*(38-len(page[0]+page[1]))
    i = 1-i
