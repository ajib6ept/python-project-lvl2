from gendiff.gendiff import generate_diff

from ..cli import arg_parse


def main():
    args = arg_parse()
    result = generate_diff(
        args.first_file, args.second_file, format_name=args.format
    )
    print(result)
