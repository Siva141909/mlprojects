from  setuptools  import setup,find_packages
from typing import List

hypne='-e .'
def get_requriments(file_path:str) -> List [str]:
    '''
    This function reads a requirements.txt file and returns a list of package names and their version numbers.
    
    '''
    requriments=[]
    with open(file_path) as f:
        requriments=f.readlines()
        requriments=[r.replace("\n","") for r in requriments]

        if hypne in requriments:
            requriments.remove(hypne)

    return requriments

setup(
    name='mlprojects',
    version='0.0.1',
    author='siva',
    author_email='rasivateja@gmail.com',
    packages=find_packages(),
    install_requires=get_requriments('requriments.txt')
)