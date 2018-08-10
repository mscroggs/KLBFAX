from page import Page
from ceefax import Ceefax
import config

class IndexPage(Page):
    def __init__(self, n):
        super(IndexPage, self).__init__(n)
        self.importance = 5
        self.title = "Index"
        self.in_index = False

    def generate_content(self):
        self.print_image(config.title)
        self.start_fg_color("GREEN")
        self.add_text("INDEX "*14)
        self.add_newline()
        i = 0
        _items = Ceefax().page_manager.sorted_pages()
        for num, page in _items:
            if page.enabled and page.in_index:
                self.start_fg_color("MAGENTA")
                if page.index_num is None:
                    self.add_text(num)
                else:
                    self.add_text(page.index_num)
                self.end_fg_color()
                self.add_text(" "+page.title)
                if i == 0:
                    self.move_cursor(x=36)
                    i = 1
                else:
                    self.add_newline()
                    i = 0

i_p = IndexPage("100")
