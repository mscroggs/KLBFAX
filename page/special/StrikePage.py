from page import Page
import config

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
strike += "-------------------------g------bbbbbb----------\n"
strike += "-------------------------g------bbbbbb----------\n"
strike += "-------------------------g----bbbbbbbbbb--------\n"
strike += "-------------------------g----bbbbbbbbbb--------\n"
strike += "-------------------------g----bbbbbbbbbb--------\n"
strike += "-------------------------g----bbbbbbbbbb--------\n"
strike += "-------------------------g----bbbbbbbbbb--------\n"
strike += "-------------------------g----bbbbbbbbbb--------\n"
strike += "-------------------------g------bbbbbb----------\n"
strike += "-------------------------g------bbbbbb----------\n"
strike += "-------------------------g--------bb------------\n"
strike += "-------------------------g--------bb------------\n"
strike += "-------------------------bbbbbbbbbbbbb----------\n"
strike += "-------------------------bbbbbbbbbbbbb----------\n"
strike += "----------------------------------bb--bb--------\n"
strike += "----------------------------------bb--bb--------\n"
strike += "----------------------------------bb--bb--------\n"
strike += "----------------------------------bb--bb--------\n"
strike += "----------------------------------bb--bb--------\n"
strike += "----------------------------------bb--bb--------\n"
strike += "----------------------------------bb------------\n"
strike += "----------------------------------bb------------\n"
strike += "----------------------------------bb------------\n"
strike += "----------------------------------bb------------\n"
strike += "--------------------------------bbbbbb----------\n"
strike += "--------------------------------bbbbbb----------\n"
strike += "--------------------------------bb--bb----------\n"
strike += "--------------------------------bb--bb----------\n"
strike += "--------------------------------bb--bb----------\n"
strike += "--------------------------------bb--bb----------\n"
strike += "--------------------------------bb--bb----------\n"
strike += "--------------------------------bb--bb----------\n"
strike += "------------------------------bbbb--bbbb--------\n"
strike += "------------------------------bbbb--bbbb--------"


class StrikePage(Page):
    def __init__(self):
        super(StrikePage, self).__init__("???")
        self.name = "STRIKE"
        self.background_loaded = True

    def generate_content(self):
        self.print_image(strike)
