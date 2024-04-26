import itertools


def correct_value(value):
    if value is 'False':
        return 'false'
    elif value is 'True':
        return 'true'
    elif value is 'None':
        return 'null'
    else:
        pass


def stylish(data, replacer=' ', spaces_count=4):
    def iter_(current_value, depth):
        if not isinstance(current_value, (dict, list)):
            return str(current_value)

        lines = []
        indent = replacer * (depth * spaces_count + 2)
        indent2 = replacer * (depth * spaces_count + 4)
        closed_indent = replacer * (depth * spaces_count)

        if isinstance(current_value, dict):
            for k, v in current_value.items():
                lines.append(f'{indent2}{k}: {iter_(v, depth+1)}')

        for node in current_value:
            if 'status' in node and node['status'] == 'added':
                value = correct_value(node['value'])
                new_key = '+ ' + node['key']
                lines.append(f'{indent}{new_key}: {iter_(value, depth+1)}')
            elif 'status' in node and node['status'] == 'removed':
                value = correct_value(node['value'])
                new_key = '- ' + node['key']
                lines.append(f'{indent}{new_key}: {iter_(value, depth+1)}')
            elif 'status' in node and node['status'] == 'same':
                value = correct_value(node['value'])
                new_key = '  ' + node['key']
                lines.append(f'{indent}{new_key}: {iter_(value, depth+1)}')
            elif 'status' in node and node['status'] == 'nested':
                value = node['value']
                new_key = '  ' + node['key']
                lines.append(f'{indent}{new_key}: {iter_(value, depth+1)}')
            elif 'status' in node and node['status'] == 'changed':
                value1 = correct_value(node['value1'])
                value2 = correct_value(node['value2'])
                new_key1 = '- ' + node['key']
                new_key2 = '+ ' + node['key']
                lines.append(f'{indent}{new_key1}: {iter_(value1, depth+1)}')
                lines.append(f'{indent}{new_key2}: {iter_(value2, depth+1)}')
            else:
                pass

        result = itertools.chain("{", lines, [closed_indent + "}"])
        return '\n'.join(result)
    return iter_(data, 0)
