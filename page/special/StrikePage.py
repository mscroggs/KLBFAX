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
        strike += "wwwwwwwwwwwwwrrwwwwrrwrrrrrrwrrwwrrwrrrrrrw-\n"
        strike += "wwwwwwwwwwwwwrrrwwrrrwwwrrwwwrrwrrwwrrwwwww-\n"
        strike += "wwwwwwwwwwwwwrrwrrwrrwwwrrwwwrrrrwwwrrrrwww-\n"
        strike += "wwwwwwwwwwwwwrrwwwwrrwwwrrwwwrrwrrwwrrwwwww-\n"
        strike += "wwwwwwwwwwwwwrrwwwwrrwrrrrrrwrrwwrrwrrrrrrw-\n"
    elif r==1:
        strike += "wrrrrrwwwrrrrwwwrrrrwwrrrrrwwrrrrrwwwrrrrrw-\n"
        strike += "wrrwwrrwrrwwrrwrrwwrrwrrwwrrwrrwwrrwrrwwwww-\n"
        strike += "wrrrrrwwrrwwrrwrrrrrrwrrrrrrwrrwwrrwwrrrrww-\n"
        strike += "wrrwwrrwrrwwrrwrrwwrrwrrwrrwwrrwwrrwwwwwrrw-\n"
        strike += "wrrrrrwwwrrrrwwrrwwrrwrrwwrrwrrrrrwwrrrrrww-\n"
    else:
        strike += "wrrrrrrwrrrrrrwrrrrrwwrrrrrrwrrwwrrwrrrrrrw-\n"
        strike += "wrrwwwwwwwrrwwwrrwwrrwwwrrwwwrrwrrwwrrwwwww-\n"
        strike += "wrrrrrrwwwrrwwwrrrrwwwwwrrwwwrrrrwwwrrrrwww-\n"
        strike += "wwwwwrrwwwrrwwwrrwrrwwwwrrwwwrrwrrwwrrwwwww-\n"
        strike += "wrrrrrrwwwrrwwwrrwwrrwrrrrrrwrrwwrrwrrrrrrw-\n"
    strike += "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww-\n"

    n = randint(0,1)
    if n == 1:
        strike += "---------------------g----------------------\n"
        strike += "---------------------g----------------------\n"
        strike += "---------------------g------000000----------\n"
        strike += "---------------------g------000000----------\n"
        strike += "---------------------g----0000000000--------\n"
        strike += "---------------------g----0000000000--------\n"
        strike += "---------------------g----0000000000--------\n"
        strike += "---------------------g----0000000000--------\n"
        strike += "---------------------g----0000000000--------\n"
        strike += "---------------------g----0000000000--------\n"
        strike += "---------------------g------000000----------\n"
        strike += "---------------------g------000000----------\n"
        strike += "---------------------g--------00------------\n"
        strike += "---------------------g--------00------------\n"
        strike += "---------------------0000000000000----------\n"
        strike += "---------------------0000000000000----------\n"
        strike += "------------------------------00--00--------\n"
        strike += "------------------------------00--00--------\n"
        strike += "------------------------------00--00--------\n"
        strike += "------------------------------00--00--------\n"
        strike += "------------------------------00--00--------\n"
        strike += "------------------------------00--00--------\n"
        strike += "------------------------------00------------\n"
        strike += "------------------------------00------------\n"
        strike += "------------------------------00------------\n"
        strike += "------------------------------00------------\n"
        strike += "----------------------------000000----------\n"
        strike += "----------------------------000000----------\n"
        strike += "----------------------------00--00----------\n"
        strike += "----------------------------00--00----------\n"
        strike += "----------------------------00--00----------\n"
        strike += "----------------------------00--00----------\n"
        strike += "----------------------------00--00----------\n"
        strike += "----------------------------00--00----------\n"
        strike += "--------------------------0000--0000--------\n"
        strike += "--------------------------0000--0000--------"
    else:
        strike += "---------------------g----------------------\n"
        strike += "---------------------g----------------------\n"
        strike += "---------000000------g----------------------\n"
        strike += "---------000000------g----------------------\n"
        strike += "-------0000000000----g----------------------\n"
        strike += "-------0000000000----g----------------------\n"
        strike += "-------0000000000----g----------------------\n"
        strike += "-------0000000000----g----------------------\n"
        strike += "-------0000000000----g----------------------\n"
        strike += "-------0000000000----g----------------------\n"
        strike += "---------000000------g----------------------\n"
        strike += "----------00000------g----------------------\n"
        strike += "-----------00--------g----------------------\n"
        strike += "-----------00--------g----------------------\n"
        strike += "---------0000000000000----------------------\n"
        strike += "---------0000000000000----------------------\n"
        strike += "-------00--00-------------------------------\n"
        strike += "-------00--00-------------------------------\n"
        strike += "-------00--00-------------------------------\n"
        strike += "-------00--00-------------------------------\n"
        strike += "-------00--00-------------------------------\n"
        strike += "-----------00-------------------------------\n"
        strike += "-----------00-------------------------------\n"
        strike += "-----------00-------------------------------\n"
        strike += "-----------00-------------------------------\n"
        strike += "---------000000-----------------------------\n"
        strike += "---------000000-----------------------------\n"
        strike += "---------00--00-----------------------------\n"
        strike += "---------00--00-----------------------------\n"
        strike += "---------00--00-----------------------------\n"
        strike += "---------00--00-----------------------------\n"
        strike += "---------00--00-----------------------------\n"
        strike += "---------00--00-----------------------------\n"
        strike += "-------0000--0000---------------------------\n"
        strike += "-------0000--0000---------------------------"

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
        s = make_strike_one()
        t = make_strike_one()
        u = make_strike_one()
        n = randint(0,15)
        s = "\n".join([j[2*n:] for j in s.split("\n")])
        self.print_image(join(s,join(t,u)))
