import os
from page import Page
from colours import colour_print
from printer import instance as printer

class TVPage(Page):
    def __init__(self, page_num, channel, feed, day):
        super(TVPage, self).__init__(page_num)
        self.title = day+"'s TV: "+channel
        self.channel = channel
        self.feed = feed
        self.day = day

    def generate_content(self):
        import urllib2
        from xml.etree import ElementTree
        content = colour_print(printer.text_to_ascii(self.channel)+" "+self.day)+"\n"
        response = urllib2.urlopen(self.feed)
        xml = response.read()
        e = ElementTree.fromstring(xml)
        for prog in e.findall('programme'):
            if int(prog.find('end').text)>int(self.now().strftime("%H%M")) or int(prog.find('start').text)>int(self.now().strftime("%H%M")) or self.day != "Today":
                content += prog.find('start').text+" "+prog.find('title').text+"\n"
        content = "Belgin Breakfast".join(content.split("Breakfast"))
        content = "The Olly Show".join(content.split("The One Show"))
        content = "Pietro".join(content.split("Jamie"))
        content = "ith Adam Townsend".join(content.split("ith Me"))
        content = "KLB".join(content.split("USA"))
        content = "KLB".join(content.split("BBC"))
        content = "News, presented by Sam Brown\n".join(content.split("News\n"))
        content = "KLB".join(content.split("A&E"))
        content = (self.colours.Style.STRIKE+"Stacey"+self.colours.Style.DEFAULT+" Huda").join(content.split("Stacey"))
        self.content = content

tv1 = TVPage("601","BBC1","http://bleb.org/tv/data/listings/0/bbc1.xml","Today")
tv2 = TVPage("602","BBC2","http://bleb.org/tv/data/listings/0/bbc2.xml","Today")
tv3 = TVPage("603","BBC3","http://bleb.org/tv/data/listings/0/bbc3.xml","Today")
tv4 = TVPage("604","BBC4","http://bleb.org/tv/data/listings/0/bbc4.xml","Today")
tv5 = TVPage("605","BBC News 24","http://bleb.org/tv/data/listings/0/bbc_news24.xml","Today")
tv6 = TVPage("606","BBC Parliament","http://bleb.org/tv/data/listings/0/bbc_parliament.xml","Today")
tv7 = TVPage("607","Channel 4","http://bleb.org/tv/data/listings/0/ch4.xml","Today")
tv8 = TVPage("608","Challenge","http://bleb.org/tv/data/listings/0/challenge.xml","Today")
tv9 = TVPage("609","Dave","http://bleb.org/tv/data/listings/0/dave.xml","Today")
tv10 = TVPage("610","five","http://bleb.org/tv/data/listings/0/five.xml","Today")
tv11 = TVPage("611","more4","http://bleb.org/tv/data/listings/0/more4.xml","Today")
tv12 = TVPage("612","Film Four","http://bleb.org/tv/data/listings/0/film_four.xml","Today")
tv13 = TVPage("613","s4c","http://bleb.org/tv/data/listings/0/s4c.xml","Today")
tv14 = TVPage("614","QVC","http://bleb.org/tv/data/listings/0/qvc.xml","Today")
tv15 = TVPage("615","BBC1","http://bleb.org/tv/data/listings/1/bbc1.xml","Tomorrow")
tv16 = TVPage("616","BBC2","http://bleb.org/tv/data/listings/1/bbc2.xml","Tomorrow")
tv17 = TVPage("617","BBC3","http://bleb.org/tv/data/listings/1/bbc3.xml","Tomorrow")
tv18 = TVPage("618","BBC4","http://bleb.org/tv/data/listings/1/bbc4.xml","Tomorrow")
tv19 = TVPage("619","BBC News 24","http://bleb.org/tv/data/listings/1/bbc_news24.xml","Tomorrow")
tv20 = TVPage("620","BBC Parliament","http://bleb.org/tv/data/listings/1/bbc_parliament.xml","Tomorrow")
tv21 = TVPage("621","Channel 4","http://bleb.org/tv/data/listings/1/ch4.xml","Tomorrow")
tv22 = TVPage("622","Challenge","http://bleb.org/tv/data/listings/1/challenge.xml","Tomorrow")
tv23 = TVPage("623","Dave","http://bleb.org/tv/data/listings/1/dave.xml","Tomorrow")
tv24 = TVPage("624","five","http://bleb.org/tv/data/listings/1/five.xml","Tomorrow")
tv25 = TVPage("625","more4","http://bleb.org/tv/data/listings/1/more4.xml","Tomorrow")
tv26 = TVPage("626","Film Four","http://bleb.org/tv/data/listings/1/film_four.xml","Tomorrow")
tv27 = TVPage("627","s4c","http://bleb.org/tv/data/listings/1/s4c.xml","Tomorrow")
tv28 = TVPage("628","QVC","http://bleb.org/tv/data/listings/1/qvc.xml","Tomorrow")
