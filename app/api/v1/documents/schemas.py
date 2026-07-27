from pydantic import BaseModel, ConfigDict
import datetime

class DocumentResponse(BaseModel):
    model_config= ConfigDict(from_attributes= True)

    id: int
    title: str
    status: str
    file_size: int
    created_at: datetime.datetime