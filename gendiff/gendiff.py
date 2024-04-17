import itertools
import json


# def listing(diff):
#     diff_list = []
#     for key, value in diff.items():
#         if value is False:
#             diff_list.append(f'  {key}: false')
#         elif value is True:
#             diff_list.append(f'  {key}: true')
#         else:
#             diff_list.append(f'  {key}: {value}')
#     return diff_list


def generate_diff(filepath1, filepath2):
    data1 = json.load(open(filepath1))
    data2 = json.load(open(filepath2))

    sorted_list = sorted(set(data1.keys()).union(set(data2.keys())))
    diff = {}
    for key in sorted_list:
        if key not in data1:
            diff[f'+ {key}'] = data2[key]
        elif key not in data2:
            diff[f'- {key}'] = data1[key]
        elif data1[key] == data2[key]:
            diff[f'  {key}'] = data1[key]
        elif data1[key] != data2[key]:
            diff[f'- {key}'] = data1[key]
            diff[f'+ {key}'] = data2[key]

    diff_list = []
    for key, value in diff.items():
        if value is False:
            diff_list.append(f'  {key}: false')
        elif value is True:
            diff_list.append(f'  {key}: true')
        else:
            diff_list.append(f'  {key}: {value}')

    # diff_list = listing(diff)
    result = itertools.chain('{', diff_list, '}')
    return '\n'.join(result)
