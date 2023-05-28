def form_plain(diff, start=''):
    result = []

    def inner(d, path):
        for key in d:
            if isinstance(d[key], dict):
                new_path = f'{path}.{key}' if path != '' else key
                if any(k in ['-', '+', ' '] for k in diff[key]):
                    result.append(make_diff(diff[key], new_path))
                else:
                    result.append(form_plain(diff[key], new_path))
        return '\n'.join(filter(lambda x: x, result))

    return inner(diff, start)


def make_diff(item, val):
    result = []
    if '-' in item and '+' in item:
        return f"Property '{val}' was updated. "\
            f"From {to_str(item['-'])} to {to_str(item['+'])}"
    for key in item:
        if key == '+':
            result.append(f"Property '{val}' was added with value: "
                          f"{to_str(item[key])}")
        if key == '-':
            result.append(f"Property '{val}' was removed")
    return ''.join(result)


def to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return f"'{value}'"
