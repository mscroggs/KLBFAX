import config
from page import Page
from functions import replace
from helpers import url_handler

class RadioPage(Page):
    def __init__(self, page_num, channel, feed):
        super(RadioPage, self).__init__(page_num)
        self.title = channel
        self.in_index = False
        self.channel = channel
        self.page_num = page_num
        self.importance = 1
        self.feed = feed
        self.feed_type = None

    def background(self):
        webpage = url_handler.load(self.feed)
        self.ls = []
        for i in webpage.split('aria-label="')[1:]:
            i = i.split('"')[0]
            if config.now().strftime("%-d %b") in i:
                time = i.split(" ")[2][:-1]
                title = i.split(": ")[-1].replace("&#039;","'")
                self.ls.append((time,title))

    def generate_content(self):
        self.add_title(self.channel,font="size4bold")
        self.move_cursor(x=75)
        self.add_text("TODAY", bg="YELLOW", fg="BLUE")
        self.move_cursor(x=0)
        for time, title in self.ls:
            self.add_text(time,fg="GREEN")
            self.add_text(" "+title)
            self.add_newline()

class RadioIPage(Page):
    def __init__(self,pages):
        super(RadioIPage, self).__init__("633")
        self.title = "Radio"
        self.importance = 1
        self.pages = pages

    def generate_content(self):
        self.add_title("Radio")

        for i,page in enumerate(self.pages):
            self.add_text(page.number, fg="RED")
            self.add_text(" "+page.title)
            if i%2==1:
                self.add_newline()
            else:
                self.move_cursor(x=38)


class WavelengthPage(Page):
    def __init__(self, page_num):
        super(WavelengthPage, self).__init__(page_num)
        self.title = "Radio Wavelengths"
        self.importance = 3
        self.in_index = False

    def generate_content(self):
        self.add_title("BBC Radio",font="size4bold")
        self.add_newline()
        #long wave
        self.print_image(  "---------------------------------------------------------------------------\n"
                           "rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr",6,5)
        self.move_cursor(x=0,y=5)
        self.add_text("kHz  150                                          198                       250 \n"
                      "LW\n"
        #                  20       19       18       17       16       15       14       13       12
                      "m    2000             1800              1600       ↑      1400              1200\n"
                      "                                                RADIO 4                         ")

        # medium wave
        self.print_image(  "---------------------------------------------------------------------------\n"
                           "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",11,5)
        self.move_cursor(x=0,y=10)
        self.add_text("kHz  500               600               750               1000             1500\n"
                      "MW\n"
        #                   60       55       50       45       40       35       30       25       20
                      "m    600               500          ↑    400           ↑   300               200\n"
                      "                                  RADIO 5            RADIO 5                    ")

        # medium wave
        self.print_image(  "---------------------------------------------------------------------------\n"
                           "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",16,5)
        self.move_cursor(x=0,y=15)
        self.add_text("MHz   88            92            96            100           104           108 \n"
                      "FM\n"
        # 88-91(2) 90-93(3) 92-95(4) 94.7(Hereford & Worcester) 97-99(1) 104(Hereford & Worcester) 103-105(4)
        #                    88            92            96            100           104           108
        #                    88 89  90 91  92 93  94 95  96 97  98 99  100101 102103 104105 106017 108
                      "          ↑      ↑      ↑    ↑           ↑                    ↑ ↑                       \n"
                      "       RADIO  RADIO   RADIO  HEREFORD   RADIO          HEREFORD  RADIO  \n"
                      "         2      3       4    & WORCESTER  4         & WORCESTER    4")

pages = []
pages.append(WavelengthPage("634"))
pages.append(RadioPage("635","BBC Radio 1","https://www.bbc.co.uk/schedules/p00fzl86"))
pages.append(RadioPage("636","BBC Radio 1Xtra","https://www.bbc.co.uk/schedules/p00fzl64"))
pages.append(RadioPage("637","BBC Radio 2","https://www.bbc.co.uk/schedules/p00fzl8v"))
pages.append(RadioPage("638","BBC Radio 2 Country","https://www.bbc.co.uk/schedules/p02hyyrj"))
pages.append(RadioPage("639","BBC Radio 2 Eurovision","https://www.bbc.co.uk/schedules/p02q2ldk"))
pages.append(RadioPage("640","BBC Music Jazz","https://www.bbc.co.uk/schedules/p031h0bc"))
pages.append(RadioPage("641","BBC Radio 3","https://www.bbc.co.uk/schedules/p00fzl8t"))
pages.append(RadioPage("642","BBC Radio 4","https://www.bbc.co.uk/schedules/p00fzl7j"))
pages.append(RadioPage("643","BBC Radio 4 Extra","https://www.bbc.co.uk/schedules/p00fzl7l"))
pages.append(RadioPage("644","BBC Radio 5 Live","https://www.bbc.co.uk/schedules/p00fzl7g"))
pages.append(RadioPage("645","BBC Radio 5 Live Sports Extra","https://www.bbc.co.uk/schedules/p00fzl7h"))
pages.append(RadioPage("646","BBC Radio 6 Music","https://www.bbc.co.uk/schedules/p00fzl65"))
pages.append(RadioPage("647","BBC Hereford & Worcester","https://www.bbc.co.uk/schedules/p00fzl7q"))
pages.append(RadioPage("648","BBC Asian Network","https://www.bbc.co.uk/schedules/p00fzl68"))
pages.append(RadioPage("649","BBC World Service","https://www.bbc.co.uk/schedules/p00fzl9p"))
pages.append(RadioPage("650","BBC Radio 1 Vintage","https://www.bbc.co.uk/schedules/p0572jvl"))
pages.append(RadioPage("651","CBeebies Radio","https://www.bbc.co.uk/schedules/p02jf21y"))
pages.append(RadioPage("652","BBC Afrique Radio","https://www.bbc.co.uk/schedules/p02yvckd"))
pages.append(RadioPage("653","BBC Hausa Radio","https://www.bbc.co.uk/schedules/p02yxhll"))
pages.append(RadioPage("654","BBC Radio Gahuza","https://www.bbc.co.uk/schedules/p02yvcry"))
pages.append(RadioPage("655","BBC Raadiyaha Soomaali","https://www.bbc.co.uk/schedules/p02yvpsb"))
pages.append(RadioPage("656","BBC Swahili Radio","https://www.bbc.co.uk/schedules/p02yvsf8"))

tp = RadioIPage(pages)
tp.index_num = "633-656"
