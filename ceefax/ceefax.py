# width:79
# height: 30
import config
import points
import os
from page import PageManager
import curses

def is_page_file(f):
    if not os.path.isfile(os.path.join(config.pages_dir, f)):
        return False
    if "_" in f:
        return False
    if "pyc" in f:
        return False
    return True


def get_ceefax():
    if Ceefax._instance is None:
        Ceefax._instance = Ceefax()
    return Ceefax._instance
    

class Ceefax:
    _instance = None
    def __init__(self):
        if config.NAME == "KLBFAX":
            points.add_one_random(printing=True)
        if not os.path.isdir(config.config_dir):
            mkdir(config.config_dir)

    def begin(self):
        self.scr = curses.initscr()
        self.page_manager = PageManager(self.scr)

        curses.start_color()
        curses.use_default_colors()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.scr.keypad(1)
        curses.resizeterm(config.HEIGHT,config.WIDTH)
        self.scr.refresh()
        self.start_loop()

    def end(self):
        curses.nocbreak()
        curses.curs_set(1)
        self.scr.keypad(0)
        curses.echo()
        curses.endwin()

    def start_loop(self):
        from time import sleep
        try:
            self.page_manager.start_loop()
        except Exception as e:
            import sys
            import traceback
            exc_type, exc_obj, tb = sys.exc_info()
            print traceback.print_tb(tb)
            print(type(e))
            print(e)
            sleep(5)
        self.end()

def restart_computer():
    from os import system
    print("Restarting")
    system("sudo shutdown -r now")


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

        if twitter is not None:
            deets = greetings.random_twitter() + " @"+twitter+"!"
        elif name is not None:
            deets = greetings.random_twitter() + " " + name
        else:
            deets = ""

        time = now.now().strftime("%H")

        name_file = points.read_name_file(namefile_path)
        if points.should_add_morning_points(time, house, name_file,
                                            barcode):
            points_added = points.add_morning_points(time, house, barcode, deets)
            extra = str(points_added) + " points to " + house + "!"
            if points_added < 0:
                extra += "\n" + "It's the weekend, go home!"

        name_page = page.NamePage(name, extra=extra)
    else:
        name_page = page.NamePage(barcode, large=False)
    return name_page


def pull_new_version():
    from os import system
    from name import NAME
    print("Pulling newest version.")
    try:
        system("cd /home/pi/ceefax;git pull")
        if NAME == "KLBFAX":
            with open("/home/pi/ceefax/temp","w") as f:
                f.write("YES")
        elif NAME == "28JHFAX":
            system("KLBur")
        try:
            with open("/home/pi/ceefax/requirements-satisfied.txt") as f:
                satis = [s.strip("\n") for s in f.readlines()]
        except:
            satis = []
        with open("/home/pi/ceefax/requirements.txt") as f:
            for line in f.readlines():
                line = line.strip("\n")
                if line not in satis:
                    print("installing "+line)
                    with open("/home/pi/ceefax/requirements-satisfied.txt","a+") as g:
                        g.write(line+"\n")
                    system("sudo pip install "+line)
                    print("installed "+line)
        stop_execution()
    except:
        pass
