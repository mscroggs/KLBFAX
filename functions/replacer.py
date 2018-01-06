import re

def escape(string):
    if string=="?":
        return "\?"
    return string

def replace(imput):
    swaps = [
            ["Donald Trump","Jonty"],
            ["Trump","Jonty"],
            ["Brexit","Eurovision"],
            ["Lord","Darth"],
            ["Lords","Siths"]
        ]
    for swap in swaps:
        imput = re.sub(r"(^|[^A-Za-z])"+swap[0]+r"($|[^A-Za-z])(?i)",r"\1"+swap[1]+r"\2",imput)
    return imput

