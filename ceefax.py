# width:79
# height: 30

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
    module = getattr(__import__("pages", fromlist=[page_file_no_ext]),
                     page_file_no_ext)
    reload(module)
    for filename in dir(module):
        obj = getattr(module, filename)
        if isinstance(obj, Page):
            try:
                pageFactory.add(obj)
            except:
                pass


def restart_computer():
    from os import system
    print("Restarting")
    system("python /home/pi/player/off.py;sudo shutdown -r now")


def stop_execution():
    ThreadSignaller.queue.put(ThreadSignaller.CleanExit)
    sys.exit()


def sleep(secs):
    sleeping_time_ms = 100
    num_of_cycles = int(round(secs * 1000 / sleeping_time_ms))

    for i in range(num_of_cycles):
        try:
            signal = ThreadSignaller.queue.get_nowait()
            if signal == ThreadSignaller.CleanExit:
                sys.exit()
            elif signal == ThreadSignaller.InterruptWait:
                return
        except Queue.Empty:
            pass

        time.sleep(sleeping_time_ms / 1000.0)


def pull_new_version():
            from os import system
            print("Pulling newest version.")
            try:
                system("cd /home/pi/ceefax;git pull")
            except:
                pass


class LoopManager(object):
    def __init__(self):
        pass

    def standard(self):
        pageFactory.show_random()
        REFRESH_RATE_SECS = 30
        
        sleep(REFRESH_RATE_SECS)

    def current(self):
        self.standard()

loop_manager = LoopManager()


def name_page_handler(input):
    if len(input) <= 3:
        while len(input) < 3:
            input = "0" + input
        pageFactory.get_reloaded_page(input).show()
    elif input == "....":
        stop_execution()
    elif input == "00488a0488":
        restart_computer()
    elif input == "0026360488":
        pull_new_version()
    else:
        barcode = input
        namefile_path = "/home/pi/cards/" + barcode
        extra = ""
        if isfile(namefile_path):
            (name, house) = points.get_name_house(namefile_path)
            
            if not house:
                extra = """Error finding your house. Please
                            report to Scroggs."""

            time = now.now().strftime("%H")

            name_file = points.read_name_file(namefile_path)
            if points.should_add_morning_points(time, house, name_file,
                                                barcode):
                points_added = points.add_morning_points(time, house, barcode)
                extra = str(points_added) + " points to " + house + "!"

            name_page = page.NamePage(name, extra=extra)
        else:
            name_page = page.NamePage(input, large=False)
        name_page.show()
