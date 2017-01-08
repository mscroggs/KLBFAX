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
    return make_transition(choice([f25]))
    return make_transition(choice([
            f01,f02,f03,f04,f05,f06,f07,f08,f09,f10,
            f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,
            f21,f22,f23,f24,f25
        ]))

def f01(y,x):
    return x+y

def f02(y,x):
    return x-y

def f03(y,x):
    return y-x

def f04(y,x):
    return -x-y

def f05(y,x):
    return x

def f06(y,x):
    return y

def f07(y,x):
    return 0

def f08(y,x):
    return max(abs(y-10),abs(x-20))

def f09(y,x):
    return max(x,y)

def f10(y,x):
    from random import randrange
    return randrange(20)

def f11(y,x):
    return abs(x-20)

def f12(y,x):
    return abs(20-x)

def f13(y,x):
    return abs(x-40)

def f14(y,x):
    return abs(40-x)

def f15(y,x):
    return abs(x-60)

def f16(y,x):
    return abs(60-x)

def f17(y,x):
    return x%10

def f18(y,x):
    return x%20

def f19(y,x):
    return y%10

def f20(y,x):
    return y%20

def f21(y,x):
    return abs(x-y)

def f22(y,x):
    return -abs(x-y)

def f23(y,x):
    return abs(x//2-y)

def f24(y,x):
    return -abs(x//2-y)

def f25(y,x):
    return max(abs(x-80),abs(y-15))
