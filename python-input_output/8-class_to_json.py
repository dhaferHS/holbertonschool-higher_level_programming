#!/usr/bin/python3
"""return dictionary"""


def class_to_json(obj):
    """a function that returns the dictionary description with simple data structure for JSON serialization"""
    return obj.__dic__
