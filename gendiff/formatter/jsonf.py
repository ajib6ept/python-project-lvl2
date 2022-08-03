import json


def json_stylish(configs_difference):
    return json.dumps(configs_difference, sort_keys=True, indent=4)
