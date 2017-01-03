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

if os.getenv("SLAVE") and not os.getenv("EXPORT_ME"):
    NAME = "28JHFAX"
elif os.getenv("EMF"):
    NAME = "EMFFAX"
else:
    NAME = "KLBFAX"


from datetime import datetime
import pytz

timezone = pytz.timezone('Europe/London') 

def now():
    return pytz.utc.localize(datetime.now()).astimezone(timezone)

