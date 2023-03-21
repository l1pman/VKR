from django import template
register = template.Library()

@register.filter
def to_rl(string):
    return string.split('n')