from gendiff.modules.parser import parser
from gendiff.modules.formaters.stylish import form_stylish
from gendiff.modules.formaters.plain import form_plain
from gendiff.modules.formaters.JSON import form_json
from gendiff.modules.make_diff import make_diff


FORMATERS = {'stylish': form_stylish, 'json': form_json, 'plain': form_plain}


def generate_diff(file1, file2, form='stylish'):
    f1 = parser(file1)
    f2 = parser(file2)
    formater = FORMATERS.get(form, form_stylish)
    return formater(make_diff(f1, f2))
