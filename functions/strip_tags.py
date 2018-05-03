import re
try:
    chr = unichr
except:
    pass

# This function is taken from
# http://effbot.org/zone/re-sub.htm#unescape-html
def unescape(text):
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return chr(int(text[3:-1], 16))
                else:
                    return chr(int(text[2:-1]))
            except ValueError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)


def strip_tags(txt):
    return unescape(re.sub(r"<[^>]*>","",txt))
