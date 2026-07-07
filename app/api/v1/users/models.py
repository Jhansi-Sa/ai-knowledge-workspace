from .database import Base
from sqlalchemy import Column, Integer, String, DateTime, func

class User(Base):
    __tablename__= "users"
    id= Column(Integer, primary_key= True)
    name= Column(String, nullable=False)
    email= Column(String, nullable=False, unique= True)
    hashed_password= Column(String, nullable=False)
    created_at= Column(DateTime, nullable=False, server_default= func.now())

