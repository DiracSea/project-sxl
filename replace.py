import sys

class SafeSub(dict):
    """防止key找不到"""
    def __missing__(self, key):
        return '{' + key + '}'

def sub(text):
    return text.format_map(SafeSub(sys._getframe(1).f_locals))