import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')


project_name='cnnClassifier'

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "prams.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]



"""windows uses backward slash in path while in the list of files we have given forward slashes
so for windows to understand we are looping thru the list and passing it thru Path() which is imported
to convert it into a windows path"""

for filepath in list_of_files:
    filepath=Path(filepath) #converts into windows path
    filedir,filename=os.path.split(filepath) # as per the items eg it will give config to filedir and config.yaml to filename

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory;{filedir} for the file:{filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open (filepath,"w")as f:
            pass
            logging.info(f"creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists.")