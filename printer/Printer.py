import fonts.size7.default

class Printer(object):
    def __init__(self):
        pass

    def set_font(self, font):
        self.font = font

    def text_to_ascii(self, text):
        return font.get_letter("A")

instance = Printer()
instance.set_font(fonts.size7.default)
