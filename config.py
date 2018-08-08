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

title =("yyyyyyyyyyyyyyyyyyyyy-------yyyyyyyyyy------yyyyyyyyyy--------------------------\n"
        "yyyyyyyyyyyyyyyyyyyyy-------yyyyyyyyyy------yyyyyyyyyy--------------------------\n"
        "yyyyyyyyyyyyyybbbbbby----------ybbbbby---------ybbbbby--------------------------\n"
        "yyyyyyyyyyyyyybbyyyyy-yyyyyyyy-ybbyyyy-yyyyyyy-ybbyyby-yyyyyyyyyyyyyyyyyyyyyyyyy\n"
        "yyyyyyyyyyyyyybbbbyyy-yyyyyyyy-ybbbbyy-yyyyyyy-ybbbbby-yyyyyyyyyyyyyyyyyyyyyyyyy\n"
        "yyyyyyyyyyyyyybbyyyyy-ybbbybby-ybbyyyy-ybbbbby-ybbyyby-ybbybbyyyyyyyyyyyyyyyyyyy\n"
        "yyyyyyyyyyyyyybbbbbby-ybbbbbby-ybbyyyy-ybbyyyy-ybbyyby-ybbybbyyyyyyyyyyyyyyyyyyy\n"
        "yyyyyyyyyyyyyyyyyyyyy-ybbybyby-yyyyyyy-ybbbbyy-yyyyyyy-yybbbyyyyyyyyyyyyyyyyyyyy\n"
        "yyyyyyyyyyyyyyyyyyyyy-ybbyyyby-yyyyyyy-ybbyyyy-yyyyyyy-ybbybbyyyyyyyyyyyyyyyyyyy\n"
        "----------------------ybbyyyby---------ybbyyyy---------ybbybbyyyyyyyyyyyyyyyyyyy\n"
        "-------------------yyyyyyyyyyy------yyyyyyyyyy------yyyyyyyyyyyyyyyyyyyyyyyyyyyy\n"
        "-------------------yyyyyyyyyyy------yyyyyyyyyy------yyyyyyyyyyyyyyyyyyyyyyyyyyyy")


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

