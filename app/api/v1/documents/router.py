from fastapi import APIRouter, Depends, UploadFile, File, Form
from app.core.database import get_db
from app.core.dependencies import get_current_user
from sqlalchemy.orm import Session
from .models import Document
from .service import upload_a_document, get_all_documents, get_document_by_id, update_document_title, delete_a_document, download_file
from .schemas import DocumentResponse
from app.api.v1.users.models import User
from typing import List


router= APIRouter(
    prefix="/documents", 
    tags= ["Documents"]
)

@router.post("/", status_code=201, response_model= DocumentResponse)
def upload_document(title: str= Form(...), file: UploadFile= File(...), current_user: User= Depends(get_current_user), db: Session =Depends(get_db)):
    return upload_a_document(title, file, current_user, db)

@router.get("/", status_code=200, response_model= List[DocumentResponse])
def get_documents(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_all_documents(current_user, db)

@router.get("/{document_id}", status_code=200, response_model= DocumentResponse)
def get_document(document_id: int, current_user: User = Depends(get_current_user), db: Session= Depends(get_db)):
    return get_document_by_id(document_id, current_user, db)

@router.put("/{document_id}", status_code=200, response_model= DocumentResponse)
def update_title(document_id: int, title: str= Form(...), current_user: User= Depends(get_current_user), db: Session= Depends(get_db)):
    return update_document_title(document_id, title, current_user, db)

@router.delete("/{document_id}", status_code=204)
def delete_document(document_id: int, current_user: User= Depends(get_current_user), db: Session= Depends(get_db)):
    return delete_a_document(document_id, current_user, db)

@router.get("/{document_id}/download", status_code=200)
def download_document(document_id: int, current_user: User= Depends(get_current_user), db: Session= Depends(get_db)):
    return download_file(document_id, current_user, db)
