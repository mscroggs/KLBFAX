#!/usr/bin/env python
import sys
sys.path.insert(0,'..')


from page import greetings

for i,g in enumerate(greetings):
    try:
        with open("dummy","w") as f:
            f.write(g)
    except:
        print g+" (number "+str(i)+") fails"
