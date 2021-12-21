from django import template

register = template.Library()


def lower(value):  # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()


def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')


register.filter('cut', cut)
register.filter('lower2', lower)
