import os
from page import Page
from colours import colour_print
from printer import instance as printer
from random import choice

class FoodPage(Page):
    def __init__(self,page_num):
        super(FoodPage, self).__init__(page_num)
        self.title = "FF choice"
        self.in_index = False
        self.is_enabled = False

    def generate_content(self):
        ls = ["Hare and tortoise",
              "Nando's",
              "Kitchin N1",
              "Franco Manca",
              "GBK",
              "Mestizo",
              "Curry (Drummond street)",
              "Bree Louise",
              "The Exmouth Arms",
              "The Resting Hare",
              "Jeremy Bentham",
              "Honest burgers",
              "Giraffe",
              "Thai Metro",
              "Pizza Express",
              "Prezzo",
              "Herman ze German",
              "ULU",
              "Las Iguanas"]
        
        self.content = colour_print(
                printer.text_to_ascii(choice(ls)),rainbow = True)

class OllyPage(Page):
    def __init__(self,page_num):
        super(OllyPage, self).__init__(page_num)
        self.title = "FF choice"
        self.in_index = False
        self.is_enabled = False

    def generate_content(self):
        ls = ["Curry?","Curry!","Indian?","Curry","Indian!",
              "Drummond Street","Buffet?","Curry","Pizza Hut Buffet",
              "Dosa","Vegetarian Curry","My third curry this week"]
        
        self.content = colour_print(
                printer.text_to_ascii(choice(ls)),rainbow = True)


sub_page = FoodPage("007")
sub_page1 = OllyPage("008")
