import json


def make_lines_from_dict(dict_item, indent):
    res = (
        json.dumps(dict_item, indent=4)
        .replace('"', "")
        .replace(",", "")
        .split("\n")
    )
    for k, v in enumerate(res):
        if v.startswith(" "):
            res[k] = " " * indent + res[k]
    res[-1] = " " * indent + res[-1]
    return "\n".join(res)


def _get_value(item, indent=4):
    if item is False:
        return "false"
    if item is True:
        return "true"
    if item is None:
        return "null"
    elif isinstance(item, dict):
        return make_lines_from_dict(item, indent)
    return item


def make_indent(depth, symbol=""):
    indent = depth * 4 * " "
    if symbol == "+":
        indent = indent[:-2] + "+ "
    elif symbol == "-":
        indent = indent[:-2] + "- "
    return indent


def stylish(configs_difference, depth=1):  # noqa: C901

    keys = list(configs_difference.keys())
    keys.sort()
    result = "{\n"
    for key in keys:
        value = configs_difference[key].get("value")
        value1 = _get_value(configs_difference[key].get("value1"), depth * 4)
        value2 = _get_value(configs_difference[key].get("value2"), depth * 4)
        if configs_difference[key]["type"] == "equal":
            indent = make_indent(depth)
            result = "".join([result, f"{indent}{key}: {value1}\n"])
        elif configs_difference[key]["type"] == "nested":
            indent = make_indent(depth)
            nested_result = f"{key}: {stylish(value, depth=depth+1)}\n"
            result = "".join([result, indent, nested_result])
        elif configs_difference[key]["type"] == "removed":
            indent = make_indent(depth, symbol="-")
            result = "".join([result, f"{indent}{key}: {value1}\n"])
        elif configs_difference[key]["type"] == "added":
            indent = make_indent(depth, symbol="+")
            result = "".join([result, f"{indent}{key}: {value2}\n"])
        elif configs_difference[key]["type"] == "changed":
            indent = make_indent(depth, symbol="-")
            result = "".join([result, f"{indent}{key}: {value1}\n"])
            indent = make_indent(depth, symbol="+")
            result = "".join([result, f"{indent}{key}: {value2}\n"])
    result = "".join([result, "    " * (depth - 1), "}"])
    return result
