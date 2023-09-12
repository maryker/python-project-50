def make_diff(f1, f2):
    result = {}
    keys = set(f1).union(set(f2))
    for key in sorted(keys):
        result[key] = check(f1, f2, key)
    return result


def check(val1, val2, key):
    res_check = {}
    if isinstance(val1.get(key), dict) and isinstance(val2.get(key), dict):
        res_check['type'] = 'deep'
        res_check['value'] = make_diff(val1[key], val2[key])
        return res_check
    if key in val1:
        if key in val2:
            if val1[key] == val2[key]:
                res_check['type'] = 'same'
                res_check['value'] = val1[key]
            else:
                res_check['type'] = 'changed'
                res_check['value'] = [val1[key], val2[key]]
        else:
            res_check['type'] = 'deleted'
            res_check['value'] = val1[key]
    else:
        res_check['type'] = 'added'
        res_check['value'] = val2[key]
    return res_check


import json
print(make_diff(json.load(open('tests/fixtures/file1.json')), json.load(open('tests/fixtures/file2.json'))))

