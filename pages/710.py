import os
from page import Page
from ceefax import Ceefax
from random import shuffle
from config import NAME
from file_handler import f_read_json
from datetime import datetime

class OxmasPage(Page):
    def __init__(self, n, title, test):
        super(OxmasPage, self).__init__(n)
        self.title = "Oxmas "+title
        self.in_index = False
        self.test = test
        self._name = title
        if NAME!="602FAX":
            self.is_enabled = False

    def generate_content(self):
        self.add_title("OXMAS "+self._name, fg="GREEN",bg="BLACK")
        db = f_read_json("db.json")
        i = 0
        for person in db:
            if self.test(person):
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
        if NAME!="602FAX":
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
        self.add_wrapped_text("Tipsy Cake, Bad-TempeGREEN Cake (Tiffin), Eton Mess, Brandy Butter, Oxmas Cake, Tiramisu, Cheese Cake, Mince Pies")
        self.add_newline()
        self.add_newline()

        self.add_text("Cheese board: ",fg="RED")
        self.add_wrapped_text("Cheddar, Stilton, Brie")
        self.add_newline()
        self.add_newline()

        self.add_text("Drinks: ",fg="GREEN")
        self.add_wrapped_text("Mulleed Wine, Selected Soft Drinks")
        self.add_newline()
        self.add_newline()


attendees = OxmasPage("710","Attendees",lambda person:person["coming"]=="yes")
santas = OxmasPage("711","Santas",lambda person:person["santa"]=="yes")
menu = OxmasMenu("712")
if NAME=="602FAX":
    attendees.title="OXMAS!"
    attendees.index_num="710-712"
    attendees.in_index=True
