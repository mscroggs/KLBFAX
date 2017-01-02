from __future__ import division

import config
def make_transition(f):
    to_do = {}
    for x in range(config.WIDTH):
        for y in range(config.HEIGHT-3):
            n = f(y,x)
            if n not in to_do:
                to_do[n] = []
            to_do[n].append((y,x))
    return to_do

def random():
    from random import choice
    return make_transition(choice([
            f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,
            f11,f12
        ]))

def f1(y,x):
    return x+y

def f2(y,x):
    return x-y

def f3(y,x):
    return y-x

def f4(y,x):
    return -x-y

def f5(y,x):
    return x

def f6(y,x):
    return y

def f7(y,x):
    return 0

def f8(y,x):
    return max(abs(y-10),abs(x-20))

def f9(y,x):
    return max(x,y)

def f10(y,x):
    from random import randrange
    return randrange(20)

def f11(y,x):
    return abs(x-20)

def f12(y,x):
    return abs(20-x)
