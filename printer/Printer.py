import fonts.size7.default
import fonts.exceptions
import screen
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
            right_shift = screen.WIDTH - len(result)
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
        text_to_print = str(self.text_to_letterblock(text, **options))
        output = []
        hit_sides = False
        for line in text_to_print.split("\n"):
            if len(line) > screen.WIDTH:
                output.append(line[:screen.WIDTH])
                hit_sides = True
            else:
                output.append(line+"x"*(screen.WIDTH-len(line)))
        if hit_sides: output.append("") 
        return "\n".join(output)

instance = Printer()
instance.set_font(fonts.size7.default)
