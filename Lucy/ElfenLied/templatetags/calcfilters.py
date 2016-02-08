from django import template

register = template.Library()

@register.filter(name='mul')
def mul(value, arg):
    '''multiplying'''
    return value.__mul__(arg)

