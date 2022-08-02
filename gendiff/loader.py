def read_data(data_source):
    with open(data_source, "r") as f:
        output = f.read()
    return output


def get_data_type(data_source):
    if data_source.endswith((".yml", ".yaml")):
        data_type = "yaml"
    else:
        data_type = "json"
    return data_type
