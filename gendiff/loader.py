import json
import yaml


def load_file(file_name):

    if file_name.endswith((".yml", ".yaml")):
        file_data = yaml.load(open(file_name), Loader=yaml.Loader)
    else:
        file_data = json.load(open(file_name))
    return file_data
