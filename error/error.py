from datetime import datetime
import traceback

class List(object):
    def __init__(self):
        self.ls = []

    def add(self, e, number):
        self.ls.append(Error(e,number))

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
        out += " " + e
        return out



list = List()
