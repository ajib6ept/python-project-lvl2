import argparse
from gendiff.gendiff import generate_diff


def arg_parse():
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument(
        "-f", "-format", metavar="FORMAT", help="set format of output"
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))
