
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from app.api.v1.users.repository import get_user_details_by_id
from .token import verify_access_token
from .database import get_db
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def get_current_user(token: str= Depends(oauth2_scheme), db: Session= Depends(get_db)):
    
        payload= verify_access_token(token)
        user_id= payload["sub"]
        user= get_user_details_by_id(user_id, db)
        if user is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
        return user
    
