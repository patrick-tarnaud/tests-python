def majuscule(str):
    return str.upper()


def minuscule(str):
    return str.lower()


def capitalize(str):
    return str.capitalize()


def add_mult(i1, i2):
    return i1 + i2, i1 * i2


def replace(str1, o='A', t='X'):
    res = str1.replace(o.lower(), t.lower())
    res = res.replace(o.upper(), t.upper())
    return res


def zero(i):
    i = 0
    return i
