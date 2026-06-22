import os
import yaml

def read_yaml(key):
    with open(os.getcwd() + "/data/elements.yml",mode="r",encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data[key]