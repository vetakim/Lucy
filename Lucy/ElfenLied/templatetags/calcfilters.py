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

@register.filter(name='pieces')
def pieces(list_, key):
    '''getting sum of list_'s elements with same key'''
    c = Counter()
    for j in list_:
        c[j[key]] += 1
    return c.most_common()

@register.filter(name='categorized')
def categorized(list_, key):
    '''getting sublist of list_ with same key'''
    c = pieces(list_, key)
    return [(i, [k for k in list_ if k[key] == i]) for i, j in c]




