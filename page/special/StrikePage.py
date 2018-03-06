from page import Page
import config
from random import choice, randint

def join(a,b):
    return "\n".join([i+j for i,j in zip(a.split("\n"),b.split("\n"))])

def make_strike_one():
    r = randint(0,40)
    strike = ""

    if r==0:
        strike += "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk\n"
        strike += "kwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwk\n"
        strike += "kwrrwwwwrrwrrrrrrwrrwwrrwrrrrrrwk\n"
        strike += "kwrrrwwrrrwwwrrwwwrrwrrwwrrwwwwwk\n"
        strike += "kwrrwrrwrrwwwrrwwwrrrrwwwrrrrwwwk\n"
        strike += "kwrrwwwwrrwwwrrwwwrrwrrwwrrwwwwwk\n"
        strike += "kwrrwwwwrrwrrrrrrwrrwwrrwrrrrrrwk\n"
        strike += "kwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwk\n"
    elif r==1:
        strike += "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk\n"
        strike += "kwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwk\n"
        strike += "kwrrrrrwwwrrrrwwwrrrrwwrrrrrwwrrrrrwwwrrrrrwk\n"
        strike += "kwrrwwrrwrrwwrrwrrwwrrwrrwwrrwrrwwrrwrrwwwwwk\n"
        strike += "kwrrrrrwwrrwwrrwrrrrrrwrrrrrrwrrwwrrwwrrrrwwk\n"
        strike += "kwrrwwrrwrrwwrrwrrwwrrwrrwrrwwrrwwrrwwwwwrrwk\n"
        strike += "kwrrrrrwwwrrrrwwrrwwrrwrrwwrrwrrrrrwwrrrrrwwk\n"
        strike += "kwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwk\n"
    else:
        strike += "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk\n"
        strike += "kwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwk\n"
        strike += "kwrrrrrrwrrrrrrwrrrrrwwrrrrrrwrrwwrrwrrrrrrwk\n"
        strike += "kwrrwwwwwwwrrwwwrrwwrrwwwrrwwwrrwrrwwrrwwwwwk\n"
        strike += "kwrrrrrrwwwrrwwwrrrrwwwwwrrwwwrrrrwwwrrrrwwwk\n"
        strike += "kwwwwwrrwwwrrwwwrrwrrwwwwrrwwwrrwrrwwrrwwwwwk\n"
        strike += "kwrrrrrrwwwrrwwwrrwwrrwrrrrrrwrrwwrrwrrrrrrwk\n"
        strike += "kwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwk\n"

    n = randint(0,1)
    if n == 1:
        strike += "---------g----------------------\n"
        strike += "---------g----------------------\n"
        strike += "---------g------000000----------\n"
        strike += "---------g------000000----------\n"
        strike += "---------g----0000000000--------\n"
        strike += "---------g----0000000000--------\n"
        strike += "---------g----0000000000--------\n"
        strike += "---------g----0000000000--------\n"
        strike += "---------g----0000000000--------\n"
        strike += "---------g----0000000000--------\n"
        strike += "---------g------000000----------\n"
        strike += "---------g------000000----------\n"
        strike += "---------g--------00------------\n"
        strike += "---------g--------00------------\n"
        strike += "---------0000000000000----------\n"
        strike += "---------0000000000000----------\n"
        strike += "------------------00--00--------\n"
        strike += "------------------00--00--------\n"
        strike += "------------------00--00--------\n"
        strike += "------------------00--00--------\n"
        strike += "------------------00--00--------\n"
        strike += "------------------00--00--------\n"
        strike += "------------------00------------\n"
        strike += "------------------00------------\n"
        strike += "------------------00------------\n"
        strike += "------------------00------------\n"
        strike += "----------------000000----------\n"
        strike += "----------------000000----------\n"
        strike += "----------------00--00----------\n"
        strike += "----------------00--00----------\n"
        strike += "----------------00--00----------\n"
        strike += "----------------00--00----------\n"
        strike += "----------------00--00----------\n"
        strike += "----------------00--00----------\n"
        strike += "--------------0000--0000--------\n"
        strike += "--------------0000--0000--------"
    else:
        strike += "---------------------g----------\n"
        strike += "---------------------g----------\n"
        strike += "---------000000------g----------\n"
        strike += "---------000000------g----------\n"
        strike += "-------0000000000----g----------\n"
        strike += "-------0000000000----g----------\n"
        strike += "-------0000000000----g----------\n"
        strike += "-------0000000000----g----------\n"
        strike += "-------0000000000----g----------\n"
        strike += "-------0000000000----g----------\n"
        strike += "---------000000------g----------\n"
        strike += "----------00000------g----------\n"
        strike += "-----------00--------g----------\n"
        strike += "-----------00--------g----------\n"
        strike += "---------0000000000000----------\n"
        strike += "---------0000000000000----------\n"
        strike += "-------00--00-------------------\n"
        strike += "-------00--00-------------------\n"
        strike += "-------00--00-------------------\n"
        strike += "-------00--00-------------------\n"
        strike += "-------00--00-------------------\n"
        strike += "-----------00-------------------\n"
        strike += "-----------00-------------------\n"
        strike += "-----------00-------------------\n"
        strike += "-----------00-------------------\n"
        strike += "---------000000-----------------\n"
        strike += "---------000000-----------------\n"
        strike += "---------00--00-----------------\n"
        strike += "---------00--00-----------------\n"
        strike += "---------00--00-----------------\n"
        strike += "---------00--00-----------------\n"
        strike += "---------00--00-----------------\n"
        strike += "---------00--00-----------------\n"
        strike += "-------0000--0000---------------\n"
        strike += "-------0000--0000---------------"

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
        y = 0
        for i in range(3):
            x = randint(-10,50)
            y = randint(y,y+5)
            s = make_strike_one()
            for a,line in enumerate(s.split("\n")):
                for b,char in enumerate(line):
                    if char != "-" and 0 <= y+a < 54 and 0 <= x+b < 80:
                        out[y+a][x+b] = char
        self.print_image("\n".join(["".join(i) for i in out]))
