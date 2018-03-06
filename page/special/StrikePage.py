from page import Page
import config
from random import choice, randint

def join(a,b):
    return "\n".join([i+j for i,j in zip(a.split("\n"),b.split("\n"))])

def make_strike_one():
    r = randint(0,40)
    strike = ""
    strike += "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww-\n"

    if r==0:
        strike += "wrrwwwwrrwrrrrrrwrrwwrrwrrrrrrw-\n"
        strike += "wrrrwwrrrwwwrrwwwrrwrrwwrrwwwww-\n"
        strike += "wrrwrrwrrwwwrrwwwrrrrwwwrrrrwww-\n"
        strike += "wrrwwwwrrwwwrrwwwrrwrrwwrrwwwww-\n"
        strike += "wrrwwwwrrwrrrrrrwrrwwrrwrrrrrrw-\n"
        dashes = 0
    elif r==1:
        strike += "wrrrrrwwwrrrrwwwrrrrwwrrrrrwwrrrrrwwwrrrrrw-\n"
        strike += "wrrwwrrwrrwwrrwrrwwrrwrrwwrrwrrwwrrwrrwwwww-\n"
        strike += "wrrrrrwwrrwwrrwrrrrrrwrrrrrrwrrwwrrwwrrrrww-\n"
        strike += "wrrwwrrwrrwwrrwrrwwrrwrrwrrwwrrwwrrwwwwwrrw-\n"
        strike += "wrrrrrwwwrrrrwwrrwwrrwrrwwrrwrrrrrwwrrrrrww-\n"
        dashes = 12
    else:
        strike += "wrrrrrrwrrrrrrwrrrrrwwrrrrrrwrrwwrrwrrrrrrw-\n"
        strike += "wrrwwwwwwwrrwwwrrwwrrwwwrrwwwrrwrrwwrrwwwww-\n"
        strike += "wrrrrrrwwwrrwwwrrrrwwwwwrrwwwrrrrwwwrrrrwww-\n"
        strike += "wwwwwrrwwwrrwwwrrwrrwwwwrrwwwrrwrrwwrrwwwww-\n"
        strike += "wrrrrrrwwwrrwwwrrwwrrwrrrrrrwrrwwrrwrrrrrrw-\n"
        dashes = 12
    strike += "w"*dashes + "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwww-\n"

    n = randint(0,1)
    if n == 1:
        strike += "-"*dashes+"---------g----------------------\n"
        strike += "-"*dashes+"---------g----------------------\n"
        strike += "-"*dashes+"---------g------000000----------\n"
        strike += "-"*dashes+"---------g------000000----------\n"
        strike += "-"*dashes+"---------g----0000000000--------\n"
        strike += "-"*dashes+"---------g----0000000000--------\n"
        strike += "-"*dashes+"---------g----0000000000--------\n"
        strike += "-"*dashes+"---------g----0000000000--------\n"
        strike += "-"*dashes+"---------g----0000000000--------\n"
        strike += "-"*dashes+"---------g----0000000000--------\n"
        strike += "-"*dashes+"---------g------000000----------\n"
        strike += "-"*dashes+"---------g------000000----------\n"
        strike += "-"*dashes+"---------g--------00------------\n"
        strike += "-"*dashes+"---------g--------00------------\n"
        strike += "-"*dashes+"---------0000000000000----------\n"
        strike += "-"*dashes+"---------0000000000000----------\n"
        strike += "-"*dashes+"------------------00--00--------\n"
        strike += "-"*dashes+"------------------00--00--------\n"
        strike += "-"*dashes+"------------------00--00--------\n"
        strike += "-"*dashes+"------------------00--00--------\n"
        strike += "-"*dashes+"------------------00--00--------\n"
        strike += "-"*dashes+"------------------00--00--------\n"
        strike += "-"*dashes+"------------------00------------\n"
        strike += "-"*dashes+"------------------00------------\n"
        strike += "-"*dashes+"------------------00------------\n"
        strike += "-"*dashes+"------------------00------------\n"
        strike += "-"*dashes+"----------------000000----------\n"
        strike += "-"*dashes+"----------------000000----------\n"
        strike += "-"*dashes+"----------------00--00----------\n"
        strike += "-"*dashes+"----------------00--00----------\n"
        strike += "-"*dashes+"----------------00--00----------\n"
        strike += "-"*dashes+"----------------00--00----------\n"
        strike += "-"*dashes+"----------------00--00----------\n"
        strike += "-"*dashes+"----------------00--00----------\n"
        strike += "-"*dashes+"--------------0000--0000--------\n"
        strike += "-"*dashes+"--------------0000--0000--------"
    else:
        strike += "---------------------g----------"+"-"*dashes+"\n"
        strike += "---------------------g----------"+"-"*dashes+"\n"
        strike += "---------000000------g----------"+"-"*dashes+"\n"
        strike += "---------000000------g----------"+"-"*dashes+"\n"
        strike += "-------0000000000----g----------"+"-"*dashes+"\n"
        strike += "-------0000000000----g----------"+"-"*dashes+"\n"
        strike += "-------0000000000----g----------"+"-"*dashes+"\n"
        strike += "-------0000000000----g----------"+"-"*dashes+"\n"
        strike += "-------0000000000----g----------"+"-"*dashes+"\n"
        strike += "-------0000000000----g----------"+"-"*dashes+"\n"
        strike += "---------000000------g----------"+"-"*dashes+"\n"
        strike += "----------00000------g----------"+"-"*dashes+"\n"
        strike += "-----------00--------g----------"+"-"*dashes+"\n"
        strike += "-----------00--------g----------"+"-"*dashes+"\n"
        strike += "---------0000000000000----------"+"-"*dashes+"\n"
        strike += "---------0000000000000----------"+"-"*dashes+"\n"
        strike += "-------00--00-------------------"+"-"*dashes+"\n"
        strike += "-------00--00-------------------"+"-"*dashes+"\n"
        strike += "-------00--00-------------------"+"-"*dashes+"\n"
        strike += "-------00--00-------------------"+"-"*dashes+"\n"
        strike += "-------00--00-------------------"+"-"*dashes+"\n"
        strike += "-----------00-------------------"+"-"*dashes+"\n"
        strike += "-----------00-------------------"+"-"*dashes+"\n"
        strike += "-----------00-------------------"+"-"*dashes+"\n"
        strike += "-----------00-------------------"+"-"*dashes+"\n"
        strike += "---------000000-----------------"+"-"*dashes+"\n"
        strike += "---------000000-----------------"+"-"*dashes+"\n"
        strike += "---------00--00-----------------"+"-"*dashes+"\n"
        strike += "---------00--00-----------------"+"-"*dashes+"\n"
        strike += "---------00--00-----------------"+"-"*dashes+"\n"
        strike += "---------00--00-----------------"+"-"*dashes+"\n"
        strike += "---------00--00-----------------"+"-"*dashes+"\n"
        strike += "---------00--00-----------------"+"-"*dashes+"\n"
        strike += "-------0000--0000---------------"+"-"*dashes+"\n"
        strike += "-------0000--0000---------------"+"-"*dashes

    if randint(1,40) == 1:
        strike = "\n".join([i[::-1] for i in strike.split("\n")][::-1])

    return choice("rgbcmy").join(strike.split("0"))

"""strikers = [strike,strike2,
"\n".join([i[::-1] for i in strike.split("\n")][::-1])]
for i in range(1,30):
    strikers.append("\n".join(["--"*i+j for j in strike.split("\n")]))
    strikers.append("\n".join(["--"*i+j for j in strike2.split("\n")]))
for i in range(1,15):
    strikers.append("\n".join([j[2*i:] for j in strike.split("\n")]))
    strikers.append("\n".join([j[2*i:] for j in strike2.split("\n")]))"""


class StrikePage(Page):
    def __init__(self):
        super(StrikePage, self).__init__("???")
        self.name = "STRIKE"
        self.background_loaded = True

    def generate_content(self):
        out = [["-"]*80 for i in range(54)]
        for i in range(3):
            x = randint(-10,60)
            y = randint(-3,10)
            s = make_strike_one()
            for a,line in enumerate(s.split("\n")):
                for b,char in enumerate(line):
                    if char != "-" and 0 <= y+a < 54 and 0 <= x+b < 80:
                        out[y+a][x+b] = char
        self.print_image("\n".join(["".join(i) for i in out]))
