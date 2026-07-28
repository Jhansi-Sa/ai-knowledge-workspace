from sqlalchemy.orm import Session
from .models import Document
from sqlalchemy import desc

def save_document(document: Document, db: Session):

    db.add(document)
    db.commit()
    db.refresh(document)
    return document

def get_all_documents_from_db(user_id, db: Session):
    document_list= db.query(Document).filter(Document.user_id== user_id).order_by(desc(Document.created_at)).all()
    return document_list

def get_document_by_id_from_db(document_id, db: Session):
    document= db.query(Document).filter(Document.id== document_id).first()
    return document

def update_document_title_in_db(document, title, db: Session):
        document.title = title
        db.commit()
        db.refresh(document)
        return document

def delete_document_from_db(document, db: Session):
    db.delete(document)
    db.commit()
    

    
