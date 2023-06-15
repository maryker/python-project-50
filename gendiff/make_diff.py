def make_diff(f1, f2):
    result = {}
    keys = set(f1).union(set(f2))
    for key in sorted(keys):
        if isinstance(f1.get(key), dict) and isinstance(f2.get(key), dict):
            result[key] = make_diff(f1[key], f2[key])
        else:
            result[key] = check(f1, f2, key)
    return result


def check(val1, val2, key):
    res_check = {}
    if key in val1:
        res_check['-'] = val1[key]
    if key in val2:
        res_check['+'] = val2[key]
    if res_check.get('-') == res_check.get('+'):
        return {' ': val1[key]}
    return res_check
