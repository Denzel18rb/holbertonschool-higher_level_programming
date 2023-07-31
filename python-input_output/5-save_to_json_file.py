#!/usr/bin/python3
"""
Save Object to a file
"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file"""
    with open(filename, mode='w', encoding="utf-8") as f:
        json_str = json.dumps(my_obj)
        f.write(json_str)
