import json


def generate_diff(file1, file2):
    f1 = json.load(open(file1))
    f2 = json.load(open(file2))
    result = {}
    keys = set(f1).union(set(f2))
    for key in sorted(keys):
        if key in f1:
            if f1.get(key, None) == f2.get(key, None):
                result[f'   {key}'] = f1[key]
            else:
                result[f' - {key}'] = f1[key]
                if key in f2:
                    result[f' + {key}'] = f2[key]
        else:
            result[f' + {key}'] = f2[key]
    # with open('tests/fixtures/file1_types.json', 'w') as file:
    #     json.dump(result, file, indent=2)
    return '{\n' + \
        '\n'.join([f'{key}: {value_to_str(value)}'
                  for key, value in result.items()]) + '\n}'


def value_to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return value
