from page import Page
import config
from random import choice, randint

def join(a,b):
    return "\n".join([i+j for i,j in zip(a.split("\n"),b.split("\n"))])

def make_strike_one():
    r = randint(0,40)
    strike = ""

    if r==0:
        strike += "-------kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk\n"
        strike += "-------kwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwk\n"
        strike += "-------kw33wwww33w333333w33ww33w333333wk\n"
        strike += "-------kw333ww333www33www33w33ww33wwwwwk\n"
        strike += "-------kw33w33w33www33www3333www3333wwwk\n"
        strike += "-------kw33wwww33www33www33w33ww33wwwwwk\n"
        strike += "-------kw33wwww33w333333w33ww33w333333wk\n"
        strike += "-------kwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwk\n"
    elif 3==1:
        strike += "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk\n"
        strike += "kwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwk\n"
        strike += "kw33333www3333www3333ww33333ww33333www33333wk\n"
        strike += "kw33ww33w33ww33w33ww33w33ww33w33ww33w33wwwwwk\n"
        strike += "kw33333ww33ww33w333333w333333w33ww33ww3333wwk\n"
        strike += "kw33ww33w33ww33w33ww33w33w33ww33ww33wwwww33wk\n"
        strike += "kw33333www3333ww33ww33w33ww33w33333ww33333wwk\n"
        strike += "kwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwk\n"
    else:
        strike += "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk\n"
        strike += "kwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwk\n"
        strike += "kw333333w333333w33333ww333333w33ww33w333333wk\n"
        strike += "kw33wwwwwww33www33ww33www33www33w33ww33wwwwwk\n"
        strike += "kw333333www33www3333wwwww33www3333www3333wwwk\n"
        strike += "kwwwww33www33www33w33wwww33www33w33ww33wwwwwk\n"
        strike += "kw333333www33www33ww33w333333w33ww33w333333wk\n"
        strike += "kwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwk\n"

    n = randint(0,1)
    if n == 1:
        strike += "---------------------1----------------------\n"
        strike += "---------------------1----------------------\n"
        strike += "---------------------1------000000----------\n"
        strike += "---------------------1------000000----------\n"
        strike += "---------------------1----0000000000--------\n"
        strike += "---------------------1----0000000000--------\n"
        strike += "---------------------1----0000000000--------\n"
        strike += "---------------------1----0000000000--------\n"
        strike += "---------------------1----0000000000--------\n"
        strike += "---------------------1----0000000000--------\n"
        strike += "---------------------1------000000----------\n"
        strike += "---------------------1------000000----------\n"
        strike += "---------------------1--------00------------\n"
        strike += "---------------------1--------00------------\n"
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
        strike += "----------------------1----------\n"
        strike += "----------------------1----------\n"
        strike += "----------000000------1----------\n"
        strike += "----------000000------1----------\n"
        strike += "--------0000000000----1----------\n"
        strike += "--------0000000000----1----------\n"
        strike += "--------0000000000----1----------\n"
        strike += "--------0000000000----1----------\n"
        strike += "--------0000000000----1----------\n"
        strike += "--------0000000000----1----------\n"
        strike += "----------000000------1----------\n"
        strike += "-----------00000------1----------\n"
        strike += "------------00--------1----------\n"
        strike += "------------00--------1----------\n"
        strike += "----------0000000000000----------\n"
        strike += "----------0000000000000----------\n"
        strike += "--------00--00-------------------\n"
        strike += "--------00--00-------------------\n"
        strike += "--------00--00-------------------\n"
        strike += "--------00--00-------------------\n"
        strike += "--------00--00-------------------\n"
        strike += "------------00-------------------\n"
        strike += "------------00-------------------\n"
        strike += "------------00-------------------\n"
        strike += "------------00-------------------\n"
        strike += "----------000000-----------------\n"
        strike += "----------000000-----------------\n"
        strike += "----------00--00-----------------\n"
        strike += "----------00--00-----------------\n"
        strike += "----------00--00-----------------\n"
        strike += "----------00--00-----------------\n"
        strike += "----------00--00-----------------\n"
        strike += "----------00--00-----------------\n"
        strike += "--------0000--0000---------------\n"
        strike += "--------0000--0000---------------"

    if randint(1,40) == 1:
        strike = "\n".join([i[::-1] for i in strike.split("\n")][::-1])

    strike = choice("rgbcmy").join(strike.split("0"))
    strike = choice("rgbcmy").join(strike.split("1"))
    strike = choice("rgbcmy").join(strike.split("3"))
    return strike

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
