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
    non_boring = [RED,GREEN,YELLOW,MAGENTA,CYAN]
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
    non_strike = [DEFAULT,BOLD,FAINT,STANDOUT]
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

def block_characters(text,invert=False):
    if invert==False:
        text = text.replace("x",u"\u2588")
        text = text.replace(",",u"\u2584")
        text = text.replace("'",u"\u2580")
    else:
        text = text.replace(" ",u"\u2588")
        text = text.replace("'",u"\u2584")
        text = text.replace(",",u"\u2580")	
        text = text.replace("x"," ")
    return text
    
def colour_print(text,background=Background.BLUE,foreground=Foreground.YELLOW+Style.BOLD,invert=False,rainbow=False):
    text = background+foreground+text
    if rainbow:
        from random import choice
        print text[0],text[1]
        newtext = Background.BLACK
        for character in text.strip("\033[44m").strip("\033[33m"):
            newtext += choice(Style.non_strike)
            newtext += choice(Foreground.non_boring)
            newtext += character
        text = newtext
    text = block_characters(text,invert)        
    #text = (u"\u2588").join(text.split("x"))
    text += Foreground.DEFAULT+Background.DEFAULT+Style.DEFAULT
    return(text)

def colour_print_join(list,joiner="",pre=""):
    length = 0
    for item in list:
        length = max(length,len(item[0].split("\n")))
    lines = [pre]*length

    for item in list:
        splitted = item[0].split("\n")
        length2 = 0
        for thing in splitted:
            length2 = max(length2,len(thing))
        for i in range(length):
            lines[i] += item[1]+item[2]
            if i<len(splitted):
                lines[i] += block_characters(splitted[i],False) + " "*(length2 - len(splitted[i]))
            else:
                lines[i] += " "*length2
            lines[i] += Foreground.DEFAULT+Background.DEFAULT+joiner
    return "\n".join(lines)
