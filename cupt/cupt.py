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

    def show_loading(self):
        from os import system
        system("""echo "\033[13]"""")
        pad = curses.newpad(1, self.WIDTH)
        pad.addstr(0,0,"Loading next page...")
        pad.refresh(0,0, self.HEIGHT+2,0, self.HEIGHT+2,self.WIDTH)

    def show_tagline(self, tagline):
        pad = curses.newpad(2, self.WIDTH)
        pre = " " * ((self.WIDTH-len(tagline))/2)
        post = " " * (self.WIDTH-len(tagline)-len(pre))
        pad.addstr(0,0,pre+tagline+post,csty("YELLOW","BLUE"))
        pad.refresh(0,0, self.HEIGHT+1,0, self.HEIGHT+2,self.WIDTH)

    def add_block(self, block, *args, **kwargs):
        bg = None
        if "bg" in kwargs:
            bg = kwargs["bg"]
        self.ls.append(Block(block, *args, bg=bg))

    def add_blocked_block(self, block, fg=None, bg=None, rainbow=False, pre=0):
        if rainbow:
            self.ls.append(BlockedBlock(block, rainbow=True, pre=pre))
        else:
            self.ls.append(BlockedBlock(block, fg=fg, bg=bg, pre=pre))

    def move_cursor(self, x=None, y=None):
        self.ls.append(Move(x,y))

    def add_newline(self):
        self.ls.append(Command("NEWLINE"))

    def add_text(self, text, wrapping=False, pre=0):
        for line in text.split("\n")[:-1]:
            self.ls.append(CuPTPart(line, wrapping, pre=pre))
            self.add_newline()
        self.ls.append(CuPTPart(text.split("\n")[-1], wrapping, pre=pre))

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
            elif isinstance(bit, BlockedBlock):
                y,x = bit.as_curses(y,x,self)
            else:
                for cha in bit.text:
                    self.add_char(y,x,cha,csty(fg,bg))
                    x += 1
                    if bit.wrapping and x >= self.WIDTH:
                        y += 1
                        x = bit.pre
                                    

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
        from .transitions import random
        self.make_curses_list()
        tran = random()
        pad = curses.newpad(1,2)
        for n in sorted(tran.keys()):
            for y,x in tran[n]:
                #if y!=self.HEIGHT-1 or x!=self.WIDTH-1:
                    if y in self.cls and x in self.cls[y]:
                        try:
                            pad.addstr(0,0,self.cls[y][x][0],self.cls[y][x][1])
                        except:
                            try:
                                pad.addstr(0,0,self.cls[y][x][0].encode("utf-8"),self.cls[y][x][1])
                            except:
                                pad.addstr(0,0," ")
                    else:
                        pad.addstr(0,0," ")
                    pad.refresh(0,0,y+1,x,y+1,x)
            sleep(.01)

class Command:
    def __init__(self, c):
        self.c = c

class Move:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

class CuPTPart:
    def __init__(self, text, wrapping, pre):
        self.text = text
        self.wrapping = wrapping
        self.pre = pre

curses_colors = {
        "RED":(curses.COLOR_RED,0),
        "LIGHTRED":(curses.COLOR_RED,1),
        "GREEN":(curses.COLOR_GREEN,0),
        "LIGHTGREEN":(curses.COLOR_GREEN,1),
        "BLUE":(curses.COLOR_BLUE,0),
        "LIGHTBLUE":(curses.COLOR_BLUE,1),
        "YELLOW":(curses.COLOR_YELLOW,1),
        "CYAN":(curses.COLOR_CYAN,0),
        "LIGHTCYAN":(curses.COLOR_CYAN,1),
        "ORANGE":(curses.COLOR_YELLOW,0),
        "MAGENTA":(curses.COLOR_MAGENTA,0),
        "PINK":(curses.COLOR_MAGENTA,1),
        "GREY":(curses.COLOR_BLACK,1),
        "DEFAULT":(-1,0),
        "WHITE":(curses.COLOR_WHITE,0),
        "BRIGHTWHITE":(curses.COLOR_WHITE,1),
        "BLACK":(curses.COLOR_BLACK,0)
    }
non_dark_colors = [
        "RED",
        "LIGHTRED",
        "GREEN",
        "LIGHTGREEN",
        "BLUE",
        "LIGHTBLUE",
        "YELLOW",
        "CYAN",
        "LIGHTCYAN",
        "ORANGE",
        "MAGENTA",
        "PINK",
        "WHITE",
        "BRIGHTWHITE"]

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
                        try:
                            cupt.add_char(y,x," ",csty(bg=self.cols[int(j)]))
                        except:
                            cupt.add_char(y,x,j)
                    x+=1
                if self.bg is not None:
                    while x<config.WIDTH:
                        cupt.add_char(y,x," ",csty(bg=self.bg))
                        x += 1
                y += 1
                x = 0
        return y,x

cmap = {
        "x":u"\u2588",
        "'":u"\u2580",
        ",":u"\u2584"
       }

class BlockedBlock:
    def __init__(self, block, fg=None, bg=None, rainbow=False, pre=0):
        self.block = block
        self.bg = bg
        self.fg = fg
        self.rainbow=rainbow
        self.pre = pre

    def as_curses(self, y, x, cupt):
        from random import choice
            
        my_csty = csty(fg=self.fg, bg=self.bg)

        if x>self.pre:
            x,y = self.pre,y+1
        if x<self.pre:
            x = self.pre

        for line in self.block.split("\n"):
            if line!="":
                for j in line:
                    if self.rainbow:
                        my_csty = csty(fg=choice(non_dark_colors))
                    for inc,outc in cmap.items():
                        if j==inc:
                            cupt.add_char(y,x,outc.encode("utf-8"),my_csty)
                            break
                    else:
                        cupt.add_char(y,x," ",my_csty)
                    x += 1
                y += 1
                x = self.pre
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

        

