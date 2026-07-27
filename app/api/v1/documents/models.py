from app.core.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

class Document(Base):
    __tablename__= "documents"
    id= Column(Integer, primary_key= True)
    user_id= Column(Integer, ForeignKey('users.id'))
    title= Column(String, nullable= False)
    storage_key= Column(String, nullable= False)
    file_size= Column(Integer)
    status= Column(String, nullable=False)
    created_at=Column(DateTime, nullable=False, server_default=func.now())

    #Relationships
    user= relationship("User", back_populates= "documents")
    
