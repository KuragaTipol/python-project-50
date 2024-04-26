def get_diff(dict1, dict2):
    sorted_keys = sorted(set(dict1.keys()).union(set(dict2.keys())))
    diff = []
    for key in sorted_keys:
        if key not in dict1:
            node = {
                'status': 'added',
                'key': key,
                'value': dict2[key]
            }
        elif key not in dict2:
            node = {
                'status': 'removed',
                'key': key,
                'value': dict1[key]
            }
        elif dict1[key] == dict2[key]:
            node = {
                'status': 'same',
                'key': key,
                'value': dict1[key]
            }
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            nested_child = get_diff(dict1[key], dict2[key])
            node = {
                'status': 'nested',
                'key': key,
                'value': nested_child
            }
        elif dict1[key] != dict2[key]:
            node = {
                'status': 'changed',
                'key': key,
                'value1': dict1[key],
                'value2': dict2[key]
            }
        else:
            raise ValueError('Something wrong! Check the files contents.')

        diff.append(node)
    return diff
