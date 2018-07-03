import os
from page import Page
from random import choice

class FoodPage(Page):
    def __init__(self,page_num):
        super(FoodPage, self).__init__(page_num)
        self.title = "FF choice"
        self.in_index = False
        self.enabled = False

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
        
        self.add_rainbow_title(choice(ls))

class OllyPage(Page):
    def __init__(self,page_num):
        super(OllyPage, self).__init__(page_num)
        self.title = "FF choice"
        self.in_index = False
        self.enabled = False

    def generate_content(self):
        ls = ["Curry?","Curry!","Indian?","Curry","Indian!",
              "Drummond Street","Buffet?","Curry","Pizza Hut Buffet",
              "Dosa","Vegetarian Curry","My third curry this week"]
        
        self.add_rainbow_title(choice(ls))


sub_page = FoodPage("007")
sub_page1 = OllyPage("008")
