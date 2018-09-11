from page import Page
from random import shuffle

class EMFMapPage(Page):
    def __init__(self):
        super(EMFMapPage, self).__init__("703")
        self.importance = 2
        self.title = "EMF site map"

    def generate_content(self):
        map = ( "------------------------K------------b-----------------------------------b------\n"
                "-----------------------K-------------bbbbbbbbb---------------------------b------\n"
                "-----------------------K------------bbbrrrrrrrbbbbbbbbK-----------bbbbbbbb------\n"
                "----------------------K-------------bbbr--ggggrrrrrrrKKbbbbbbbbbbb--------b-----\n"
                "----------------------K-------------bbr---ggggggggggKKrrr------------------b----\n"
                "---------------------K--------------br-bb-gggggggggKKggggrr-----------------bbb-\n"
                "---------------------K--------------br-bb-ggggggggKKgggggg-rr------------------b\n"
                "--------------------K---------------br-bb-ggggggggKKgggggg--r-------------------\n"
                "--------------------K--------------b-r-bb-gggggggKKggggggg--r-------------------\n"
                "-------------------K--------------b-r-bbb-gggggggKggggggggg-r-------------------\n"
                "-------------------K-------------b-r--bb--ggggggKKgggggggggr--------------------\n"
                "------------------K-------------b--r-bbb--gggggKKggggggggggr--------------------\n"
                "------------------K------------b---r-bbb--ggggKKgggggggggggr--------------------\n"
                "-----------------K------------b----r-bbbb-gggKKggggggggggggr--------------------\n"
                "-----------------K-------------b---r------ggKKgggggggggggggr--------------------\n"
                "----------------K------------bb---rbbbbbbbb-KKgggggggggggggr--------------------\n"
                "----------------K-----------b----rbbbbb----KKbbbbbbbKKKKKKr---------------------\n"
                "---------------K-------------b---rbbbb-----KK----w-Kbbrrrrr---------------------\n"
                "---------------K-------------b---rbbbb----KKgggg-w-Kgrbbbbbbbb------------------\n"
                "--------------K---------------b--rbbbb---KKggggg---Kggrb------bbb---------------\n"
                "--------------K---------------b--r-bb----KKgggggw-Kggggrb--------bbb--bb--------\n"
                "-------------K-----------------b-r------KK-gggggg-Kggggrb-----------bbb---------\n"
                "-------------K-----------------b-r-----KKw--www--Kgggggrb-------------bb--------\n"
                "------------K------------------b-r----KKww--www-Kggggggrb-----------------------\n"
                "------------K----------------bb-r---KKK-ww--www-Kggggggrb-----------------------\n"
                "-------KKKKK----------------brrrr--KK-K--------Kgggggggrb-----------------------\n"
                "-------K---K----------KKKKKKKKKKKKKKKKKKKKKKKKKggggggggrb-----------------------\n"
                "-------K--K--KKKKKKKKK------brKKmm--wwK-www---gKKKgggggrb-----------------------\n"
                "--------K-KKK----------------brKKm----K-www---ggKKgggggr-bb----bb---------------\n"
                "--------KK-------------------brmmm----K-------gggKgggggr---bbbb--bbbbbbbb-------\n"
                "---------K-------------------br------K----www-ggKggggggr------------------------\n"
                "--------K-------------------b-r-w----K----wwwgggKgggggr-------------------------\n"
                "--------K-------------------br--w--w-K----wwwgggKgggggr-------------------------\n"
                "-------K-------------------br-www----K-------gggKgggggr-------------------------\n"
                "-------K------------------b-r-www--w-KwwwwgggggKgggggr--------------------------\n"
                "------K------------------b-r--w----w-KwwwwgggggKgggggr--------------------------\n"
                "------K-----------------brrr--ggggggK-wwwwgggggKgggggr--------------------------\n"
                "-----K-----------------br-----ggggggKggggggggggKgggggr--------------------------\n"
                "-----K----------------br-bb---ggggggKgggggggggKgggggr---------------------------\n"
                "----K----------------br-bbbb--ggggggKgggggggggKgggggr---------------------------\n"
                "----K---------------br-bbbbb--ggggggKgggggggggKggggr----------------------------\n"
                "---K----------------br-bbbbb--ggggggKggggg---Kgggggr----------------------------\n"
                "---K----------------br-bbbbb--gggggKgggggg-wwKgggggr---------------KK-----------\n"
                "--K----------------b-r-bbbb---gggggK-------wwKmmmmr----------------KK-----------\n"
                "--K----------------br-bbbbb---gggggKwwwwmmmmKmmmmmr----------------gg-----------\n"
                "-K-----------------br-bbbbb---gggggKwwwwmmmmKmmmmr-----------------gg-----------\n"
                "-K-----------------br-bbbbb---gggggKwwwwmmmKmmmmmr-----------------bb-----------\n"
                "K-----------------b-r-bbbbb---ggggKwwwwmmmmKrrrrrr-----------------bb-----------\n"
                "K-----------------b--r-bb-rrr-ggggKwwwwmmmmKKKKKK------------------rr-----------\n"
                "------------------b--r-bb-r--rrrr-K----mmmKr-----KKKK--------------rr-----------\n"
                "-----------------b----r--rbbbbbb-rKrr--mmmKr--b------KKKK----------ww-----------\n"
                "-----------------b-bbbbrrb------bbbbbrrrrrKr-b-b---------KKK-------ww-----------\n"
                "----------------b---bbb--------------bbbbbKbb---b-----------KK-----mm-----------\n"
                "----------------b--bbb--------------------K-------------------KK---mm-----------"
              )
        self.print_image(map,0,0)

        self.move_cursor(x=37,y=23)
        self.add_text("A",fg="BLACK",bg="WHITE")
        self.move_cursor(x=45,y=11)
        self.add_text("B",fg="BLACK",bg="WHITE")
        self.move_cursor(x=39,y=17)
        self.add_text("C",fg="BLACK",bg="WHITE")

        self.move_cursor(x=67,y=20)
        self.add_text("KEY",fg="BRIGHTWHITE",bg="BLACK")
        self.move_cursor(x=69,y=21)
        self.add_text("Road",fg="WHITE",bg="BLACK")
        self.move_cursor(x=69,y=22)
        self.add_text("Camping",fg="WHITE",bg="BLACK")
        self.move_cursor(x=69,y=23)
        self.add_text("Water",fg="WHITE",bg="BLACK")
        self.move_cursor(x=69,y=24)
        self.add_text("Fence",fg="WHITE",bg="BLACK")
        self.move_cursor(x=69,y=25)
        self.add_text("Marquee",fg="WHITE",bg="BLACK")
        self.move_cursor(x=69,y=26)
        self.add_text("Backstage",fg="WHITE",bg="BLACK")

        self.move_cursor(x=0,y=0)
        self.add_title("Map",font="size4", fill=False, fg="BLACK", bg="BRIGHTWHITE")


map_page = EMFMapPage()
