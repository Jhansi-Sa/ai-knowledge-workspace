from fastapi import APIRouter
from .schemas import UserCreate, UserResponse
from .service import create_user

router= APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/register", status_code=201, response_model= UserResponse) 
def register_user(user: UserCreate):
    return create_user(user)