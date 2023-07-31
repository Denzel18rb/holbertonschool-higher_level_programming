#!/usr/bin/python3
"""
Load, add, save
"""


import json
import os
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
if os.path.exists(filename):
    json_obj = load_from_json_file(filename)
else:
    json_obj = []
json_obj.extend(sys.argv[1:])
save_to_json_file(json_obj, filename)
