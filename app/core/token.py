from datetime import datetime, timedelta, timezone
from jose import jwt
from app.core.config import (DATABASE_URL, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES)
from fastapi import HTTPException

def create_access_token(data: dict):
    to_encode= data.copy()
    expire= datetime.now(timezone.utc)+timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode["exp"]= expire

    token= jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_access_token(token: str):
    try:
        payload= jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    

