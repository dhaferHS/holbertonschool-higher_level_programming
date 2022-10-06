#!/usr/bin/python3
"""
load add and save
"""


import json
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__(
    '6-load_from_json_file.py').load_from_json_file


filename = "add_item.json"

try:
    adding = load_from_json_file(filename)
    
except FileNotFoundError:
    adding = []

save_to_json_file(adding + argv[1:], filename)
