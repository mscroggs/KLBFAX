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

def now():
    return _dt.now()

title =("yyyyyyyyyyyyyyyyyyyyy       yyyyyyyyyy      yyyyyyyyyy                          \n"
        "yyyyyyyyyyyyyyyyyyyyy       yyyyyyyyyy      yyyyyyyyyy                          \n"
        "yyyyyyyyyyyyyy      y          y     y         y     y                          \n"
        "yyyyyyyyyyyyyy  yyyyy yyyyyyyy y  yyyy yyyyyyy y  yy y yyyyyyyyyyyyyyyyyyyyyyyyy\n"
        "yyyyyyyyyyyyyy    yyy yyyyyyyy y    yy yyyyyyy y     y yyyyyyyyyyyyyyyyyyyyyyyyy\n"
        "yyyyyyyyyyyyyy  yyyyy y   y  y y  yyyy y     y y  yy y y  y  yyyyyyyyyyyyyyyyyyy\n"
        "yyyyyyyyyyyyyy      y y      y y  yyyy y  yyyy y  yy y y  y  yyyyyyyyyyyyyyyyyyy\n"
        "yyyyyyyyyyyyyyyyyyyyy y  y y y yyyyyyy y    yy yyyyyyy yy   yyyyyyyyyyyyyyyyyyyy\n"
        "yyyyyyyyyyyyyyyyyyyyy y  yyy y yyyyyyy y  yyyy yyyyyyy y  y  yyyyyyyyyyyyyyyyyyy\n"
        "                      y  yyy y         y  yyyy         y  y  yyyyyyyyyyyyyyyyyyy\n"
        "                   yyyyyyyyyyy      yyyyyyyyyy      yyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
        "                   yyyyyyyyyyy      yyyyyyyyyy      yyyyyyyyyyyyyyyyyyyyyyyyyyyy")

title = "b".join(title.split(" "))

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

