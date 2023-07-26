from gendiff.parser import parse
from gendiff.formaters.stylish import form_stylish
from gendiff.formaters.plain import form_plain
from gendiff.formaters.JSON import form_json
from gendiff.make_diff import make_diff


FORMATERS = {'stylish': form_stylish, 'json': form_json, 'plain': form_plain}


def generate_diff(file1, file2, form='stylish'):
    f1 = parse(file1)
    f2 = parse(file2)
    formater = FORMATERS.get(form, form_stylish)
    return formater(make_diff(f1, f2))
