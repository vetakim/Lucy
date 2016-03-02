from django import template

register = template.Library()

@register.filter(name='mul')
def mul(value, arg):
    '''multiplying'''
    return value.__mul__(arg)

@register.filter(name='get')
def get(value, arg):
    '''getting value from dict'''
    return value.__getitem__(arg)

# def categorized(list_, key):
    
