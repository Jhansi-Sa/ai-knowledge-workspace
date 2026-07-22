from pydantic import BaseModel, ConfigDict, EmailStr
import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    model_config= ConfigDict(from_attributes= True)

    id: int
    name: str
    email:EmailStr
    created_at: datetime.datetime

class UserUpdate(BaseModel):
    name:str
    email:EmailStr

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str


    
