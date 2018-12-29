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

flight_api = "http://example.com/{}{}{}"

from datetime import datetime as _dt

def now():
    return _dt.now()

title =("-------yyyyyyyyyyyyyyyyy---------yyyyyyyyyy--------yyyyyyyyyy---------\n"
        "-------yyyyyyyyyyyyyyyyy---------yyyyyyyyyy--------yyyyyyyyyy---------\n"
        "-------yy......y......yy-----------y..yy.yy----------y.....yy---------\n"
        "-------yyyyyyy.y..yyy.yy-yyyyyyyyy-y..yy.yy-yyyyyyyy-y..yy.yy-yyyyyyyy\n"
        "-------yy......y......yy-yyyyyyyyy-y.....yy-yyyyyyyy-y.....yy-yyyyyyyy\n"
        "-------yy..yyyyy..yyy.yy-yyyyy..yy-y..yy.yy-y.....yy-y..yy.yy-y..y..yy\n"
        "-------yy......y......yy-yyyyy..yy-y..yy.yy-y..yyyyy-y..yy.yy-y..y..yy\n"
        "-------yyyyyyyyyyyyyyyyy-yyyyy..yy-yyyyyyyy-y....yyy-yyyyyyyy-yy...yyy\n"
        "-------yyyyyyyyyyyyyyyyy-y..yy..yy-yyyyyyyy-y..yyyyy-yyyyyyyy-y..y..yy\n"
        "-------------------------y......yy----------y..yyyyy----------y..y..yy\n"
        "-----------------------yyyyyyyyyyy--------yyyyyyyyyy--------yyyyyyyyyy\n"
        "-----------------------yyyyyyyyyyy--------yyyyyyyyyy--------yyyyyyyyyy").replace(".","b")


twitter_access_key = None
twitter_access_secret = None
twitter_consumer_key = None
twitter_consumer_secret = None

metoffer_api_key = None
open_weather_api_key = None

location = [51.5252257441084, -0.134831964969635]

try:
    from localconfig import *
except ImportError:
    pass
