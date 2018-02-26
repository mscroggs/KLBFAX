from page import Page
import config
from random import choice, randint
strike = ""
strike += "----wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww-\n"
strike += "----wrrrrrrwrrrrrrwrrrrrwwrrrrrrwrrwwrrwrrrrrrw-\n"
strike += "----wrrwwwwwwwrrwwwrrwwrrwwwrrwwwrrwrrwwrrwwwww-\n"
strike += "----wrrrrrrwwwrrwwwrrrrwwwwwrrwwwrrrrwwwrrrrwww-\n"
strike += "----wwwwwrrwwwrrwwwrrwrrwwwwrrwwwrrwrrwwrrwwwww-\n"
strike += "----wrrrrrrwwwrrwwwrrwwrrwrrrrrrwrrwwrrwrrrrrrw-\n"
strike += "----wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww-\n"
strike += "-------------------------g----------------------\n"
strike += "-------------------------g----------------------\n"
strike += "-------------------------g------000000----------\n"
strike += "-------------------------g------000000----------\n"
strike += "-------------------------g----0000000000--------\n"
strike += "-------------------------g----0000000000--------\n"
strike += "-------------------------g----0000000000--------\n"
strike += "-------------------------g----0000000000--------\n"
strike += "-------------------------g----0000000000--------\n"
strike += "-------------------------g----0000000000--------\n"
strike += "-------------------------g------000000----------\n"
strike += "-------------------------g------000000----------\n"
strike += "-------------------------g--------00------------\n"
strike += "-------------------------g--------00------------\n"
strike += "-------------------------0000000000000----------\n"
strike += "-------------------------0000000000000----------\n"
strike += "----------------------------------00--00--------\n"
strike += "----------------------------------00--00--------\n"
strike += "----------------------------------00--00--------\n"
strike += "----------------------------------00--00--------\n"
strike += "----------------------------------00--00--------\n"
strike += "----------------------------------00--00--------\n"
strike += "----------------------------------00------------\n"
strike += "----------------------------------00------------\n"
strike += "----------------------------------00------------\n"
strike += "----------------------------------00------------\n"
strike += "--------------------------------000000----------\n"
strike += "--------------------------------000000----------\n"
strike += "--------------------------------00--00----------\n"
strike += "--------------------------------00--00----------\n"
strike += "--------------------------------00--00----------\n"
strike += "--------------------------------00--00----------\n"
strike += "--------------------------------00--00----------\n"
strike += "--------------------------------00--00----------\n"
strike += "------------------------------0000--0000--------\n"
strike += "------------------------------0000--0000--------"

strike2 = ""
strike2 += "----wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww-\n"
strike2 += "----wrrrrrrwrrrrrrwrrrrrwwrrrrrrwrrwwrrwrrrrrrw-\n"
strike2 += "----wrrwwwwwwwrrwwwrrwwrrwwwrrwwwrrwrrwwrrwwwww-\n"
strike2 += "----wrrrrrrwwwrrwwwrrrrwwwwwrrwwwrrrrwwwrrrrwww-\n"
strike2 += "----wwwwwrrwwwrrwwwrrwrrwwwwrrwwwrrwrrwwrrwwwww-\n"
strike2 += "----wrrrrrrwwwrrwwwrrwwrrwrrrrrrwrrwwrrwrrrrrrw-\n"
strike2 += "----wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww-\n"
strike2 += "-------------------------g----------------------\n"
strike2 += "-------------------------g----------------------\n"
strike2 += "-------------000000------g----------------------\n"
strike2 += "-------------000000------g----------------------\n"
strike2 += "-----------0000000000----g----------------------\n"
strike2 += "-----------0000000000----g----------------------\n"
strike2 += "-----------0000000000----g----------------------\n"
strike2 += "-----------0000000000----g----------------------\n"
strike2 += "-----------0000000000----g----------------------\n"
strike2 += "-----------0000000000----g----------------------\n"
strike2 += "-------------000000------g----------------------\n"
strike2 += "--------------00000------g----------------------\n"
strike2 += "---------------00--------g----------------------\n"
strike2 += "---------------00--------g----------------------\n"
strike2 += "-------------0000000000000----------------------\n"
strike2 += "-------------0000000000000----------------------\n"
strike2 += "-----------00--00-------------------------------\n"
strike2 += "-----------00--00-------------------------------\n"
strike2 += "-----------00--00-------------------------------\n"
strike2 += "-----------00--00-------------------------------\n"
strike2 += "-----------00--00-------------------------------\n"
strike2 += "---------------00-------------------------------\n"
strike2 += "---------------00-------------------------------\n"
strike2 += "---------------00-------------------------------\n"
strike2 += "---------------00-------------------------------\n"
strike2 += "-------------000000-----------------------------\n"
strike2 += "-------------000000-----------------------------\n"
strike2 += "-------------00--00-----------------------------\n"
strike2 += "-------------00--00-----------------------------\n"
strike2 += "-------------00--00-----------------------------\n"
strike2 += "-------------00--00-----------------------------\n"
strike2 += "-------------00--00-----------------------------\n"
strike2 += "-------------00--00-----------------------------\n"
strike2 += "-----------0000--0000---------------------------\n"
strike2 += "-----------0000--0000---------------------------"

mike  = "----wwwwwwwwwwwwwrrwwwwrrwrrrrrrwrrwwrrwrrrrrrw-\n"
mike += "----wwwwwwwwwwwwwrrrwwrrrwwwrrwwwrrwrrwwrrwwwww-\n"
mike += "----wwwwwwwwwwwwwrrwrrwrrwwwrrwwwrrrrwwwrrrrwww-\n"
mike += "----wwwwwwwwwwwwwrrwwwwrrwwwrrwwwrrwrrwwrrwwwww-\n"
mike += "----wwwwwwwwwwwwwrrwwwwrrwrrrrrrwrrwwrrwrrrrrrw-\n"

boards  = "----.rrrrr...rrrr...rrrr..rrrrr..rrrrr...rrrrr.-\n"
boards += "----.rr..rr.rr..rr.rr..rr.rr..rr.rr..rr.rr.....-\n"
boards += "----.rrrrr..rr..rr.rrrrrr.rrrrrr.rr..rr..rrrr..-\n"
boards += "----.rr..rr.rr..rr.rr..rr.rr.rr..rr..rr.....rr.-\n"
boards += "----.rrrrr...rrrr..rr..rr.rr..rr.rrrrr..rrrrr..-\n"
boards = boards.replace(".","w")

r = randint(0,99)

if r==0:
    strike[49*1:49*6] = mike
elif r==1:
    strike[49*1:49*6] = boards    

strikers = [strike,strike2,"\n".join([i[::-1] for i in strike.split("\n")][::-1])]
for i in range(1,30):
    strikers.append("\n".join(["--"*i+j for j in strike.split("\n")]))
    strikers.append("\n".join(["--"*i+j for j in strike2.split("\n")]))
for i in range(1,15):
    strikers.append("\n".join([j[2*i:] for j in strike.split("\n")]))
    strikers.append("\n".join([j[2*i:] for j in strike2.split("\n")]))

class StrikePage(Page):
    def __init__(self):
        super(StrikePage, self).__init__("???")
        self.name = "STRIKE"
        self.background_loaded = True

    def generate_content(self):
        s = choice(strikers)
        s = choice("rgbcmy").join(s.split("0"))
        self.print_image(s)
