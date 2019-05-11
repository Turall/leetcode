import re


def validnumber(s):
    pattern = r"^[+-]?(([0-9]+\.?[0-9]*)|([0-9]*\.?[0-9]+))([e][+-]?[0-9]+)?$"
    s = s.strip()
    return bool(re.match(pattern, s))


s = " -90e3   "
print(validnumber(s))

