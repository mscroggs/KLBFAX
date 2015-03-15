import fonts.size7.default
import fonts.exceptions
from fonts.LetterBlock import LetterBlock


def process_printing_options(function):
    def wrapper(self, text, **options):
        padding_options = options.get("padding", {})
        padding_enabled = padding_options != {}
        left_shift = padding_options.get("left", 0)
        filler = padding_options.get("filler", "|")
        if padding_enabled:
            text = filler * left_shift + text

        result = function(self, text)

        if padding_enabled:
            right_shift = 80 - result.get_length()
            if right_shift > 0:
                result += function(self, filler * right_shift)

        return result

    return wrapper


class Printer(object):
    def __init__(self):
        pass

    def set_font(self, font):
        self.font = font

    @process_printing_options
    def text_to_letterblock(self, text):
        try:
            return reduce(LetterBlock.__add__, map(self.font.get_letter, text))
        except fonts.exceptions.LetterNotDefined:
            return text

    def text_to_ascii(self, text, **options):
        return str(self.text_to_letterblock(text, **options))


instance = Printer()
instance.set_font(fonts.size7.default)
