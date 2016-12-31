import curses
import config

class CuPT:
    # CuPT: Curses Printing Tool
    def __init__(self, scr):
        self.WIDTH = config.WIDTH
        self.HEIGHT = config.HEIGHT-3
        self.ls = []
        self.scr = scr

    def clear_content(self):
        self.ls = []

    def show_page_number(self, n):
        txt = n + " "+config.NAME+" " + config.now().strftime("%a %d %b %H:%M")
        pad = curses.newpad(1, len(txt)+1)
        pad.addstr(0,0,txt,csty())
        pad.refresh(0,0, 0,self.WIDTH-len(txt)-1, 0,self.WIDTH)

    def show_tagline(self, tagline):
        pad = curses.newpad(1, self.WIDTH)
        pre = " " * ((self.WIDTH-len(tagline))/2)
        post = " " * (self.WIDTH-len(tagline)-len(pre)-1)
        pad.addstr(0,0,pre+tagline+post,csty("YELLOW","BLUE"))
        pad.refresh(0,0, self.HEIGHT+1,0, self.HEIGHT+1,self.WIDTH)

    def add_block(self, block, *args, **kwargs):
        bg = None
        if "bg" in kwargs:
            bg = kwargs["bg"]
        self.ls.append(Block(block, *args, bg=bg))

    def move_cursor(self, x=None, y=None):
        self.ls.append(Move(x,y))

    def add_newline(self):
        self.ls.append(Command("NEWLINE"))

    def add_text(self, text, wrapping=False):
        for line in text.split("\n")[:-1]:
            self.ls.append(CuPTPart(text, wrapping))
            self.add_newline()
        self.ls.append(CuPTPart(text.split("\n")[-1], wrapping))

    def start_fg_color(self, color):
        self.ls.append(FGColor(color))

    def end_fg_color(self):
        self.ls.append(FGColor())

    def start_bg_color(self, color):
        self.ls.append(BGColor(color))

    def end_bg_color(self):
        self.ls.append(BGColor())

    def make_curses_list(self):
        self.cls = {}
        y, x = 0, 0
        fg, bg = -1, -1
        for bit in self.ls:
            if isinstance(bit, Command):
                if bit.c == "NEWLINE":
                    y += 1
                    x = 0
            elif isinstance(bit, FGColor):
                fg = bit.color
            elif isinstance(bit, BGColor):
                bg = bit.color
            elif isinstance(bit, Move):
                if bit.x is not None:
                    x = bit.x
                if bit.y is not None:
                    y = bit.y
            elif isinstance(bit, Block):
                y,x = bit.as_curses(y,x,self)
            else:
                for cha in bit.text:
                    self.add_char(y,x,cha,csty(fg,bg))
                    x += 1
                    if bit.wrapping and x >= self.WIDTH:
                        y += 1
                        x = 0

    def add_char(self, y, x, cha, sty=None):
        if sty is None:
            sty = csty()
        if y not in self.cls:
            self.cls[y] = {}
        self.cls[y][x] = (cha, sty)

    def pad(self):
        return curses.newpad(self.HEIGHT, self.WIDTH)

    def show(self):
        from time import sleep
        self.make_curses_list()
        pad = self.pad()
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                if x!=self.WIDTH-1 or y!=self.HEIGHT-1:
                    if y in self.cls and x in self.cls[y]:
                        pad.addstr(y,x,self.cls[y][x][0],self.cls[y][x][1])
        pad.refresh(0,0,1,0,self.HEIGHT+1,self.WIDTH)

class Command:
    def __init__(self, c):
        self.c = c

class Move:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

class CuPTPart:
    def __init__(self, text, wrapping):
        self.text = text
        self.wrapping = wrapping

curses_colors = {
        "RED":(curses.COLOR_RED,0),
        "GREEN":(curses.COLOR_GREEN,0),
        "BLUE":(curses.COLOR_BLUE,0),
        "YELLOW":(curses.COLOR_YELLOW,1),
        "ORANGE":(curses.COLOR_YELLOW,0),
        "MAGENTA":(curses.COLOR_MAGENTA,0)
    }


class FGColor:
    def __init__(self, color=None):
        self.color = color

class BGColor:
    def __init__(self, color=None):
        self.color = color

class Block:
    def __init__(self, block, *args, **kwargs):
        bg = None
        if "bg" in kwargs:
            bg = kwargs["bg"]
        self.block = block
        self.cols = args
        self.bg = bg

    def as_curses(self, y, x, cupt):
        if x!=0:
            x,y = 0,y+1

        for line in self.block.split("\n"):
            if line!="":
                for j in line:
                    if j ==" ":
                        if self.bg is None:
                            cupt.add_char(y,x," ")
                        else:
                            cupt.add_char(y,x," ",csty(bg=self.bg))
                    else:
                        cupt.add_char(y,x," ",csty(bg=self.cols[int(j)]))
                    x+=1
                if self.bg is not None:
                    while x<config.WIDTH:
                        cupt.add_char(y,x," ",csty(bg=self.bg))
                        x += 1
                y += 1
                x = 0
        return y,x

class ColorManager:
    _instance=None

    def __init__(self):
        self.cols = [(-1,-1)]

    def get_col(self, fg, bg):
        for i,c in enumerate(self.cols):
            if c[0] == fg and c[1] == bg:
                return curses.color_pair(i)
        curses.init_pair(len(self.cols), fg, bg)
        self.cols.append((fg,bg))
        return curses.color_pair(len(self.cols)-1)

def clm():
    if ColorManager._instance is None:
        ColorManager._instance = ColorManager()
    return ColorManager._instance

def csty(fg=None,bg=None):
    try:
        fgc = curses_colors[fg]
    except KeyError:
        fgc = (-1,0)
    try:
        bgc = curses_colors[bg]
    except KeyError:
        bgc = (-1,0)

    c = clm().get_col(fgc[0],bgc[0])
    if bgc[1] == 1:
        c |= curses.A_BLINK
    if fgc[1] == 1:
        c |= curses.A_BOLD
    return c

        

