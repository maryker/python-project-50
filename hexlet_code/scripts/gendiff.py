import argparse
import json



parser = argparse.ArgumentParser(
                    prog='gendiff',
                    description='Compares two configuration files and shows a difference.')

parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()


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
    return '{\n' + '\n'.join([f'{key}: {bool_to_str(value)}' for key, value in result.items()]) + '\n}'


def bool_to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def main():
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()