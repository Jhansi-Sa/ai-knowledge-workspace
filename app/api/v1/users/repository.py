from .schemas import UserCreate, UserUpdate
from app.core.security import hash_password
from sqlalchemy.orm import Session
from .models import User

#db=["admin@gmail.com", "test@gmail.com", "john@gmail.com"]

def save_user_to_database(user: UserCreate, db: Session):
    hashed_password= hash_password(user.password)
    new_user= User(
        name= user.name,
        email=user.email,
        hashed_password= hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    

def user_exists_by_email(email:str, db:Session):
    user= db.query(User).filter(User.email== email).first()
    return user is not None

def get_user_details_by_id(user_id: int, db: Session):
    user= db.query(User).filter(User.id==user_id).first()
    return user

def get_all_users_from_db(db:Session):
    user_list= db.query(User).all()
    return user_list

def update_user_details_in_db(user_id: int, user: UserUpdate, db: Session):
    existing_user=db.query(User).filter(User.id== user_id).first()
    if existing_user:
        existing_user.name=user.name
        existing_user.email=user.email
        db.commit()
        db.refresh(existing_user)
        return existing_user
    return None
    
def delete_user_details_in_db(user_id: int, db: Session):
    delete_user= db.query(User).filter(User.id== user_id).first()
    if delete_user:
        db.delete(delete_user)
        db.commit()
        return True
    return False

#login 
def get_user_by_email_from_db(email: str, db: Session):
    user= db.query(User).filter(User.email== email).first()
    return user

