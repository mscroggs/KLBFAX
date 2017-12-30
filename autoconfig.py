import os as _os
from file_handler import default_path,ceefax_path

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

