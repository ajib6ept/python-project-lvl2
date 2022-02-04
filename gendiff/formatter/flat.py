def _get_value(item):
    if item is False:
        return "false"
    if item is True:
        return "true"
    if item is None:
        return "null"
    elif isinstance(item, dict):
        return "[complex value]"
    return f"'{item}'"


def flat_stylish(files_difference, start_symbol="\n", start_key=""):
    keys = list(files_difference.keys())
    keys.sort()
    result = start_symbol
    for key in keys:
        value = files_difference[key].get("value")
        value1 = _get_value(files_difference[key].get("value1"))
        value2 = _get_value(files_difference[key].get("value2"))

        key1 = f"{start_key}.{key}" if start_key else key
        if files_difference[key]["status"] == "removed":
            removed_key_line = f"Property '{key1}' was removed\n"
            result = result + removed_key_line
        elif files_difference[key]["status"] == "added":
            added_key_line = (
                f"Property '{key1}' was added with value: {value2}\n"
            )
            result = result + added_key_line
        elif files_difference[key]["status"] == "changed":
            changed_line = (
                f"Property '{key1}' was updated. From {value1} to {value2}\n"
            )
            result = f"{result}{changed_line}"
        elif files_difference[key]["status"] == "nested":
            result = (
                f"{result}{flat_stylish(value,start_symbol='',start_key=key1)}"
            )
    return result
