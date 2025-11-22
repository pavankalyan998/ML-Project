from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT= '-e .'
def get_Requirements(file_path:str)->List[str]:
    '''
    This function will return the list of Requirments
    '''
    Requirements=[]
    with open(file_path) as file_obj:
        Requirements=file_obj.readlines()
        Requirements=[Req.replace("\n","")for Req in Requirements]

        if HYPEN_E_DOT in Requirements:
            Requirements.remove(HYPEN_E_DOT)
    return Requirements

setup(
name ='MLProject',
Version='0.0.1',
Author='pavan',
Author_email='pavandec1998@gmail.com',
packages=find_packages(),
install_requires=get_Requirements('Requirements.txt')

)