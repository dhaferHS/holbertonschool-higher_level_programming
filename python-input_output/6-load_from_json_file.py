#!/usr/bin/python3
"""load an object"""


import json


def load_from_json_file(filename):
    """a function that creates an Object from a JSON file"""
    with open(filename, "w", encoding="utf-8"):
        filename.write(jason.loads)
