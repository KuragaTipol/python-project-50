def get_diff(dict1, dict2):
    sorted_keys = sorted(set(dict1.keys()).union(set(dict2.keys())))
    diff = []
    for key in sorted_keys:
        if key not in dict1:
            child = {
                'status': 'added',
                'key': key,
                'value': sorted_keys[key]
            }
        elif key not in dict2:
            child = {
                'status': 'removed',
                'key': key,
                'value': sorted_keys[key]
            }
        elif dict1[key] == dict2[key]:
            child = {
                'status': 'same',
                'key': key,
                'value': sorted_keys[key]
            }
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            nested_child = {get_diff_tree(dict1[key], dict2[key])}
            child = {
                'status': 'nested',
                'key': key,
                'value': nested_child
            }
        elif dict1[key] != dict2[key]:
            child = {
                'status': 'changed',
                'key': key,
                'value1': dict1[key],
                'value2': dict2[key]
            }
        else:
            raise ValueError('Something wrong! Check the files contents.')

        diff.append(child)
    return diff
