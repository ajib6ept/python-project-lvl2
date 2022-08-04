def _get_value(item):
    if item is False:
        return "false"
    if item is True:
        return "true"
    if item is None:
        return "null"
    if isinstance(item, dict):
        return "[complex value]"
    if isinstance(item, int):
        return item
    return f"'{item}'"


def plain_stylish(configs_difference):
    result = create_diff_plain(configs_difference, path="")
    return result


def create_diff_plain(configs_difference, path=""):
    keys = list(configs_difference.keys())
    keys.sort()
    result = ""
    for key in keys:
        value = configs_difference[key].get("value")
        value1 = _get_value(configs_difference[key].get("value1"))
        value2 = _get_value(configs_difference[key].get("value2"))

        key1 = f"{path}.{key}" if path else key
        if configs_difference[key]["type"] == "removed":
            removed_key_line = f"Property '{key1}' was removed\n"
            result = "".join([result, removed_key_line])
        elif configs_difference[key]["type"] == "added":
            added_key_line = (
                f"Property '{key1}' was added with value: {value2}\n"
            )
            result = "".join([result, added_key_line])
        elif configs_difference[key]["type"] == "changed":
            changed_line = (
                f"Property '{key1}' was updated. From {value1} to {value2}\n"
            )
            result = "".join([result, changed_line])
        elif configs_difference[key]["type"] == "nested":
            result = f"{result}{create_diff_plain(value, path=key1)}"
    result = result.rstrip() if not path else result
    return result
