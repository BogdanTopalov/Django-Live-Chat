from django import template

register = template.Library()


@register.filter
def index(value, i):
    """ Get key value """
    return value[f"{i}"]
