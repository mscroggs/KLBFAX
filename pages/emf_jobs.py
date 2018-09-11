from page import Page
from random import shuffle

class JobPage(Page):
    def __init__(self, page_num, title, desc):
        super(JobPage, self).__init__(page_num)
        self.title = title
        self.desc = desc
        self.in_index = False
        self.importance = 0

    def generate_content(self):
        self.add_title("Jobs: "+self.title,fg="BLACK",bg="ORANGE",font="size4")
        self.add_newline()
        self.add_wrapped_text(self.desc)
        self.add_newline()
        self.add_newline()
        self.add_text("Sign up for this role now at the volunteering desk\n  or online at emfcamp.org/volunteer",fg="BRIGHTWHITE")

page1 = JobPage("171","Badge Helper","Fix, replace and troubleshoot badges and their software.")
page2 = JobPage("172","Bar","Help run the bar. Serve drinks, take payment, keep it clean.")
page3 = JobPage("173","Car Parking","Help park cars and get people on/off site.")
page4 = JobPage("174","Catering","Help our excellent catering team provide food for all the volunteers.")
page5 = JobPage("175","Entrance Steward","Greet people, check their tickets and help them get on site.")
page6 = JobPage("176","Green Room","Make sure speakers get where they need to be with what they need.")
page7 = JobPage("177","Herald","Introduce talks and manage speakers at stage.")
page8 = JobPage("178","Info Desk","Be a point of contact for attendees. Either helping with finding things or just getting an idea for what's on")
page10 = JobPage("179","NOC","Plug/Unplug DKs")
page11 = JobPage("180","Stage: Audio/Visual","Run the audio for a stage. Make sure mics are working and that presentations work.")
page12 = JobPage("181","Stage: Camera Operator","Point, focus and expose the camera, then lock off shot and monitor it.")
page13 = JobPage("182","Stage: Vision Mixer","Vision mix the output to screen and to stream.")
page14 = JobPage("183","Tent Steward","Check the various tents (e.g. Arcade, Lounge, Spillout) are clean and everything's OK.")
page16 = JobPage("184","Youth Workshop Helper","Help support our youth workshop leaders and participants.")
