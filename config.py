import os as _os

def test_dir(directory):
    if not _os.path.isdir(directory):
        try:
            _os.mkdir(directory)
        except:
            pass

default_path = _os.path.join(_os.path.expanduser("~"), ".fax/")
ceefax_path = _os.path.dirname(_os.path.realpath(__file__))

test_dir(default_path)

WIDTH = 80
HEIGHT = 30

pages_dir = _os.path.join(ceefax_path, "pages")
with open(_os.path.join(ceefax_path, "VERSION")) as f:
    VERSION = f.read()

sleeping_time_ms = 100
default_page_duration_sec = int(_os.getenv('default_page_duration_sec', 30))

NAME = "EMFFAX"

from datetime import datetime as _dt
import pytz as _pytz

timezone = _pytz.timezone('Europe/London')

def now():
    return _pytz.utc.localize(_dt.now()).astimezone(timezone)

title = """
0000000000000000000             000000000       000000000
000000000000      0               0     0         0     0
000000000000  00000 0000000000000 0  0000 0000000 0  0  0 0000000000000000000000
000000000000    000 0    000    0 0    00 0     0 0     0 0  0  0000000000000000
000000000000  00000 0  0  0  0  0 0  0000 0  0000 0  0  0 0  0  0000000000000000
000000000000      0 0  00   00  0 0  0000 0    00 0  0  0 00   00000000000000000
0000000000000000000 0  0000000  0 0000000 0  0000 0000000 0  0  0000000000000000
                    0  0000000  0         0  0000         0  0  0000000000000000
                  000000000000000       000000000       000000000000000000000000"""

twitter_access_key = None
twitter_access_secret = None
twitter_consumer_key = None
twitter_consumer_secret = None


try:
    from localconfig import *
except ImportError:
    pass

