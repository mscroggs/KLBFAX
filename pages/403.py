import os
from page import Page
from printer import instance as printer

class PointsPage(Page):
    def __init__(self, page_num):
        super(PointsPage, self).__init__(page_num)
        self.title = "House Points"

    def generate_content(self):
        import json

        with open('/home/pi/.klb/points') as f:
            data = json.load(f)

        content = self.colours.colour_print(printer.text_to_ascii("recipes"))
        content += "\n"
        for house,points in data.items():
            content += "\n"
            content += self.colours.Foreground.YELLOW + house + self.colours.Foreground.DEFAULT
            content += " "*(20-len(house))
            content += self.colours.Foreground.GREEN + str(points) + self.colours.Foreground.DEFAULT

        self.content = content

page_number = os.path.splitext(os.path.basename(__file__))[0]
p_page = PointsPage(page_number)

class SecretPage(Page):
    def __init__(self, page_num):
        super(SecretPage, self).__init__(page_num)
        self.title = "Secret Page"
        self.is_enabled = False

    def generate_content(self):
        import json

        with open('/home/pi/.klb/points') as f:
            data = json.load(f)
        house = "Hufflepuff"
        if house in data:
            data[house]+=10
        else:
            data[house]=10
        with open('/home/pi/.klb/points','w') as f:
            data = json.dump(f)

        content = self.colours.colour_print(printer.text_to_ascii("secret page"))
        content += "\n\n"
        content += "You have found the secret page!\n\n"
        content += "Ten points to Hufflepuff!!!"

        self.content = content

s_page = SecretPage("042")
