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

page1 = JobPage("171","Arcade helpers","Volunteers are needed to help in the retro gaming tent.")
#page2 = JobPage("172","EMF Job 2","")
#page3 = JobPage("173","EMF Job 3","")
#page4 = JobPage("174","EMF Job 4","")
#page5 = JobPage("175","EMF Job 5","")
#page6 = JobPage("176","EMF Job 6","")
#page7 = JobPage("177","EMF Job 7","")
#page8 = JobPage("178","EMF Job 8","")
#page9 = JobPage("179","EMF Job 9","")
#page9 = JobPage("180","EMF Job 10","")
#page9 = JobPage("181","EMF Job 11","")
#page9 = JobPage("182","EMF Job 12","")
#page9 = JobPage("183","EMF Job 13","")
#page9 = JobPage("184","EMF Job 14","")
