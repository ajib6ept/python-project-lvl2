import argparse
import json


def generate_diff(file_path1, file_path2):

    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    keys = list(set(list(file1.keys()) + list(file2.keys())))
    keys.sort()
    out = "{\n"
    for key in keys:
        if file1.get(key) == file2.get(key):
            out = out + "    " + f"{key}: {file2[key]}\n"
        else:
            if key in file1.keys():
                out = out + "  " + f"- {key}: {file1[key]}\n"
            if key in file2.keys():
                out = out + "  " + f"+ {key}: {file2[key]}\n"
    out = out + "}"
    return out


def arg_parse():
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument(
        "-f", "-format", metavar="FORMAT", help="set format of output"
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))
