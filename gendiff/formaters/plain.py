def form_plain(diff, start=''):
    result = []

    def inner(d, path):
        for key, val in d.items():
            new_path = f'{path}.{key}' if path != '' else key
            result.append(make_diff(val, new_path))
        return '\n'.join(filter(lambda x: x, result))

    return inner(diff, start)


def make_diff(item, val):
    if item['type'] == 'changed':
        return f"Property '{val}' was updated. "\
            f"From {to_str(item['value'][0])} to {to_str(item['value'][1])}"
    elif item['type'] == 'added':
        return f"Property '{val}' was added with value: {to_str(item['value'])}"
    elif item['type'] == 'deleted':
        return f"Property '{val}' was removed"
    elif item['type'] == 'deep':
        return form_plain(item['value'], val)
    elif item['type'] == 'same':
        pass
    else:
        raise ValueError('Incorrect type')


def to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, int):
        return value
    else:
        return f"'{value}'"
