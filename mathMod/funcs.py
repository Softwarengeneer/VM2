import math


# first
def first(val):
    return math.pow(val, 2) + val + 2


def firstP1(val):
    return 2 * val + 1


# second
def second(val):
    return 3 * math.pow(val, 2) - (14 * val) - 5


def secondP1(val):
    return 6 * val - 14


# third
def third(val):
    return math.pow(val, 2) + (2 * val) + 1


def thirdP1(val):
    return 2 * val + 2


# fourth
def fourth(val):
    return math.pow(math.e, val) - 1


def fourthP1(val):
    return math.pow(math.e, val)


# for System

# first system
def fun0(x0, y0):
    return [valStr1(x0, y0), valStr2(x0, y0)]


def yakobian0(x0, y0):
    return [[1, 1], [2 * x0, 2 * y0]]


def valStr1(val, val1):
    return val + val1 - 8


def valStr2(val, val1):
    return math.pow(val, 2) + math.pow(val1, 2) - 82


def valGr(val):
    return 8 - val


def valGr1(val):
    return math.pow(82 - math.pow(val, 2), 0.5)


