import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO , format='[%(asctime)s]: %(message)s:')
logging.info("Your script started successfully")


list_of_files = [
    f"src/__init__.py",
    f"src/helper.py",
    '.env',
    'requirements.txt',
    'setup.py',
    'app.py',
    'research/trials.ipynb',
]

# logic to create folder structure
# This codes are help to create the files to the project automatically

for filepath in list_of_files:   # To find the os and set the slash accordingly
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


#To create the file directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as fp:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}, skipping creation.")












        