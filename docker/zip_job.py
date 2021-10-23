import os
import os.path
import zipfile
from pathlib import Path

def validate_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File {file_path} does not exists")

def create_zip_file(source_file_path):
    zip_file_name = f"{Path(source_file_path).stem}_{os.environ['VERSION']}.zip"
    zf = zipfile.ZipFile(zip_file_name, 'w')
    zf.write(source_file_path)
    zf.close()
    validate_file(zip_file_name)

arr = ['a','b','c','d']
for item in arr:
    file_name = f"{item}.txt"
    with open(file_name, 'w'): 
        pass
    validate_file(file_name)
    create_zip_file(file_name)
