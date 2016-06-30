import os
from page import Page
from colours import colour_print
from printer import instance as printer
from random import choice

page_number = os.path.splitext(os.path.basename(__file__))[0]

class SuckPage(Page):
    def __init__(self,page_num):
        super(SuckPage, self).__init__(page_num)
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


sub_page = SuckPage(page_number)
