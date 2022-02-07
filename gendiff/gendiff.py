from gendiff.loader import load_file
from gendiff.formatter.default import stylish
from gendiff.formatter.flat import flat_stylish
from gendiff.formatter.jsonf import json_stylish

FORMATTERS = {
    "stylish": stylish,
    "plain": flat_stylish,
    "json": json_stylish,
}


def generate_diff(file_path1, file_path2, format_name="stylish"):

    file1 = load_file(file_path1)
    file2 = load_file(file_path2)

    files_difference = diff(file1, file2)

    result = FORMATTERS[format_name](files_difference)

    return result


def diff(file1, file2):

    diff_dict = {}
    keys = list(set(list(file1.keys()) + list(file2.keys())))
    for key in keys:
        if file1.get(key) == file2.get(key):
            diff_dict[key] = {
                "status": "equal",
                "value1": file1.get(key),
                "value2": file2.get(key),
            }
        else:
            if isinstance(file1.get(key), dict) and isinstance(
                file2.get(key), dict
            ):
                diff_dict[key] = {
                    "status": "nested",
                    "value": diff(file1.get(key), file2.get(key)),
                }
            elif key in file1.keys() and key not in file2.keys():
                diff_dict[str(key)] = {
                    "status": "removed",
                    "value1": file1.get(key),
                    "value2": file2.get(key),
                }
            elif key in file2.keys() and key not in file1.keys():
                diff_dict[str(key)] = {
                    "status": "added",
                    "value1": file1.get(key),
                    "value2": file2.get(key),
                }
            else:
                diff_dict[str(key)] = {
                    "status": "changed",
                    "value1": file1.get(key),
                    "value2": file2.get(key),
                }
    return diff_dict
