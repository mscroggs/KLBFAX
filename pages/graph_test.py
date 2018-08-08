from page import Page
from random import randint

class GraphTestPage(Page):
    def __init__(self, page_num):
        super(GraphTestPage, self).__init__(page_num)
        self.title = "Graph Test"
        self.in_index = False
        self.enabled = False

    def generate_content(self):
        self.add_title("Graph",font='size4bold')
        self.plot(sorted([randint(1,100) for i in range(4)]),[randint(1,100) for i in range(4)],4,0,height=23,
                xtitle="Random numbers",ytitle="Different random numbers",
                xmin=0,xmax=100,ymin=0,ymax=100)

page = GraphTestPage("004")
