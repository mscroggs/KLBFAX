import fonts.size7.default
import fonts.exceptions
from fonts.LetterBlock import LetterBlock


class Printer(object):
    def __init__(self):
        pass

    def set_font(self, font):
        self.font = font

    def text_to_ascii(self, text):
        try:
            return str(reduce(LetterBlock.__add__, map(self.font.get_letter, text)))
        except fonts.exceptions.LetterNotDefined:
            return text

instance = Printer()
instance.set_font(fonts.size7.default)
