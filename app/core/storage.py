from fastapi import UploadFile
from pathlib import Path
import shutil
import uuid

UPLOAD_DIR= Path("uploads")
UPLOAD_DIR.mkdir(exist_ok= True)
def save_file(file: UploadFile) ->str:
    file_name= file.filename
    
    extension_name= Path(file_name).suffix.lower()
    unique_file= str(uuid.uuid4())+extension_name

    file_directory= UPLOAD_DIR/unique_file

    with open(file_directory, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return str(file_directory)


def get_file_size(file:UploadFile) -> int:

    file.file.seek(0,2)

    file_size= file.file.tell()

    file.file.seek(0)

    return file_size

def delete_file(storage_key):
    file_path= Path(storage_key)
    if file_path.exists():
        file_path.unlink()
        
def get_file(storage_key):
    file_path=Path(storage_key)
    if file_path.exists():
        return file_path
    raise FileNotFoundError(f"File not found: {storage_key}")