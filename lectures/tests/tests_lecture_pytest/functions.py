from time import sleep


def check_sum(x, y):
    return x + y


def check_dif(x, y):
    return x - y


def division(x, y):
    return x // y


def check_after_sum(x, y):
    s = check_sum(x, y)
    return (x + y) * s


def r_list():
    return [1, 2, 3, 5]


def is_windows():
    # This sleep could be some complex operation instead
    sleep(5)
    return True


def get_operating_system():
    return "Windows" if is_windows() else "Linux"
