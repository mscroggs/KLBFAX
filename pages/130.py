from page import Page


class PointsPage(Page):
    def __init__(self):
        super(PointsPage, self).__init__("130")
        self.title = "House Points"
        self.index_num = "130-131"

    def generate_content(self):
        self.add_title("house points")

        self.start_fg_color("GREEN")
        self.add_text("Year")
        pos = (6,17,27,38,48,59,65)
        for p,t in zip(pos,["Gryffindor","Slytherin","Hufflepuff","Ravenclaw","Durmstrang","Squib","Peeves"]):
            self.move_cursor(x=p)
            self.add_text(t)
        self.end_fg_color()
        self.add_newline()
        for ls in [
                ("2015a",(692,  525,1155, 702, 440, 513,   0)),
                ("2015b",(3382, 408,4614,3591, 606,2174,  38)),
                ("2016a",(1621, 378,3640,3407, 202,3744,  30)),
                ("2016b",(1428,1609,3789,3609, 366, 434,   0))
                  ]:
            self.start_fg_color("GREEN")
            self.add_text(ls[0])
            self.end_fg_color()
            for p,t in zip(pos,ls[1]):
                self.move_cursor(p)
                if t == max(ls[1]):
                    self.start_fg_color("RED")
                self.add_text(str(t))
                if t == max(ls[1]):
                    self.end_fg_color()
            self.add_newline()

p_page = PointsPage()
