import os
from os.path import join,expanduser
from page import Page
from file_handler import f_readlines

class EventPage(Page):
    def __init__(self):
        super(EventPage, self).__init__("150")
        self.title = "Events"

    def generate_content(self):
        self.add_title("EVENTS")
        events={}
        cur=""
        lines = f_readlines('events')
        for line in lines:
            line = line.decode("utf-8")
            line = line.strip("\n")
            if line != "":
                if line[0] == "#":
                    line = line.strip("#").strip(" ")
                    cur = line
                    events[cur] = []
                elif cur in events:
                    events[cur].append(line)

        for date in sorted(events):
            event = events[date]
            self.add_text(date)
            self.add_newline()
            i = 0
            col = "WHITE"
            for info in event:
                self.add_text("  ")
                self.start_fg_color(col)
                self.add_text(info)
                self.end_fg_color()
                self.add_newline()
                if col == "WHITE":
                    if i >= 2:
                        col = "YELLOW"
                    i += 1
                elif col == "YELLOW":
                    col = "GREEN"
                elif col == "GREEN":
                    col = "YELLOW"
            self.add_newline()

events_page = EventPage()
