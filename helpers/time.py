from datetime import datetime as _dt
import pytz as _pytz
import config

def datetime(*args, **kwargs):
    #return _pytz.utc.localize(_dt(*args, **kwargs)).astimezone(config.timezone)
    return _dt(*args, **kwargs)
