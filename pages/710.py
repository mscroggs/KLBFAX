import os
from page import Page
from ceefax import Ceefax
from random import shuffle
from config import NAME,is_oxmas,is_oxmas_day
from file_handler import f_read_json
from datetime import datetime

class OxmasPage(Page):
    def __init__(self, n, title, test, verb):
        super(OxmasPage, self).__init__(n)
        self.title = "Oxmas "+title
        self.in_index = False
        self.test = test
        self._name = title
        self.verb = verb
        if NAME!="28JHFAX":
            self.is_enabled = False

    def generate_content(self):
        self.add_title("OXMAS "+self._name, fg="GREEN",bg="BLACK")
        ls = [p for p in f_read_json("db.json") if self.test(p)]
        self.add_newline()
        self.start_fg_color("GREEN")
        self.add_text(str(len(ls)))
        self.end_fg_color()
        self.add_text(" people are "+self.verb)
        self.add_newline()
        i = 0
        for person in ls:
            self.add_text(person["name"][1] + " (" + person["name"][0] + ")")
            if i%2==0:
                self.move_cursor(x=35)
            else:
                self.add_newline()
            i += 1

class OxmasMenu(Page):
    def __init__(self, n):
        super(OxmasMenu, self).__init__(n)
        self.title = "Oxmas Menu"
        self.in_index = False
        if NAME!="28JHFAX":
            self.is_enabled = False

    def generate_content(self):
        self.add_title("OXMAS Menu", fg="GREEN",bg="BLACK")
        self.add_newline()
        self.add_text("Meat: ",fg="RED")
        self.add_wrapped_text("Chicken, Lamb, Ham, Pork, Beef, Sausages wrapped in Bacon")
        self.add_newline()
        self.add_newline()

        self.add_text("Vegetarian: ",fg="GREEN")
        self.add_wrapped_text("Amazing bread thingy")
        self.add_newline()
        self.add_newline()

        self.add_text("On the side: ",fg="RED")
        self.add_wrapped_text("Roast Potatoes, Parsnips, Stuffing, Peas, Carrots, Leeks, Broccoli, Cauliflower, Brussels Sprouts")
        self.add_newline()
        self.add_newline()

        self.add_text("Sauces: ",fg="GREEN")
        self.add_wrapped_text("Meaty Gravy, Veggie Gravy, Mint Sauce, Cranberry Sauce")
        self.add_newline()
        self.add_newline()

        self.add_text("Puddings: ",fg="RED")
        self.add_wrapped_text("Tipsy Cake, Bad-Tempered Cake (Tiffin), Eton Mess, Brandy Butter, Oxmas Cake, Tiramisu, Cheese Cake, Mince Pies")
        self.add_newline()
        self.add_newline()

        self.add_text("Cheese board: ",fg="GREEN")
        self.add_wrapped_text("Cheddar, Stilton, Brie")
        self.add_newline()
        self.add_newline()

        self.add_text("Drinks: ",fg="RED")
        self.add_wrapped_text("Mulled Wine, Selected Soft Drinks")
        self.add_newline()
        self.add_newline()

class OxmasTimetable(Page):
    def __init__(self, n):
        super(OxmasTimetable, self).__init__(n)
        self.title = "Oxmas Timetable"
        self.in_index = False
        if NAME!="28JHFAX":
            self.is_enabled = False

    def generate_content(self):
        self.add_title("OXMAS Timetable", fg="GREEN",bg="BLACK")
        self.add_newline()
        for line in [
                    "11:00 Arrivals start",
                    "13:00 Dinner is served",
                    "14:00 Pudding",
                    "15:00 The mandatory Oxmas walk (optional)",
                    "16:00 The Queen's Speech (on iPlayer)",
                    "16:10 Stockings, secret santa & presents",
                    "17:00 Oxmas Quiz",
                    "18:00 Prizes",
                    "18:30 Leftover food",
                    "20:00 More leftover food",
                    "21:00 More leftover food",
                    "23:00 More leftover food",
                    ]:
            self.add_text(line[:6],fg="RED")
            self.add_text(line[6:])
            self.add_newline()

class OxmasNOW(Page):
    def __init__(self, n):
        super(OxmasNOW, self).__init__(n)
        self.title = "Oxmas Now"
        self.in_index = False
        self.is_enabled = False

    def generate_content(self):
        if is_oxmas():
            self.is_enabled = True
        else:
            self.is_enabled = False
        self.add_title("OXMAS NOW", fg="GREEN",bg="BLACK")
        self.add_newline()
        if is_oxmas_day():
            now = datetime.now()
            self.add_title("IT IS TIME FOR",fg="RED",bg="BLACK")
            if now.hour < 11:
                self.add_title("BREAKFAST",fg="RED",bg="BLACK")
            elif now.hour < 13:
                self.add_title("ARRIVALS",fg="RED",bg="BLACK")
            elif now.hour < 14:
                self.add_title("OXMAS DINNER",fg="RED",bg="BLACK")
            elif now.hour < 15:
                self.add_title("THE OXMAS WALK",fg="RED",bg="BLACK")
            elif now.hour == 16 and now.minute <= 20:
                self.add_title("The Queen's speech",fg="RED",bg="BLACK")
            elif now.hour == 16:
                self.add_title("Presents",fg="RED",bg="BLACK")
            elif now.hour < 18:
                self.add_title("The oxmas quiz",fg="RED",bg="BLACK")
            elif now.hour == 18 and self.minute <= 30:
                self.add_title("prizes",fg="RED",bg="BLACK")
            else:
                self.add_title("leftover food",fg="RED",bg="BLACK")
        else:
            self.add_title("TODAY IS NOT",fg="RED",bg="BLACK")
            self.add_title("OXMAS DAY",fg="RED",bg="BLACK")



attendees = OxmasPage("710","Attendees",lambda person:person["coming"]=="yes","coming to Oxmas")
santas = OxmasPage("711","Santas",lambda person:person["santa"]=="yes","playing secret santa")
menu = OxmasMenu("712")
timetable = OxmasTimetable("713")
now = OxmasNOW("714")

if NAME == "28JHFAX":
    attendees.title = "OXMAS!"
    attendees.index_num = "710-714"
    attendees.in_index = True
