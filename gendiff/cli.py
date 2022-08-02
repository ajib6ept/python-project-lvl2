import argparse


def arg_parse():
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument(
        "-f",
        "--format",
        metavar="FORMAT",
        default="stylish",
        help="set format of output",
        choices=["stylish", "plain", "json"],
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    return args
