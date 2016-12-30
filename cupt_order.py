def random_order():
    from random import choice
    return choice([
                   (f1,0,0)
                  ])

import screen

def f1(y,x):
    if y%2 == 0:
        if x < screen.WIDTH-1:
            return (y,x+1)
        if y == screen.HEIGHT-1:
            return None,None
        return (y+1,x)
    if x>0:
        return (y,x-1)
    if y == screen.HEIGHT-1:
        return None,None
    return (y+1,x)

