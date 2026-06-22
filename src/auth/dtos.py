from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from fastapi import HTTPException

class RegisterDTO(BaseModel):
    name : str
    useranme: str
    password: str = Field(min_length=8)
    rePassword: str = Field(min_length=8)

    
    @model_validator(mode="after")
    def pass_check(self):
        if self.password != self.rePassword:
            raise HTTPException(status_code=400, detail={
                "error": "Password Do Not Match..."
            })
            
        return self
    
class LoginDTO(BaseModel):
    username: str
    password: str = Field

class UserResponseDTO(BaseModel):
    created_at: datetime
    name: str
    username: str
    last_login: datetime
    is_active: bool
