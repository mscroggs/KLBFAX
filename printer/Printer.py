import fonts.size7.default
import fonts.size7condensed.default
import fonts.size7extracondensed.default
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
    def __init__(self, squashed=None):
        self.squashed = squashed

    def set_font(self, font):
        self.font = font

    @process_printing_options
    def text_to_letterblock(self, text):
        try:
            return reduce(LetterBlock.__add__, map(self.font.get_letter, text))
        except fonts.exceptions.LetterNotDefined:
            return text

    def text_to_ascii(self, text, fill=True, **options):
        try:
            text_to_print = str(self.text_to_letterblock("|"+text, **options))
        except:
            text_to_print = text
        output = []
        hit_sides = False
        for line in text_to_print.split("\n"):
            if len(line) > screen.WIDTH:
                output.append(line[:screen.WIDTH])
                hit_sides = True
            elif fill:
                output.append(line+"x"*(screen.WIDTH-len(line)))
            else:
                output.append(line)
        if hit_sides and self.squashed is not None:
            return self.squashed.text_to_ascii(text,fill,**options)
        
        return "\n".join(output)

 
extrathin_instance = Printer()
extrathin_instance.set_font(fonts.size7extracondensed.default)
 
thin_instance = Printer(extrathin_instance)
thin_instance.set_font(fonts.size7condensed.default)

instance = Printer(thin_instance)
instance.set_font(fonts.size7.default)