import json


def json_stylish(files_difference):
    return json.dumps(files_difference, sort_keys=True, indent=4)
