class CuPT:
    # CuPT: Curses Printing Tool
    def __init__(self, scr):
        import screen
        self.WIDTH = screen.WIDTH
        self.HEIGHT = screen.HEIGHT-3
        self.ls = []
        self.scr = scr

    def add_newline(self):
        self.ls.append(Command("NEWLINE"))

    def add_text(self, text, wrapping=False):
        self.ls.append(CuPTPart(text, wrapping))

    def start_fg_color(self, color):
        self.ls.append(FGColor(color))

    def end_fg_color(self):
        self.ls.append(FGColor())

    def start_bg_color(self, color):
        self.ls.append(BGColor(color))

    def end_bg_color(self):
        self.ls.append(BGColor())

    def make_curses_list(self):
        import curses
        self.cls = {}
        y, x = 0, 0
        col_n = 1
        fg, bg = -1, -1
        curses.init_pair(col_n, bg, fg)
        for bit in self.ls:
            if isinstance(bit, Command):
                if bit.c == "NEWLINE":
                    y += 1
                    x = 0
            elif isinstance(bit, FGColor):
                col_n += 1
                fg = bit.as_curses_color()
                curses.init_pair(col_n, bg, fg)
            elif isinstance(bit, BGColor):
                col_n += 1
                bg = bit.as_curses_color()
                curses.init_pair(col_n, bg, fg)
            else:
                for cha in bit.text:
                    if y not in self.cls:
                        self.cls[y] = {}
                    self.cls[y][x] = (cha, col_n)
                    x += 1
                    if bit.wrapping and x >= self.WIDTH:
                        y += 1
                        x = 0

        #print self.cls

    def pad(self):
        import curses
        return curses.newpad(self.HEIGHT, self.WIDTH)

    def show(self):
        self.make_curses_list()
        from cupt_order import random_order
        pad = self.pad()
        f,y,x = random_order()
        while y is not None:
            if y in self.cls and x in self.cls[y]:
                pad.addstr(y,x,self.cls[y][x][0],self.cls[y][x][1])
            y,x = f(y,x)
        pad.refresh(0,0, 0,0, self.HEIGHT+1, self.WIDTH)

class Command:
    def __init__(self, c):
        self.c = c

class CuPTPart:
    def __init__(self, text, wrapping):
        self.text = text
        self.wrapping = wrapping

class FGColor:
    def __init__(self, color=None):
        self.color = color

    def as_curses_color(self):
        import curses
        if color == "RED":
            return curses.COLOR_RED
        if color == "GREEN":
            return curses.COLOR_GREEN
        if color == "BLUE":
            return curses.COLOR_BLUE
        return -1

class BGColor:
    def __init__(self, color=None):
        self.color = color

    def as_curses_color(self):
        import curses
        if color == "RED":
            return curses.COLOR_RED
        if color == "GREEN":
            return curses.COLOR_GREEN
        if color == "BLUE":
            return curses.COLOR_BLUE
        return -1

