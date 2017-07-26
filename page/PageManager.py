import random
import config
import os
from page import Page,special
import signal
import curses
import points

class TimeUp(BaseException):
    pass

def alarm(signum, frame):
    raise TimeUp

def pass_f(signum, frame):
    pass

def is_page_file(f):
    if not os.path.isfile(os.path.join(config.pages_dir, f)):
        return False
    if "_" in f:
        return False
    if "pyc" in f:
        return False
    return True

def get_chr(ip):
    if 48<=ip<=57 or 65<=ip<=90 or 97<=ip<=122:
        return chr(ip)
    return ""

class PageManager:
    def __init__(self, scr):
        self.i = 0
        self.loads = 0
        self.pages = {}
        self.scr = scr

        self.load_all_pages()

    def load_all_pages(self):
        if not os.path.exists(config.pages_dir):
            raise ConfigError("The pages folder doesn't exist: " + pages_dir)
        only_page_files = [f for f in os.listdir(config.pages_dir) if is_page_file(f)]
        for page_file in only_page_files:
            page_file_no_ext = os.path.splitext(page_file)[0]
            try:
                module = getattr(__import__("pages", fromlist=[page_file_no_ext]),
                                 page_file_no_ext)
                reload(module)
                for filename in dir(module):
                    obj = getattr(module, filename)
                    if isinstance(obj, Page):
                        self.add(obj)
            except:
                pass

    def add(self, page):
        self.pages[page.number] = page

    def get_loaded_random(self):
        page = FailPage()
        self.loads += 1
        while not page.loaded or not page.background_loaded:
            page = random.choice(self.get_enabled_pages(str(self.i)))
            self.i += 1
            self.i %= 10
            if page.background_loaded:
                page.loaded = False
                try:
                    page.reload()
                    page.loaded = True
                except:
                    pass
        return page

    def print_all(self):
        items = self.pages.items()
        items.sort()
        for page_num, page in items:
            p = ""
            if not page.is_enabled: p += "\033[31m"
            p += (page_num+" ")
            p += (page.title)
            if not page.is_enabled: p += "\033[0m"
            print(p)

    def export_all_to_html(self):
        # To do: Write this!
        pass

    def export_all(self):
        import os
        items = self.pages.items()
        items.sort()
        ls = ["# List of pages","The pages in brackets are disabled.",""]
        for page_num, page in items:
            p = ""
            if not page.is_enabled: p += "("
            p += (page_num+" ")
            p += (page.title)
            if not page.is_enabled: p += ")"
            ls.append(p)
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../PAGES.md"),"w") as f:
            f.write("\n".join(ls))

    def get_enabled_pages(self, starting="0"):
        if starting == "0":
            return [self.pages["100"]]
        output = [page for page in self.pages.values() if page.is_enabled and page.number[0]==starting]
        if len(output) > 0:
            return output
        else:
            return [page for page in self.pages.values() if page.is_enabled]

    def page_exists(self, page_num):
        if page_num in self.pages:
            return True

        return False

    def background_loop(self):
        from time import sleep
        while True:
            for page in self.pages.values():
                try:
                    page.background_error = None
                    page.background_loaded = False
                    page.background()
                    page.background_loaded = True
                except Exception as e:
                    page.background_error = e
            sleep(60*30)

    def start_loop(self, test=None):
        try:
            import thread
        except ImportError:
            import _thread as thread
        if test is not None:
            page = self.pages[test]
            try:
                page.background_error = None
                page.background_loaded = False
                page.background()
                page.background_loaded = True
            except Exception as e:
                page.background_error = e
        thread.start_new_thread(self.background_loop,())
        self.main_loop()

    def main_loop(self):
        from time import sleep
        import sys
        import select
        inp = "100"
        while True:
            self.clear_input()
            if inp is not None:
                page = self.handle_input(inp)
            elif config.now().strftime("%H") == "12" and config.now().minute < 20:
                page = special.LunchPage()
            elif config.now().strftime("%a%H") == "Fri17" and config.now().minute < 20:
                page = special.PubPage()
            else:
                page = self.get_loaded_random()
            self.show(page)
            signal.signal(signal.SIGALRM, alarm)
            signal.alarm(30)
            try:
                key = None
                inp = ""
                while key != curses.KEY_ENTER and key != 10:
                    key = self.scr.getch()
                    try:
                        if key==263:
                            inp = inp[:-1]
                        else:
                            inp += get_chr(key)
                        self.show_input(inp)
                    except ValueError:
                        pass
                signal.alarm(0)
                signal.signal(signal.SIGALRM, pass_f)
            except TimeUp:
                inp = None

    def handle_input(self, the_input):
        if the_input == "pub":
            return special.PubPage()
        if the_input == "lunch":
            return special.LunchPage()
        if the_input == "1337" or the_input == "0026360488" or the_input == "0082620488":
            import computer
            computer.git_pull()
        if the_input == "00488a0488":
            import computer
            computer.reboot()
        if the_input == "....":
            import computer
            computer.kill_ceefax()
        if len(the_input)>6:
            from page.special import NamePage
            namefile_path = "/home/pi/cards/" + the_input
            extra = ""
            from functions import greetings
            if os.path.isfile(namefile_path):
                _name, house, twitter = points.get_name_house(namefile_path)
            else:
                _name, house, twitter = None,None,None
            if _name is not None:
                if house is None:
                    extra = "Error finding your house. Please report to Scroggs."
                if twitter is not None:
                    deets = greetings.random_twitter() + " @"+twitter+"!"
                elif _name is not None:
                    deets = greetings.random_twitter() + " " + _name
                else:
                    deets = ""
        
                time = config.now().strftime("%H")
        
                name_file = points.read_name_file(namefile_path)
                if points.should_add_morning_points(time, house, name_file,
                                                    the_input):
                    points_added = points.add_morning_points(time, house, the_input, deets)
                    extra = str(points_added) + " points to " + house + "!"
                    if points_added < 0:
                        extra += "\nIt's the weekend, go home!"
        
                name_page = NamePage(_name, extra=extra)
            else:
                name_page = NamePage(the_input, large=False)
            return name_page



        try:
            while len(the_input)<3:
                the_input = "0"+str(the_input)
            return self.pages[the_input]
        except KeyError:
            return FailPage("Page "+the_input+" does not exist. Try the index in page 100.",False)

    def show(self, page):
        page.cupt.show_loading()
        if not isinstance(page, FailPage):
            if page.background_error is not None:
                page = FailPage("There was an error running page "+page.number+"'s background function.\n\n"+str(page.background_error))
            elif page.number != "100" and not page.background_loaded:
                page = FailPage("Page "+page.number+" currently updating. Please try again in a few minutes",False)
        try:
            page.loaded = False
            page.reload()
            page.loaded = True
            page.show()
        except Exception as e:
            page = FailPage(e)
            page.reload()
            page.loaded = True
            page.show()

    def show_input(self, i):
        pad = curses.newpad(1, config.WIDTH)
        pad.addstr(0,0,i[:config.WIDTH-1])
        pad.refresh(0,0, config.HEIGHT-1,0, config.HEIGHT-1,config.WIDTH)

    def clear_input(self):
        self.show_input(" "*config.WIDTH)

class FailPage(Page):
    def __init__(self, e=None, points=True):
        super(FailPage, self).__init__("---")
        self.ee = None
        self.set_exception(e)
        self.is_enabled = False
        self.duration_sec = 2
        self.points = points

    def generate_content(self):
        if self.points:
            from points import add_points
            add_points("Slytherin", 2)

        if self.points:
            self.add_text("Page failed to load...")
            self.add_newline()
            self.add_newline()
            self.add_text("2 points to Slytherin!")
            self.add_newline()
            self.add_newline()

        if self.ee is None:
            self.add_text("UNKNOWN ERROR")
        elif type(self.ee) == str:
            self.add_wrapped_text(self.ee)
        else:
            self.add_wrapped_text(str(self.ee))

    def set_exception(self, e):
        self.ee = e

