class Foreground:
    DEFAULT = "\033[0m"
    BLACK   = "\033[30m"
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    BLUE    = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN    = "\033[36m"
    WHITE   = "\033[97m"
    LGRAY   = "\033[37m"
    DGRAY   = "\033[90m"
    LRED    = "\033[91m"
    LGREEN  = "\033[92m"
    LYELLOW = "\033[93m"
    LBLUE   = "\033[94m"
    LMAGENTA= "\033[95m"
    LCYAN   = "\033[96m"
    list = [DEFAULT,BLACK,RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN,WHITE]
    delist = ["DEFAULT","BLACK","RED","GREEN","YELLOW","BLUE","MAGENTA","CYAN","WHITE"]

class Style:
    DEFAULT  = "\033[0m"
    BOLD     = "\033[1m"
    FAINT    = "\033[2m"
    STANDOUT = "\033[3m"
    UNDERLINE= "\033[4m"
    BLINK    = "\033[5m"
    STRIKE    = "\033[9m"
    list = [DEFAULT,BOLD,FAINT,STANDOUT,UNDERLINE,BLINK,STRIKE]
    delist = ["DEFAULT","BOLD","FAINT","STANDOUT","UNDERLINE","BLINK","STRIKE"]

class Background:
    DEFAULT = "\033[0m"
    BLACK   = "\033[40m"
    RED     = "\033[41m"
    GREEN   = "\033[42m"
    YELLOW  = "\033[43m"
    BLUE    = "\033[44m"
    MAGENTA = "\033[45m"
    CYAN    = "\033[46m"
    LGRAY   = "\033[47m"
    DGRAY   = "\033[100m"
    LRED    = "\033[101m"
    LGREEN  = "\033[102m"
    LYELLOW = "\033[103m"
    LBLUE   = "\033[104m"
    LMAGENTA= "\033[105m"
    LCYAN   = "\033[106m"
    WHITE   = "\033[107m"
    list = [DEFAULT,BLACK,RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN,WHITE]
    non_boring = [RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN]
    delist = ["DEFAULT","BLACK","RED","GREEN","YELLOW","BLUE","MAGENTA","CYAN","WHITE"]

def colour_print(text,background=Background.BLUE,foreground=Foreground.YELLOW):
    text = background+foreground+text
    text = (u"\u2588").join(text.split("x"))
    text += Foreground.DEFAULT+Background.DEFAULT
    return(text)
