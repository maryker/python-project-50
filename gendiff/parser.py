import json
import os

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def parse(file):
    extention = os.path.splitext(file)[1]
    with open(file, 'r') as f:
        return read_file(f, extention)


def read_file(file, extention):
    if extention == '.json':
        return json.load(file)
    elif extention == '.yaml' or extention == '.yml':
        return load(file, Loader=Loader)
