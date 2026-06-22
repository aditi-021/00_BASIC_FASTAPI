## Alembic - something  about database versioning
from src.utils.base import Base
from datetime import datetime
from sqlalchemy import DateTime, String, Text, func, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "users"
    
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    username: Mapped[str] = mapped_column(String(100))
    
    hashed_password: Mapped[str] = mapped_column(String(200))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    last_login: Mapped[datetime] = mapped_column(DateTime(), default=func.now())
    created_at: Mapped[datetime] = mapped_column(
        DateTime(),
        server_default=func.now()
    )