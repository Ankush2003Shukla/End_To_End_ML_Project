from setuptools import find_packages,setup
from typing import List

def get_requirements(path:str) -> List[str]:
    req = []
    with open(path) as file:
        req = file.readlines()
        req = [i.replace("\n"," ") for i in req]

    return req

setup(
    name = 'End_to_End_ML_project',
    version = '0.0.1',
    author = 'Ankush',
    author_email= 'shuklaankush2003@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)
print(setup)