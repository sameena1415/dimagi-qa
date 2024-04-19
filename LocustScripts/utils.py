import csv
import json

import yaml


def load_csv_data(path, model=None):
    with path.open() as f:
        reader = csv.DictReader(f)
        data = list(reader)

    if model:
        return [model(**row) for row in data]
    return data


def load_yaml_data(path, model=None):
    with path.open() as f:
        data = yaml.safe_load(f)

    if model:
        return model(**data)
    return data


def load_json_data(path):
    with path.open() as f:
        return json.load(f)
