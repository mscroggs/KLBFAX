from datetime import datetime
import traceback
from config import current_dir
class List(object):
    def __init__(self):
        self.ls = []

    def add(self, e, number):
        self.ls.append(Error(e,number))
        self.ls = self.ls[-10:]

    def __iter__(self):
        return iter(self.ls[::-1])

class Error(object):
    def __init__(self, e, number):
        self.e = e
        self.number = number
        self.datetime = datetime.now()
        self.traceback = traceback.format_exc()

    def _error_as_string(self):
        if isinstance(self.e, str):
            return self.e
        return self.e.__class__.__name__

    def as_string(self):
        out = "At " + self.datetime.strftime("%Y-%m-%d %H:%M")
        out += ", page " + self.number + " had a"
        e = self._error_as_string()
        if e.lower()[0] in ["a","e","i","o","u"]:
            out += "n"
        return out + " " + e


    def short_traceback(self):
        last = 0
        tsp = self.traceback.split("\n")
        for i,line in enumerate(tsp):
            if "/pages/" in line:
                last = i
        out = tsp[last:last+2]
        last = 0
        for i,line in enumerate(tsp):
            if current_dir in line:
                last = i
        out += tsp[last:last+2]
        return "\n".join(out)


list = List()
