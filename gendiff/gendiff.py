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
        file1_value = file1.get(key)
        file2_value = file2.get(key)
        diff_dict[key] = {
            "value1": file1_value,
            "value2": file2_value,
        }
        if file1_value == file2_value:
            diff_dict[key]["status"] = "equal"
        else:
            if isinstance(file1_value, dict) and isinstance(file2_value, dict):
                diff_dict[key] = {
                    "status": "nested",
                    "value": diff(file1_value, file2_value),
                }
            elif key in file1.keys() and key not in file2.keys():
                diff_dict[key]["status"] = "removed"
            elif key in file2.keys() and key not in file1.keys():
                diff_dict[key]["status"] = "added"
            else:
                diff_dict[key]["status"] = "changed"
    return diff_dict
