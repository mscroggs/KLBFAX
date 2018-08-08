from page import Page
from random import shuffle

class JobPage(Page):
    def __init__(self, page_num, title, desc):
        super(JobPage, self).__init__(page_num)
        self.title = title
        self.desc = desc
        self.in_index = False
        self.importance = 4

    def generate_content(self):
        self.add_title("Jobs: "+self.title,fg="BLACK",bg="ORANGE",font="size4")
        self.add_newline()
        self.add_text(self.desc)
        self.add_newline()
        self.add_newline()
        self.add_text("Sign up for this role now at the volunteering desk or online at emfcamp.org/TBC",fg="BRIGHTWHITE")

#TODO: fill these in with volunteer roles
page1 = JobPage("161","Arcade helpers","Volunteers are needed to help in the retro gaming tent.")
#page2 = JobPage("162","EMF Job 2","")
#page3 = JobPage("163","EMF Job 3","")
#page4 = JobPage("164","EMF Job 4","")
#page5 = JobPage("165","EMF Job 5","")
#page6 = JobPage("166","EMF Job 6","")
#page7 = JobPage("167","EMF Job 7","")
#page8 = JobPage("168","EMF Job 8","")
#page9 = JobPage("169","EMF Job 9","")
