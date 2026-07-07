from .schemas import UserCreate, UserUpdate, UserLogin, TokenResponse
from .repository import save_user_to_database, user_exists_by_email, get_user_details_by_id, get_all_users_from_db, update_user_details_in_db, delete_user_details_in_db, get_user_by_email_from_db
from fastapi import HTTPException
from .models import User
from sqlalchemy.orm import Session
from app.core.security import verify_password
from app.core.token import create_access_token

def create_user(user: UserCreate, db:Session):
    if user_exists_by_email(user.email, db):
        raise HTTPException(status_code=409, detail= "Email already exists")
    new_user=save_user_to_database(user, db)
    return new_user

def get_user_by_id(user_id, db:Session):
    user= get_user_details_by_id(user_id, db) 
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_all_users_details(db:Session):
    user_list= get_all_users_from_db(db)
    return user_list

def update_user_details_by_id(user_id: int, user:UserUpdate, db: Session):
    update_user= update_user_details_in_db(user_id, user, db)
    if update_user is None:
        raise HTTPException(status_code=404, detail= "User Not Found")
    return update_user

def delete_user_details_by_id(user_id: int, db: Session):
    if delete_user_details_in_db(user_id, db):
        return None
    raise HTTPException(status_code=404, detail="User Not Found")

def get_user_details_by_email(user:UserLogin, db: Session):
    existing_user=get_user_by_email_from_db(user.email, db)
    if existing_user:
        if verify_password(user.password, existing_user.hashed_password):
            payload= {
                "sub": str(existing_user.id),
                "email": existing_user.email
            }
            token= create_access_token(payload)
            return TokenResponse(
                access_token= token,
                token_type= "bearer"
            )
        raise HTTPException(status_code=401, detail= "Invalid Username or password")
    raise HTTPException(status_code=401, detail="Invalid Username or password")

        


