#!/usr/bin/python3
"""load,add and save """


import json
def load_from_json_file(filename):
    """a function that creates an Object from a JSON file"""
    with open(filename, 'r', encoding="utf-8") as filename:
        return json.loads(filename.read())
    
def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file using a JSON"""
    with open(filename, 'w', encoding="utf-8") as filename:
        filename.write(json.dumps(my_obj))
