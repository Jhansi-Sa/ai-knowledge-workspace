from pydantic import BaseModel, ConfigDict
import datetime

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    model_config= ConfigDict(from_attributes= True)

    id: int
    name: str
    email:str
    created_at: datetime.datetime

class UserUpdate(BaseModel):
    name:str
    email:str

class UserLogin(BaseModel):
    email:str
    password:str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str