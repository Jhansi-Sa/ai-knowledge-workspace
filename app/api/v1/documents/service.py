from fastapi import HTTPException
from .repository import save_document, get_all_documents_from_db, get_document_by_id_from_db, update_document_title_in_db, delete_document_from_db 
from fastapi import UploadFile
from .models import Document
from app.api.v1.users.models import User
from sqlalchemy.orm import Session
from pathlib import Path
from app.core.storage import save_file, get_file_size, get_file, delete_file
from fastapi.responses import FileResponse
from app.core.constants import MAX_FILE_SIZE, DOCUMENT_STATUS_READY, ALLOWED_FILE_EXTENSIONS

def upload_a_document(title: str, file: UploadFile, current_user: User, db: Session):
    if title.strip() == "":
        raise HTTPException(status_code=400, detail= "Invalid Title")

    file_name= file.filename
    if not file_name:
        raise HTTPException(status_code=400, detail= "Invalid File name")
    
    if Path(file_name).suffix.lower() not in ALLOWED_FILE_EXTENSIONS:
        raise HTTPException(status_code=400, detail= "Invalid File Type, only PDF's allowed")
    file_size=get_file_size(file)
    #need to implement this file size
    if  file_size> MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail= "Invalid File size, file size should be lower than 2 GB")
    
    #need to generate meta data later when we introduce s3 in AWS
    storage_key= save_file(file)
    document= Document(
        user_id= current_user.id,
        title= title,
        storage_key= storage_key,
        file_size= file_size,
        status= DOCUMENT_STATUS_READY
    )
    new_doc= save_document(document, db)
    return new_doc
    
def get_all_documents(current_user: User, db: Session):
    return get_all_documents_from_db(current_user.id, db)

def get_document_by_id(document_id: int, current_user: User, db: Session):
    document= get_document_by_id_from_db(document_id, db)
    if document is None:
        raise HTTPException(status_code=404, detail= "Document not found")
    if document.user_id!= current_user.id:
        raise HTTPException(status_code=403, detail= "Forbidden")
    return document

def update_document_title(document_id: int, title: str, current_user: User, db: Session):
    
    if title.strip()== "":
        raise HTTPException(status_code=400, detail="Inavlid Title. Title cannot be an empty value")
    document= get_document_by_id_from_db(document_id, db)
    if document is None:
        raise HTTPException(status_code=404, detail= "Document Not Found")
    if document.user_id != current_user.id:
        raise HTTPException(status_code=403, detail= "Forbidden") 
    update_document_title_in_db(document, title, db)
    return document

def delete_a_document(document_id: int, current_user: User, db: Session):
    document= get_document_by_id_from_db(document_id, db)
    if document is None:
        raise HTTPException(status_code=404, detail= "Document not found")
    if document.user_id != current_user.id:
        raise HTTPException(status_code=403, detail= "Forbidden")
    delete_file(document.storage_key)
    delete_document_from_db(document, db)
    return None

def download_file(document_id:int, current_user:User, db: Session):
    document= get_document_by_id_from_db(document_id, db)
    if document is None:
        raise HTTPException(status_code=404, detail= "File Not Found")
    if document.user_id != current_user.id:
        raise HTTPException(status_code=403, detail= "Forbidden")

    file_path= get_file(document.storage_key) 
    return FileResponse(path= file_path, filename= document.title+".pdf", media_type= "application/pdf")

