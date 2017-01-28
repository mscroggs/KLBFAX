from page import Page
from random import choice

class TubePage(Page):
    def __init__(self,page_num):
        super(TubePage, self).__init__(page_num)
        self.title = "Tube Line Status"

    def background(self):
        import tubestatus
        # Create a new status object for retrieving data
        self.current_status = tubestatus.Status()

    def generate_content(self):
        self.add_title("Tube Lines")
        # Get a list of tube lines
        lines = self.current_status.list_lines()
        # Loop through the lines and print the status of each one
        lines_tube = [lines[i] for i in [1,2,12,4,10,0,3,14,5,7,11]]
        lines_other = [lines[i] for i in [8,6,13,9]]
        colours_tube = ["ORANGE","RED","YELLOW","GREEN","PINK","GREY","MAGENTA","DEFAULT","BLUE","LIGHTBLUE","LIGHTCYAN"]
        colours_tube_text = ["WHITE","WHITE","BLACK","BLACK","BLACK","WHITE","WHITE","WHITE","WHITE","WHITE","BLACK"]

        colours_other = ["CYAN","ORANGE","BLUE","LIGHTGREEN"]
        colours_other_text = ["BLACK","BLACK","WHITE","BLACK"]

        mapping = [ ('There is a GOOD SERVICE on the rest of the line.', ''),
                    ('GOOD SERVICE on the rest of the line.', ''),
                    ('There is a GOOD SERVICE on all other routes.', ''),
                    ('GOOD SERVICE on all other routes.', ''),
                    ('GOOD SERVICE on other London Overground routes.', ''),
                    ('GOOD SERVICE on other London Overground routes', ''),
                    ('The service will resume again at 0615 on Monday.', ''),
                    ('The service will resume again at 0615 tomorrow.', ''),
                    ('The service will resume again at 0615.', ''),
                    ('Train service will resume at 06:15 tomorrow.', ''),
                    ('No service between ', ''),
                    #('Minor delays ', ''),
                    (' due to planned engineering work.', ''),
                    (' due to planned work.', ''),
                    #('due to ', ''),
                    ('King\'s Cross St. Pancras', 'KX'),
                    ('Kings Cross St. Pancras', 'KX'),
                    ('Tottenham Court Road', 'TCR'),
                    ('Highbury & Islington', 'H&I'),
                    ('Harrow & Wealdstone', 'H&W'),
                    ('Cross', 'X'),
                    ('Road', 'Rd'),
                    ('Square', 'Sq'),
                    ('Street', 'St'),
                    ('Junction', 'Jn'),
                    ('Town', 'Tn'),
                    ('Park', 'Pk'),
                    ('Lane', 'Ln'),
                    ('Hill', 'Hl'),
                    ('Central','Ctl'),
                    ('North ','N '),
                    ('South ','S '),
                    ('East ','E '),
                    ('West ','W '),
                    (' and ','-'),
                    ('between ',''),
                    (' to ','-')]

        content_bad_service = ""
        content_good_service = ""
        good = []
        for line,fg,bg in zip(lines_tube + lines_other,colours_tube_text+colours_other_text,colours_tube+colours_other):
            desc = self.current_status.get_status(line).description
            if desc == "Good Service":
                good.append((line,fg,bg))
            else:
                self.start_fg_color(fg)
                self.start_bg_color(bg)
                self.add_text(" " + str(line).replace("and","&") +" "*(20-len(str(line).replace("and","&"))))
                self.end_bg_color()
                self.end_fg_color()
                if desc == "Minor Delays":
                    self.start_fg_color("YELLOW")
                elif desc == "Part Closure":
                    self.start_fg_color("ORANGE")
                else:
                    self.start_fg_color("LIGHTRED")

                full_description = " "
                full_description += self.current_status.get_status(line).description
                description = self.current_status.get_status(line).status_details
                for k, v in mapping:
                    description = description.replace(k, v)
                if len(description)>1:
                    full_description += ": " + description
                self.add_wrapped_text(full_description,pre=24)
                self.end_fg_color()
                self.add_newline()

        self.add_newline()

        for line,fg,bg in good:
            desc = self.current_status.get_status(line).description
            self.start_fg_color(fg)
            self.start_bg_color(bg)
            self.add_text(" " + str(line).replace("and","&") +" "*(20-len(str(line).replace("and","&"))))
            self.end_bg_color()
            self.start_fg_color("GREEN")

            self.add_wrapped_text(" Good service",pre=24)
            self.end_fg_color()
            self.add_newline()

page = TubePage("315")
