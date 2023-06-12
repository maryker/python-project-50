import json

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def parser(file):
    if file.endswith('.json'):
        return pars_json(file)
    elif file.endswith('.yaml') or file.endswith('.yml'):
        return pars_yaml(file)


def pars_json(file):
    return json.load(open(file))


def pars_yaml(file):
    return load(open(file), Loader=Loader)
