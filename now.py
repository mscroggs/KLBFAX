from datetime import datetime
import pytz

timezone = pytz.timezone('Europe/London') 

def now():
    return pytz.utc.localize(datetime.now()).astimezone(timezone)

