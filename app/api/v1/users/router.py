from fastapi import APIRouter, Depends
from .schemas import UserCreate, UserResponse, UserUpdate, TokenResponse, UserLogin
from .service import create_user, get_user_by_id, get_all_users_details, update_user_details_by_id, delete_user_details_by_id, authenticate_user
from sqlalchemy.orm import Session
from app.core.database import get_db
from typing import List
from app.core.dependencies import get_current_user
from .models import User
from fastapi.security import OAuth2PasswordRequestForm


router= APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/register", status_code=201, response_model= UserResponse) 
def register_user(user: UserCreate, db: Session= Depends(get_db)):
    return create_user(user, db)

@router.get("/me", response_model= UserResponse)
def get_me(current_user:User= Depends(get_current_user)):
    return current_user

@router.get("/{user_id}", status_code=200, response_model=UserResponse)
def get_user(user_id: int, db: Session= Depends(get_db)):
    return get_user_by_id(user_id, db)

@router.get("/",status_code=200, response_model=List[UserResponse])
def get_all_users(db: Session= Depends(get_db)):
    return get_all_users_details(db)

@router.put("/{user_id}", status_code=200, response_model= UserResponse)
def update_user_by_id(user_id: int, user: UserUpdate, db: Session= Depends(get_db)):
    return update_user_details_by_id(user_id, user, db)

@router.delete("/{user_id}", status_code=204)
def delete_user_by_id(user_id: int, db: Session= Depends(get_db)):
    return delete_user_details_by_id(user_id, db)


@router.post("/login", status_code=200, response_model= TokenResponse)
def user_login(form_data: OAuth2PasswordRequestForm= Depends(), db: Session= Depends(get_db)):
    return authenticate_user(form_data.username, form_data.password, db)

