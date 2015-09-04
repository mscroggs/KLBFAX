# width:79
# height: 30

import sys
from os import listdir
from os.path import isfile
import os
from page import PageFactory, Page
import Keyboard
import time
import thread_communication


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
    for object in dir(module):
        obj = getattr(module, object)
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
    Keyboard.is_thread_active = False
    sys.exit()


def sleep(secs):
    for i in range(secs):
        if not Keyboard.is_thread_active:
            sys.exit()

        if thread_communication.should_interrupt:
            return

        time.sleep(1)


def pull_new_version():
            from os import system
            print("Pulling newest version.")
            try:
                system("cd /home/pi/ceefax;git pull")
            except:
                pass

