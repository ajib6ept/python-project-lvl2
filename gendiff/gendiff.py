from gendiff.loader import read_data, get_data_type
from gendiff.parser import parsing_data
from gendiff.formatter.tools import get_formatter


def generate_diff(data_path1, data_path2, format_name="stylish"):

    raw_data1 = read_data(data_path1)
    raw_data2 = read_data(data_path2)

    config1_type = get_data_type(data_path1)
    config2_type = get_data_type(data_path2)

    config1 = parsing_data(raw_data1, config1_type)
    config2 = parsing_data(raw_data2, config2_type)

    files_difference = diff(config1, config2)
    formatter = get_formatter(format_name)
    result = formatter(files_difference)

    return result


def diff(config1, config2):

    diff_dict = {}
    keys = config1.keys() | config2.keys()
    for key in keys:
        config1_value = config1.get(key)
        config2_value = config2.get(key)
        diff_dict[key] = {
            "value1": config1_value,
            "value2": config2_value,
        }
        if config1_value == config2_value:
            diff_dict[key]["type"] = "equal"
        elif isinstance(config1_value, dict) and isinstance(
            config2_value, dict
        ):
            diff_dict[key] = {
                "type": "nested",
                "value": diff(config1_value, config2_value),
            }
        elif key in config1.keys() and key not in config2.keys():
            diff_dict[key]["type"] = "removed"
        elif key in config2.keys() and key not in config1.keys():
            diff_dict[key]["type"] = "added"
        else:
            diff_dict[key]["type"] = "changed"
    return diff_dict
