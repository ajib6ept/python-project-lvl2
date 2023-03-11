import json

import yaml


def parsing_data(raw_data, data_type):
    if data_type == "json":
        data = json.loads(raw_data)
    else:
        data = yaml.load(raw_data, Loader=yaml.Loader)
    return data
