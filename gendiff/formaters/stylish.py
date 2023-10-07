FORMS = {'deleted': '-', 'added': '+', 'same': ' '}


def form_stylish(value, replace=' ', repeat=4):
    return check_for_dict(value, 1, replace, repeat)


def make_dict(item, depth, replace, repeat):
    result = []
    result.append('{\n')
    for key, val in item.items():
        if isinstance(val, dict):
            if 'type' in val:
                result.append(make_diff(val, key, depth, replace, repeat))
            else:
                result.append(f'{replace*(depth*repeat)}{key}: '
                              + make_dict(val, depth + 1, replace, repeat)
                              + '\n')
        else:
            result.append(f'{replace*(depth*repeat)}{key}: {to_str(val)}\n')
    result.append(f'{replace*repeat*(depth-1)}' + '}')
    return ''.join(result)


def make_diff(value, key, depth, replace, repeat):
    result = []
    if value['type'] == 'deep':
        result.append(f'{replace*((depth*repeat)-2)}  {key}: '
                      + make_dict(value['value'], depth + 1, replace, repeat)
                      + '\n')
    elif value['type'] in FORMS:
        result.append(f"{replace*((depth*repeat)-2)}"
                      + f"{FORMS[value['type']]} {key}: "
                      + check_for_dict(value['value'], depth + 1,
                                       replace, repeat) + "\n")
    elif value['type'] == 'changed':
        result.append(f"{replace*((depth*repeat)-2)}- {key}: "
                      + check_for_dict(value['value'][0], depth + 1,
                                       replace, repeat) + "\n")
        result.append(f"{replace*((depth*repeat)-2)}+ {key}: "
                      + check_for_dict(value['value'][1], depth + 1,
                                       replace, repeat) + "\n")
    else:
        raise ValueError('Incorrect type')
    return ''.join(result)


def check_for_dict(item, depth, replace, repeat):
    if isinstance(item, dict):
        return make_dict(item, depth, replace, repeat)
    else:
        return to_str(item)


def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)
