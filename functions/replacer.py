import re

def escape(string):
    if string=="?":
        return "\?"
    return string

def replace(txt):
    swaps = [
            ["Donald Trump","Donald Duck"],
            ["Trump","Duck"],
            ["Brexit","Eurovision"],
            ["Lord","Darth"],
            ["Lords","Siths"],
            ["House of Commons","Jedi Council"]
        ]
    for swap in swaps:
        txt = re.sub(r"(^|[^A-Za-z])"+swap[0]+r"($|[^A-Za-z])(?i)",r"\1"+swap[1]+r"\2",txt)
    return txt
