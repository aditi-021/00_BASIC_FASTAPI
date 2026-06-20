from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker, create_async_engine, AsyncAttrs)
from sqlalchemy.orm import DeclarativeBase
from src.utils.settings import setting

## create a connector = connect with my db
## user -> connect database - session - session creator

engine = create_async_engine(url=setting.DATABASE_URL, echo = setting.DEBUG)

AsyncLocalSession = async_sessionmaker(
    bind=engine
    #connection pool -> true if we want always on session
    
)

class Base(AsyncAttrs, DeclarativeBase):
    pass

async def get_db():
    ##session automcatically closes after the work
    async with AsyncLocalSession() as session:
        yield session