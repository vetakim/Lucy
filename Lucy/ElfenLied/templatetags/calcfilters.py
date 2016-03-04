from django import template
from collections import Counter

register = template.Library()

@register.filter(name='mul')
def mul(value, arg):
    '''multiplying'''
    return value.__mul__(arg)

@register.filter(name='get')
def get(value, arg):
    '''getting value from dict'''
    return value.__getitem__(arg)

@register.filter(name='categorized')
def categorized(list_, key):
    c = Counter()
    for j in list_:
        c[j[key]] += 1
    return list(zip(c.keys(), c.values()))
