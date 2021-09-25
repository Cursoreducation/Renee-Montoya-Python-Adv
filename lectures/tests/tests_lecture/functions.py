from check_sum import *


def check_dif(x, y):
    return x - y


def division(x, y):
    return x // y


def check_after_sum(x, y):
    s = check_sum(x, y)
    return (x + y) * s


def return_dict():
    return {"a": 1, "b": 2}