import fonts.size7.default
import fonts.size7condensed.default
import fonts.size7extracondensed.default
import fonts.size4.default
import fonts.size4bold.default
import fonts.size4mono.default
import fonts.exceptions
import config
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
            right_shift = config.WIDTH - len(result)
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
            from functools import reduce
        except:
            pass
        try:
            return reduce(LetterBlock.__add__, map(self.font.get_letter, text))
        except fonts.exceptions.LetterNotDefined:
            return text

    def text_to_ascii(self, text, fill=True, vertical_condense=False, **options):
        try:
            text_to_print = str(self.text_to_letterblock("|"+text, **options))
        except:
            text_to_print = text
        output = []
        hit_sides = False
        for line in text_to_print.split("\n"):
            if len(line) > config.WIDTH:
                output.append(line[:config.WIDTH])
                hit_sides = True
            elif fill:
                output.append(line+"x"*(config.WIDTH-len(line)))
            else:
                output.append(line)
        if vertical_condense:
            output = self.v_condense(output)

        if hit_sides and self.squashed is not None:
            return self.squashed.text_to_ascii(text,fill,vertical_condense=vertical_condense,**options)

        return "\n".join(output)

    def v_condense(self, text):
        output = []
        for i in range(0,len(text),2):
            line = ""
            if i+1==len(text):
                text.append("x"*len(text[i]))
            for a,b in zip(text[i],text[i+1]):
                if a+b=="xx":
                    line += "x"
                elif a+b=="x ":
                    line += "'"
                elif a+b=="' ":
                    line += "'"
                elif a+b==", ":
                    line += "'"
                elif a+b==" x":
                    line += ","
                elif a+b==" ,":
                    line += ","
                elif a+b==" '":
                    line += ","
                elif a+b=="  ":
                    line += " "
                else:
                    line += "x"
            output.append(line)
        return output

extrathin_instance = Printer()
extrathin_instance.set_font(fonts.size7extracondensed.default)

thin_instance = Printer(extrathin_instance)
thin_instance.set_font(fonts.size7condensed.default)

instance = Printer(thin_instance)
instance.set_font(fonts.size7.default)

# If you want to add more fonts you have to also add their names into __init__.py
size4_instance = Printer()
size4_instance.set_font(fonts.size4.default)

size4bold_instance = Printer(size4_instance)
size4bold_instance.set_font(fonts.size4bold.default)

size4mono_instance = Printer()
size4mono_instance.set_font(fonts.size4mono.default)
