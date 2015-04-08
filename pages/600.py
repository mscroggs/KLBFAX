import os
from page import Page
from colours import colour_print
from printer import instance as printer

class TVPage(Page):
    def __init__(self, page_num, channel, feed):
        super(TVPage, self).__init__(page_num)
        self.title = "TV: "+channel
        self.channel = channel
        self.feed = feed

    def generate_content(self):
        import urllib2
        from xml.etree import ElementTree
        content = colour_print(printer.text_to_ascii(self.channel))+"\n"
        response = urllib2.urlopen(self.feed)
        xml = response.read()
        e = ElementTree.fromstring(xml)
        for prog in e.findall('programme'):
            if int(prog.find('end').text)>int(self.now().strftime("%H%M")):
                content += prog.find('start').text+" "+prog.find('title').text+"\n"
        self.content = content

tv1 = TVPage("601","BBC1","http://bleb.org/tv/data/listings/1/bbc1.xml")
tv2 = TVPage("602","BBC2","http://bleb.org/tv/data/listings/1/bbc2.xml")
tv3 = TVPage("603","BBC3","http://bleb.org/tv/data/listings/1/bbc3.xml")
tv4 = TVPage("604","BBC4","http://bleb.org/tv/data/listings/1/bbc4.xml")
tv5 = TVPage("605","BBC News 24","http://bleb.org/tv/data/listings/1/bbc_news24.xml")
tv6 = TVPage("606","BBC Parliament","http://bleb.org/tv/data/listings/1/bbc_parliament.xml")
tv7 = TVPage("607","Channel 4","http://bleb.org/tv/data/listings/1/ch4.xml")
tv8 = TVPage("608","Challenge","http://bleb.org/tv/data/listings/1/challenge.xml")
tv9 = TVPage("609","Dave","http://bleb.org/tv/data/listings/1/dave.xml")
tv10 = TVPage("610","five","http://bleb.org/tv/data/listings/1/five.xml")
tv11 = TVPage("611","more4","http://bleb.org/tv/data/listings/1/more4.xml")
tv12 = TVPage("612","Film Four","http://bleb.org/tv/data/listings/1/film_four.xml")
tv13 = TVPage("613","s4c","http://bleb.org/tv/data/listings/1/s4c.xml")
tv14 = TVPage("614","QVC","http://bleb.org/tv/data/listings/1/qvc.xml")
