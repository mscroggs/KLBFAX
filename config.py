import os
import inspect

WIDTH = 80
HEIGHT = 30

config_dir = os.path.join(os.path.expanduser('~'), '.klb')

pages_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "pages")
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "VERSION")) as f:
    VERSION = f.read()

debug = False
if os.getenv('DEBUG'):
    debug = True

def has_gmail_login():
    return os.path.isfile(os.path.join(os.path.expanduser("~"), ".klb/gmail"))


def get_bd_filepath():
    if os.getenv('DEVELOP') or os.getenv('SLAVE'):
        return os.path.join(current_dir, dummy_data_folder, 'birthdays.json')
    else:
        return os.path.join(config_dir, 'birthdays.json')


current_dir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))

dummy_data_folder = "dummy_data"
birthday_file = get_bd_filepath()

sleeping_time_ms = 100
default_page_duration_sec = int(os.getenv('default_page_duration_sec', 30))

weather_f_name = 'uk_weather_data'



if os.getenv("SLAVE"):
    NAME = "28JHFAX"
elif os.getenv("EMF"):
    NAME = "EMFFAX"
elif os.getenv("POST"):
    NAME = "602FAX"
elif os.getenv("WWW"):
    NAME = "WWWFAX"
else:
    NAME = "KLBFAX"

MAIN = False
if os.path.isdir("/home/pi/.klbtemp"):
    MAIN = True

from datetime import datetime

if NAME == "28JHFAX":
    def is_oxmas():
        return (datetime.now().month==12 and datetime.now().day in [14,15,16,17,18,19,20,21,22])
    def is_oxmas_day():
        return (is_oxmas() and datetime.now().weekday()==5)
else:
    def is_oxmas():
        return False
    def is_oxmas_day():
        return False

import pytz

timezone = pytz.timezone('Europe/London')

def now():
    return pytz.utc.localize(datetime.now()).astimezone(timezone)

