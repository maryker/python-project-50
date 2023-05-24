def form_plain(dictt, start=''):
    result = []

    def inner(d, path):
        for key in d:
            if isinstance(d[key], dict):
                new_path = f'{path}.{key}' if path != '' else key
                if any(k in ['-', '+', ' '] for k in dictt[key]):
                    result.append(make_diff(dictt[key], new_path))
                else:
                    result.append(form_plain(dictt[key], new_path))
        return '\n'.join(filter(lambda x: x, result))

    return inner(dictt, start)


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
    if value == 'true' or value == 'false' or value == 'null':
        return value
    else:
        return f"'{value}'"
