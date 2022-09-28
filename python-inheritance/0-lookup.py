#!/usr/bin/python3
""" function that list of availble aatributes and methods of an object"""


def lookup(obj):
    '''Lookup object attributes and methods.
    Args:
        obj to list.
    Return:
        list of attributes.
    '''
    return dir(obj)
