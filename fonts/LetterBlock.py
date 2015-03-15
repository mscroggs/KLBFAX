class LetterBlock:
    def __init__(self, _str):
        self._str = _str

    def __add__(self, other):
        return LetterBlock(merge_blog_strings(self._str, other._str))

    def __str__(self):
        return self._str


def merge_blog_strings(str1, str2):
    return "\n".join([l1 + l2 for l1, l2 in zip(str1.split("\n"), str2.split("\n"))])
