import json


def _get_value(item, depth, indent=4):
    if item == False:
        return "false"
    if item == True:
        return "true"
    if item is None:
        return "null"
    elif isinstance(item, dict):
        res = (
            json.dumps(item, indent=4)
            .replace('"', "")
            .replace(",", "")
            .split("\n")
        )
        for k, v in enumerate(res):
            if v.startswith(" "):
                res[k] = " " * indent + res[k]
        res[-1] = " " * indent + res[-1]
        return "\n".join(res)
    return item


def make_indent(depth, symbol=""):
    indent = depth * 4 * " "
    if symbol == "+":
        indent = indent[:-2] + "+ "
    elif symbol == "-":
        indent = indent[:-2] + "- "
    return indent


def make_result(depth, symbol, key, value):
    indent = make_indent(depth, symbol)
    return f"{indent}{key}: {value}\n"


def stylish(files_difference, indent=4, depth=1):

    keys = list(files_difference.keys())
    keys.sort()
    result = "{\n"
    for key in keys:
        value = files_difference[key].get("value")
        value1 = _get_value(files_difference[key].get("value1"), depth, indent)
        value2 = _get_value(files_difference[key].get("value2"), depth, indent)
        if files_difference[key]["status"] == "equal":
            indent1 = make_indent(depth)
            result = result + f"{indent1}{key}: {value1}\n"
        elif files_difference[key]["status"] == "nested":
            indent1 = make_indent(depth)
            result = (
                result
                + indent1
                + f"{key}: {stylish(value, indent=indent+4, depth=depth+1)}\n"
            )
        elif files_difference[key]["status"] == "removed":
            indent1 = make_indent(depth, symbol="-")
            result = result + f"{indent1}{key}: {value1}\n"
        elif files_difference[key]["status"] == "added":
            indent1 = make_indent(depth, symbol="+")
            result = result + f"{indent1}{key}: {value2}\n"
        elif files_difference[key]["status"] == "changed":
            indent1 = make_indent(depth, symbol="-")
            result = result + f"{indent1}{key}: {value1}\n"
            indent1 = make_indent(depth, symbol="+")
            result = result + f"{indent1}{key}: {value2}\n"
    result = result + "    " * (depth - 1) + "}"
    return result
