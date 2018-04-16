from page import Page
import random

class httpPage(Page):
    def __init__(self, number, error):
        super(httpPage, self).__init__(number)
        self.title = error
        self.in_index = False
        self.error_text = error

    def generate_content(self):
        self.add_title(self.number + " " + self.error_text, font="size4")

        self.print_image("------------------------------------------------bb---------\n"
                         "--------------------------------------bbbbbbbbbbbbbbbbb----\n"
                         "---------------------------bbbbbbbbbbbbbbbbbbb-------bbbb--\n"
                         "---------------------bbbbbbbbbbbbbbbbbbbbbbb------------b--\n"
                         "-----------------bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb--------bb-\n"
                         "---------------bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb------bb-\n"
                         "-------------bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb----b--\n"
                         "-----------bbbbbb-bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb--b--\n"
                         "---------bbbbb--bbbbbbbbbbbbbb-----bbbbbbbbbbbbbbbbbbbbb---\n"
                         "--------bbbb--bbbbbbbbbbbb-------------bbbbbbbbbbbbbbbbbb--\n"
                         "-------bb---bbbbbbbbbbb------------------bbbbbbbbbbbbbbbb--\n"
                         "-------b---bbbbbbbbbbb---------------------bbbbbbbbbbbbbbb-\n"
                         "---------bbbbbbbbbbbb----------------------bbbbbbbbbbbbbbbb\n"
                         "--------bbbbbbbbbbbbb-----------------------bbbbbbbbbbbbbbb\n"
                         "-------bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                         "-----bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                         "----bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
                         "---bbbbbbbbbbbbbbbbbb--------------------------------------\n"
                         "---bbbbbbbbbbbbbbbbbb--------------------------------------\n"
                         "--bbbbbbbbbbbbbbbbbbbb-------------------------------------\n"
                         "-bbbbbbbbbbbbbbbbbbbbbb--------------------bbbbbbbbbbbbbbb-\n"
                         "-bbbbb--bbbbbbbbbbbbbbbb------------------bbbbbbbbbbbbbbb--\n"
                         "bbbbb----bbbbbbbbbbbbbbbbbb------------bbbbbbbbbbbbbbbbb---\n"
                         "bbbb------bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb----\n"
                         "bbbb--------bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb------\n"
                         "bbbb----------bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb--------\n"
                         "bbbb------------bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb----------\n"
                         "bbbbb-------------bbbbbbbbbbbbbbbbbbbbbbbbbbbb-------------\n"
                         "--bbbbbbb--bbbbbb------bbbbbbbbbbbbbbbbbbb-----------------",random.randrange(5,15),random.randrange(0,20))


p1 = httpPage("400","Bad Request")
p2 = httpPage("401","Unauthorised")
p3 = httpPage("402","Payment Required")
p4 = httpPage("403","Forbidden")
p5 = httpPage("404","Not Found")
p6 = httpPage("405","Method Not Allowed")
p7 = httpPage("406","Not Acceptable")
p8 = httpPage("407","Proxy Authentication Required")
p9 = httpPage("408","Request Timeout")
pa = httpPage("409","Conflict")
pb = httpPage("410","Gone")
pc = httpPage("411","Length Required")
pd = httpPage("412","Precondition Failed")
pe = httpPage("413","Payload Too Large")
pf = httpPage("414","URI Too Long")
pg = httpPage("415","Unsupported Media Type")
ph = httpPage("416","Range Not Satisfiable")
pi = httpPage("417","Expectation Failed")
pj = httpPage("418","I'm a Teapot")
pk = httpPage("421","Misdirected Request")
pl = httpPage("422","Unprocessable Entity")
pm = httpPage("423","Locked")
pn = httpPage("424","Failed Dependency")
po = httpPage("426","Upgrade Required")
pp = httpPage("428","Precondition Required")
pq = httpPage("429","Too Many Requests")
pr = httpPage("431","Request Header Fields Too Large")
ps = httpPage("451","Unavailable for Legal Reasons")
