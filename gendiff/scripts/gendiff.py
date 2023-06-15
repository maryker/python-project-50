import argparse
from gendiff.generate_diff import generate_diff


def get_args():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description='Compares two configuration \
                                     files and shows a difference.')

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    return parser.parse_args()


def main():
    args = get_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
