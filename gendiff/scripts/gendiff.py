import argparse
from gendiff.modules.gendiff import generate_diff
from gendiff.modules.formaters.stylish import form_stylish
from gendiff.modules.formaters.plain import form_plain
from gendiff.modules.formaters.JSON import form_json


def parsing():
    parser = argparse.ArgumentParser(
                        prog='gendiff',
                        description='Compares two configuration \
                                    files and shows a difference.')

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    return parser.parse_args()


def main():
    args = parsing()
    if not args.format:
        print(generate_diff(args.first_file, args.second_file, form_stylish))
    elif args.format == 'plain':
        print(generate_diff(args.first_file, args.second_file, form_plain))
    elif args.format == 'json':
        print(generate_diff(args.first_file, args.second_file, form_json))


if __name__ == '__main__':
    main()
