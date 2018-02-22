from page import Page
import config
from random import choice
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
strike2 += "---------------0000------g----------------------\n"
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

strikers = [strike,strike2]

class StrikePage(Page):
    def __init__(self):
        super(StrikePage, self).__init__("???")
        self.name = "STRIKE"
        self.background_loaded = True

    def generate_content(self):
        s = choice(strikers)
        s = choice("rgbcmy").join(s.split("0"))
        self.print_image(s)
