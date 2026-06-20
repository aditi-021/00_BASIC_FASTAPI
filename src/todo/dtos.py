from pydantic import BaseModel, Field
from datetime import datetime

class TodoCreateDTO(BaseModel):
    title : str = Field(min_length=10)
    description: str = ""
    completed: bool = False


class TodoReturnResponse(BaseModel):
    title : str
    description : str = ""
    completed: bool = False
    id: int
    created_at: datetime
    
    