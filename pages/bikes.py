from __future__ import division
from page import Page
from helpers import url_handler

class BikePage(Page):
    def __init__(self, page_num):
        super(BikePage, self).__init__(page_num)
        self.title = "Boris Bikes"
        self.tagline = "Live Santander Cycles. Data from TfL."
        self.in_index = True
        self.importance = 1
        pages.append([page_num,self.title])

    def generate_content(self):
        import dateutil.parser
        import datetime, pytz

        self.add_title(self.title,font='size4',fg="BRIGHTWHITE",bg="RED")

        underground =("WWWWWWWWWWW\n"
                      "WWWrrrrrWWW\n"
                      "WWrrWWWrrWW\n"
                      "WRRRRRRRRRW\n"
                      "WRRRRRRRRRW\n"
                      "WWrrWWWrrWW\n"
                      "WWWrrrrrWWW\n"
                      "WWWWWWWWWWW")
        self.print_image(underground,0,69)

        #self.add_title("buses")

        self.move_cursor(x=0)
        self.start_fg_color("GREEN")
        pos = (0,45,51, 73)
        for p,t in zip(pos,("Name","Bikes","Spaces","Updated")):
            self.move_cursor(x=p)
            self.add_text(t)
        self.end_fg_color()
        self.add_newline()


        docks_set1 = [127,86,395]
        docks_set2 = [371,332,254,354]

        bike_data = url_handler.load_json("https://api.tfl.gov.uk/bikepoint")
        docks_data = []

        for dock in docks_set1 + [-1] + docks_set2:
            if dock == -1:
                docks_data.append(("", "", "", "",""))
            else:
                dock_data = bike_data[dock]
                dock_name = dock_data['commonName'].replace(" ,",",")
                docked_bikes = "{:5d}".format(int(dock_data['additionalProperties'][6]['value']))
                empty_docks = "{:6d}".format(int(dock_data['additionalProperties'][7]['value']))
                broken_bikes = "{:6d}".format(int(dock_data['additionalProperties'][8]['value']) - int(empty_docks) - int(docked_bikes));
                data_date = dock_data['additionalProperties'][4]['modified'];
                update_time = datetime.datetime.strftime(dateutil.parser.parse(data_date).astimezone(pytz.timezone('Europe/London')),"  %H:%M")

                docks_data.append((dock_name, docked_bikes, empty_docks, update_time))

        for dock in docks_data:
            for p,t,c in zip(pos,dock[:],(None,"GREEN","LIGHTRED",None)):
                self.move_cursor(x=p)
                self.start_fg_color(c)
                self.add_text(t)
                self.end_fg_color()
            self.add_newline()

pages=[]

bike01 = BikePage("824")
