import json
import yaml
import os
from gendiff.stylish import stylish
from gendiff.generate_diff import get_diff


def open_file(filepath):
    if '.json' in filepath:
        file = json.load(open(os.path.join('Tests/Fixtures', filepath)))
    elif '.yml' or '.yaml' in filepath:
        file = yaml.safe_load(open(os.path.join('Tests/Fixtures', filepath)))
    else:
        raise ValueError('Format is wrong! Needs json or yaml.')
    return file


def generate_diff(filepath1, filepath2):
    data1 = open_file(filepath1)
    data2 = open_file(filepath2)
    diff = get_diff(data1, data2)
    result = stylish(diff)
    return result
