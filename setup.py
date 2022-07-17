from setuptools import setup,find_packages
from typing import List


#Declaring variables for setup functions
PROJECT_NAME="forest_cover_type_predictor"
VERSION="0.0.1"
AUTHOR="Kunal Chowdhury"
DESRCIPTION="This is forest cover predictor ML project"
REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list



setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESRCIPTION,

# This find_packages() basically scans the root folder for all folders having a __init__ file and returns it. We can hardode as "housing" as well
    packages = find_packages(), #["housing"]
    install_requires = get_requirements_list()
    )