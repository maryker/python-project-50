import argparse
from hexlet_code.modules.generate_diff import generate_diff
from hexlet_code.modules.formater import stylish


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
    print(stylish(generate_diff(args.first_file, args.second_file)))


if __name__ == '__main__':
    main()
