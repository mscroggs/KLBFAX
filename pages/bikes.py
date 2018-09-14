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
        pos = (0,45,51, 67)
        for p,t in zip(pos,("Name","Bikes","Spaces","Last updated")):
            self.move_cursor(x=p)
            self.add_text(t)
        self.end_fg_color()
        self.add_newline()


        docks_set1 = ['BikePoints_131','BikePoints_90','BikePoints_425']
        docks_set2 = ['BikePoints_392','BikePoints_350','BikePoints_266','BikePoints_373']

        bike_data = url_handler.load_json("https://api.tfl.gov.uk/bikepoint")

        docks_dict = dict()
        for dock in bike_data:
            docks_dict[dock['id']] = [dock['commonName'],int(dock['additionalProperties'][6]['value']), int(dock['additionalProperties'][7]['value']), int(dock['additionalProperties'][8]['value']), dock['additionalProperties'][4]['modified']  ]

        docks_data = []

        for dock_id in docks_set1 + [-1] + docks_set2:
            if dock_id == -1:
                docks_data.append(("", "", "", "",""))
            else:
                dock_data = docks_dict[dock_id]
                dock_name = dock_data[0].replace(" ,",",")
                docked_bikes = "{:5d}".format(dock_data[1])
                empty_docks = "{:6d}".format(dock_data[2])
                broken_bikes = "{:6d}".format((dock_data[3]) - int(empty_docks) - int(docked_bikes));
                data_date = dock_data[4];
                update_time = datetime.datetime.strftime(dateutil.parser.parse(data_date).astimezone(pytz.timezone('Europe/London')),"  %H:%M")
                mins_ago = (datetime.datetime.now(pytz.utc) - dateutil.parser.parse(data_date)).seconds//60
                ago = "  " + "{:2d}".format(mins_ago) + " min ago"

                docks_data.append((dock_name, docked_bikes, empty_docks, ago))

        for dock in docks_data:
            for p,t,c in zip(pos,dock[:],(None,"GREEN","LIGHTRED",None)):
                self.move_cursor(x=p)
                self.start_fg_color(c)
                self.add_text(t)
                self.end_fg_color()
            self.add_newline()

pages=[]

bike01 = BikePage("824")
