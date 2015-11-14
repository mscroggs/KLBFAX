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
