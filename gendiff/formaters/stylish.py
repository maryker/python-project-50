def form_stylish(value, replace=' ', repeat=2):
    return to_str(value, 1, replace, repeat)


def make_dict(item, depth, replace, repeat):
    result = []
    result.append('{\n')
    for key, val in item.items():
        if isinstance(val, dict):
            result.append(make_diff(val, key, depth + 1, replace, repeat)
                          + '\n')
        else:
            result.append(f'{replace*((depth + 1)*repeat)}{key}: {val}\n')
    result.append(f'{replace*repeat*(depth - 1)}' + '}')
    return ''.join(result)


def make_diff(dict, val, depth, replace, repeat):
    new_diff = []
    for key in dict:
        if key in ['-', '+', ' ']:
            new_diff.append(f'{replace*(depth*repeat - 2)}{key} {val}: '
                            + to_str(dict[key], depth + 1, replace, repeat))
    if not any(k in ['-', ' ', '+'] for k in dict):
        new_diff.append(f'{replace*(depth*repeat)}{val}: '
                        + to_str(dict, depth + 1, replace, repeat))
    return '\n'.join(new_diff)


def to_str(item, depth, replace, repeat):
    result = []
    if isinstance(item, dict):
        return make_dict(item, depth, replace, repeat)
    else:
        result.append(value_to_str(item))
    return ''.join(result)


def value_to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)
