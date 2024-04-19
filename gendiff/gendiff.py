import itertools
import json
import yaml


def open_file(filepath):
    if '.json' in filepath:
        file = json.load(open(filepath))
    elif '.yml' or '.yaml' in filepath:
        file = yaml.safe_load(open(filepath))
    return file


def to_style(dict_):
    list_ = []
    for key, value in dict_.items():
        if value is False:
            list_.append(f'  {key}: false')
        elif value is True:
            list_.append(f'  {key}: true')
        else:
            list_.append(f'  {key}: {value}')
    result = itertools.chain('{', list_, '}')
    return '\n'.join(result)


def sorted_diff_dict(dict1, dict2):
    sorted_list = sorted(set(dict1.keys()).union(set(dict2.keys())))
    diff = {}
    for key in sorted_list:
        if key not in dict1:
            diff[f'+ {key}'] = dict2[key]
        elif key not in dict2:
            diff[f'- {key}'] = dict1[key]
        elif dict1[key] == dict2[key]:
            diff[f'  {key}'] = dict1[key]
        elif dict1[key] != dict2[key]:
            diff[f'- {key}'] = dict1[key]
            diff[f'+ {key}'] = dict2[key]
    return diff


def generate_diff(filepath1, filepath2):
    data1 = open_file(filepath1)
    data2 = open_file(filepath2)
    diff_dict = sorted_diff_dict(data1, data2)
    result = to_style(diff_dict)
    return result
