# width:79
# height: 30
import config
import points
import os
from page import PageManager
from cupt import Screen

def is_page_file(f):
    if not os.path.isfile(os.path.join(config.pages_dir, f)):
        return False
    if "_" in f:
        return False
    if "pyc" in f:
        return False
    return True


def get_ceefax(test=None):
    if Ceefax._instance is None:
        Ceefax._instance = Ceefax(test)
    return Ceefax._instance

class Ceefax:
    _instance = None
    def __init__(self, test=None):
        self.start_time = config.now()
        if config.NAME == "KLBFAX":
            points.add_one_random(printing=True)
        if not os.path.isdir(config.config_dir):
            os.mkdir(config.config_dir)
        self.test = test

    def begin(self):
        with Screen() as scr:
            self.page_manager = PageManager(scr)
            self.start_loop()

    def start_loop(self):
        self.page_manager.start_loop(self.test)

    def kill(self):
        raise KeyboardInterrupt

