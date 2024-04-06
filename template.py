import os
from pathlib import Path
import logging
#Setting up logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "mlProject"



list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"


]



for filepath in list_of_files:
    #pathlib use for the various os has various format bt pathlib fixed that problem 
    filepath = Path(filepath)
    #here i separate the folder and file using the split function
    filedir, filename = os.path.split(filepath)
    # Checks if the directory part is exist or not if not exixt then creating .Logs this action using the logging module.
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
    #again chech if the file is exists or not and the size of the file 0 or not if any of condition true then file will be created 
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    #otherwise file already exists 
    else:
        logging.info(f"{filename} is already exists")