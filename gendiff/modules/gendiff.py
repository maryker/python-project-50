from gendiff.modules.parser import parser
from gendiff.modules.formaters.stylish import form_stylish


def generate_diff(file1, file2, form=form_stylish):
    f1 = parser(file1)
    f2 = parser(file2)

    def inner(f1, f2):
        result = {}
        keys = set(f1).union(set(f2))
        for key in sorted(keys):
            if isinstance(f1.get(key, None), dict) and\
                    isinstance(f2.get(key, None), dict):
                result[key] = inner(f1[key], f2[key])
            else:
                result[key] = check(f1, f2, key)
        return result

    return form(inner(f1, f2))


def check(val1, val2, key):
    res_check = {}
    if key in val1:
        res_check['-'] = val1[key]
    if key in val2:
        res_check['+'] = val2[key]
    if res_check.get('-', None) == res_check.get('+', None):
        return {' ': val1[key]}
    return res_check
