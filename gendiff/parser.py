import json

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def parser(file):
    if file.endswith('.json'):
        with open(file) as f:
            return parse_json(f)
    elif file.endswith('.yaml') or file.endswith('.yml'):
        with open(file) as f:
            return parse_yaml(f)


def parse_json(file):
    return json.load(file)


def parse_yaml(file):
    return load(file, Loader=Loader)
