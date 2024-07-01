# your_app/templatetags/templatetag.py

from django import template
from datetime import datetime, date

register = template.Library()

@register.simple_tag
def current_datetime(format_string):
    """
    Returns the current date and time formatted according to the given format string.
    """
    return datetime.now().strftime(format_string)

@register.filter(name='truncate_chars')
def truncate_chars(value, max_length):
    """
    Truncates the string to the specified number of characters.
    """
    if len(value) > max_length:
        return value[:max_length] + '...'
    return value

@register.filter(name='to_uppercase')
def to_uppercase(value):
    """
    Converts a string to uppercase.
    """
    return value.upper()

@register.simple_tag
def calculate_age(birth_date):
    """
    Calculates age based on the given birth date.
    """
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

