import yaml
from parent.exception import ForestException
import os,sys

def read_yaml_file(file_path:str)-> dict:
    """This function will read the config.yaml file which has all the configuration info"""

    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise ForestException(e,sys) from e