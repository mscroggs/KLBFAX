import os
from os.path import join,expanduser
from page import Page
from printer import instance as printer

class PointsPage(Page):
    def __init__(self, page_num):
        super(PointsPage, self).__init__(page_num)
        self.title = "House Points"

    def generate_content(self):
        import json
        from operator import itemgetter
        with open(join(expanduser('~'),'.klb/points')) as f:
            data = json.load(f)

        if "Gryffindor" in data: g = str(data["Gryffindor"])
        else:                    g = "0"
        if "Hufflepuff" in data: h = str(data["Hufflepuff"])
        else:                    h = "0"
        if "Slytherin" in data:  s = str(data["Slytherin"])
        else:                    s = "0"
        if "Ravenclaw" in data:  r = str(data["Ravenclaw"])
        else:                    r = "0"

        content = self.colours.colour_print(printer.text_to_ascii("house points"))
        content += "\nWhat do points mean?\n"

        content += self.colours.colour_print_join([
                        (printer.text_to_ascii(g,False)+"\nGryffindor",
                            self.colours.Background.RED,
                            self.colours.Foreground.YELLOW+self.colours.Style.BOLD),
                        (printer.text_to_ascii(s,False)+"\nSlytherin",
                            self.colours.Style.BLINK,
                            self.colours.Foreground.GREEN)
                    ],"   ","   ")
        content += "\n"
        content += self.colours.colour_print_join([
                        (printer.text_to_ascii(r,False)+"\nRavenclaw",
                            self.colours.Background.WHITE,
                            self.colours.Foreground.BLUE+self.colours.Style.BOLD),
                        (printer.text_to_ascii(h,False)+"\nHufflepuff",
                            self.colours.Style.BLINK,
                            self.colours.Foreground.YELLOW+self.colours.Style.BOLD)
                    ],"   ","   ")
        content += "\n"
        sorted_pts = sorted(data.items(),key=itemgetter(1),reverse=True)

        content += "Full List\n"
        i=0
        for house,points in sorted_pts:
            i+=1
            content += self.colours.Foreground.YELLOW + house + self.colours.Foreground.DEFAULT
            content += " "
            content += self.colours.Foreground.GREEN + str(points) + self.colours.Foreground.DEFAULT
            if i%4==0:  content += "\n"
            else:       content += "  "

        self.content = content

page_number = os.path.splitext(os.path.basename(__file__))[0]
p_page = PointsPage(page_number)

class SecretPage(Page):
    def __init__(self, page_num):
        super(SecretPage, self).__init__(page_num)
        self.title = "Secret Page"
        self.is_enabled = False

    def generate_content(self):
        from points import add_points
        add_points("Hufflepuff",10)

        content = self.colours.colour_print(printer.text_to_ascii("secret page"))
        content += "\n\n"
        content += "You have found the secret page!\n\n"
        content += "Ten points to Hufflepuff!!!"

        self.content = content

s_page = SecretPage("042")
