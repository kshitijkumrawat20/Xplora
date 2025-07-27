from setuptools import find_packages, setup
from typing import List 
 
def get_requirements()-> List[str]:
    """
    This function will return list of requirements
    """

    requirements_list: List[str] = []
    try:
        ## Open and read the requirements.txt
        with open('requirements.txt','r') as file: 
            lines = file.readlines()
            # process each file 
            for line in lines:
                # strip whitespace and new line character
                requirement = line.strip()
                # ignore empty line and -e 
                if requirement and requirement != '-e .':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirements_list
print(get_requirements())


setup(
    name = "Xplora",
    version = "0.0.1",
    author="Kshitij kumrawat",
    author_email="kshitijk146@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()

)
