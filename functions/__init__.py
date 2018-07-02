from .replacer import replace
from .strip_tags import strip_tags

def strip_tags_and_replace(txt):
    return replace(strip_tags(txt))
