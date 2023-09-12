FORMS = {'deleted': '-', 'added': '+', 'same': ' '}

def form_stylish(value, replace=' ', repeat=2):
    return to_str(value, 1, replace, repeat)


def make_dict(item, depth, replace, repeat):
    result = []
    result.append('{\n')
    for key, val in item.items():
        if isinstance(val, dict):
            if 'type' in val:
                if val['type'] == 'deep':
                    result.append(f"{replace*(depth*repeat)}  {key}: {make_dict(val['value'], depth+1, replace, repeat)}\n")
                else:
                    result.append(make_diff(val, key, depth+1, replace, repeat))
            else:
                result.append(f'{replace*(depth*repeat-2)}{key}: {make_dict(val, depth+1, replace, repeat)}\n')
        else:
            result.append(f'{replace*((depth+1)*repeat)}{key}: {val_to_str(val)}\n')
    result.append(f'{replace*(repeat*depth-2)}' + '}')
    return ''.join(result)


def make_diff(value, key, depth, replace, repeat):
    result = []
    if value['type'] in FORMS:
        result.append(f"{replace*(depth*repeat)}{FORMS[value['type']]} {key}: {to_str(value['value'], depth+1, replace, repeat)}" + "\n")
    else:
        result.append(f"{replace*(depth*repeat)}- {key}: {to_str(value['value'][0], depth+1, replace, repeat)}" + "\n")
        result.append(f"{replace*(depth*repeat)}+ {key}: {to_str(value['value'][1], depth+1, replace, repeat)}" + "\n")
    return ''.join(result)


def to_str(item, depth, replace, repeat):
    result = []
    if isinstance(item, dict):
        return make_dict(item, depth, replace, repeat)
    else:
        result.append(val_to_str(item))
    return ''.join(result)


def val_to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)
