import os
import inspect


def get_bd_filepath():
    if os.getenv('DEVELOP') or os.getenv('SLAVE'):
        return os.path.join(current_dir, dummy_data_folder, 'birthdays.json')
    else:
        return os.path.join(os.path.expanduser('~'), '.klb/birthdays.json')


current_dir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))

dummy_data_folder = "dummy_data"
birthday_file = get_bd_filepath()

sleeping_time_ms = 100
default_page_duration_sec = int(os.getenv('default_page_duration_sec', 30))

weather_file_location = '/home/pi/ceefax/uk_weather_data'
