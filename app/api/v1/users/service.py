from .schemas import UserCreate
from .repository import save_user_to_database, user_exists_by_email
from fastapi import HTTPException

def create_user(user: UserCreate):
    if user_exists_by_email(user.email):
        raise HTTPException(status_code=409, detail= "Email already exists")
    new_user=save_user_to_database(user)
    return new_user