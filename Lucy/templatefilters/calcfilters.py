from django import template

register = template.Library()

def mul(value, arg):
    '''multiplying'''
    return value * arg
