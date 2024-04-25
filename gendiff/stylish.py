import itertools


# def stylish(value, replacer=' ', spaces_count=2):
#     def iter_(current_value, depth=1):
#         deep_indent = replacer * depth * spaces_count
#         closed_indent = replacer * (depth-1) * spaces_count
#         lines = []
#
#         if isinstance(current_value, dict):
#             for key, val in current_value.items():
#                 lines.append(f'{deep_indent}{key}: {iter_(val, depth + 1)}')
#                 result = itertools.chain("{", lines, [closed_indent + "}"])
#         else:
#             return str(current_value)
#         return '\n'.join(result)
#     return iter_(value)

def correct_value(value):

    return result


def stylish(data, replacer=' ', spaces_count=4):
    def iter_(current_value, depth):
        if not isinstance(current_value, (dict, list)):
            return str(current_value)
        lines = []
        indent = '  '

        if isinstance(current_value, dict):
            for k, v in current_value:
                lines.append(f'  ...  ')

        for node in current_value:
            if node['status'] == 'added':
                new_key = ' +' + node['key']
                lines.append(f'{indent}{new_key}: {iter_(node['value'], depth)}')
            elif node['status'] == 'removed':
                new_key = ' -' + node['key']
                lines.append('f  ...  ')
            elif node['status'] == 'same':
                new_key =
                lines.append('f  ...  ')
            elif node['status'] == 'nested':
                new_key =
                lines.append('f  ...  ')
            elif node['status'] == 'changed':
                new_key =
                new_key =
                lines.append('f  ...  ')
                lines.append('f  ...  ')

        result = itertools.chain("{", lines, [closed_indent + "}"])
        return '\n'.join(result)
    return iter_(data)
