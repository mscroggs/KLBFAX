# width:79
# height: 30

import config
import sys
from os import listdir
from os.path import isfile
import os
from page import PageFactory, Page
import time
import points
import now
import page
import ThreadSignaller
import Queue
from random import choice

class ConfigError(Exception):
    pass


def is_page_file(f):
    if "_" in f:
        return False
    if "pyc" in f:
        return False
    return True


pages_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "pages")
if not os.path.exists(pages_dir):
    try:
        os.makedirs(pages_dir)
    except OSError:
        raise ConfigError("The pages folder doesn't exist" +
                          "and cannot be created: " + pages_dir)

only_page_files = [f for f in listdir(pages_dir)
                   if isfile(os.path.join(pages_dir, f)) and is_page_file(f)]

pageFactory = PageFactory()

for page_file in only_page_files:
    page_file_no_ext = os.path.splitext(page_file)[0]
    try:
        module = getattr(__import__("pages", fromlist=[page_file_no_ext]),
                         page_file_no_ext)
        reload(module)
        for filename in dir(module):
            obj = getattr(module, filename)
            if isinstance(obj, Page):
                pageFactory.add(obj)
    except:
        pass


def restart_computer():
    from os import system
    print("Restarting")
    system("python /home/pi/player/off.py;sudo shutdown -r now")


def stop_execution():
    ThreadSignaller.queue.put(ThreadSignaller.CleanExit)


def get_greeting_page(barcode):
    namefile_path = "/home/pi/cards/" + barcode
    extra = ""
    from page import greetings
    if isfile(namefile_path):
        (name, house, twitter) = points.get_name_house(namefile_path)

        if not house:
            extra = """Error finding your house. Please
                        report to Scroggs."""

        if twitter is None:
            deets = ""
        else:
            deets = greetings.random() + " @"+twitter+"! "

        time = now.now().strftime("%H")

        name_file = points.read_name_file(namefile_path)
        if points.should_add_morning_points(time, house, name_file,
                                            barcode):
            points_added = points.add_morning_points(time, house, barcode, deets)
            extra = str(points_added) + " points to " + house + "!"

        name_page = page.NamePage(name, extra=extra)
    else:
        name_page = page.NamePage(barcode, large=False)
    return name_page


def pull_new_version():
    from os import system
    print("Pulling newest version.")
    try:
        system("cd /home/pi/ceefax;git pull")
        with open("/home/pi/ceefax/temp","w") as f:
            f.write("YES")
        stop_execution()
    except:
        pass


class LoopManager(object):
    def __init__(self):
        pass

    def _get_cycles_left(self, duration_sec):
        return int(round(duration_sec * 1000.0 / config.sleeping_time_ms))

    def standard(self):
        i = 0
        num_cycles_left = 0
        the_page = None

        while True:
            if i >= num_cycles_left:
                if now.now().strftime("%H") == "12" and now.now().minute < 20:
                    the_page = page.LunchPage()
                if now.now().strftime("%a%H") == "Fri17" and now.now().minute < 20:
                    the_page = page.PubPage()
                else:
                    the_page = pageFactory.get_loaded_random()
            try:
                signal = ThreadSignaller.queue.get_nowait()
                if isinstance(signal, ThreadSignaller.ShowPage):
                    the_page = pageFactory.get_reloaded_page(signal.page_num)
                elif isinstance(signal, ThreadSignaller.ShowGreetingPage):
                    the_page = get_greeting_page(signal.barcode)
                elif signal == ThreadSignaller.CleanExit:
                    self.weather_thread.stop()
                    sys.exit()
                elif signal == ThreadSignaller.InterruptStandardLoop:
                    break
            except Queue.Empty:
                pass

            if the_page:
                num_cycles_left = self._get_cycles_left(the_page.duration_sec)
                i = 0
                the_page.show()
                the_page = None
            if not the_page:
                i += 1
                time.sleep(config.sleeping_time_ms / 1000.0)

    def current(self):
        self.standard()

    def set_weather_thread(self, weather_thread):
        self.weather_thread = weather_thread

loop_manager = LoopManager()


def name_page_handler(input):
    # make sure the Keyboard thread is never blocked by loading pages
    if len(input) <= 3:
        while len(input) < 3:
            input = "0" + input
        ThreadSignaller.queue.put(ThreadSignaller.ShowPage(input))
    elif input == "....":
        stop_execution()
    elif input == "00488a0488":
        restart_computer()
    elif input == "0026360488":
        pull_new_version()
    else:
        ThreadSignaller.queue.put(ThreadSignaller.ShowGreetingPage(input))
