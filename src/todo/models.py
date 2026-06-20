### "todos", id, title, description, completed, created_at -> updated_at

from datetime import datetime
from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from src.utils.base import Base

class TodoDB(Base):
    
    __tablename__ = "todos"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String())
    
    description : Mapped[str | None] = mapped_column(Text, default=None)
    
    completed: Mapped[bool] = mapped_column(default=False)
    
    created_at : Mapped[datetime] = mapped_column(
        DateTime(),
        server_default=func.now()  
    )
    
    
    
    
    
