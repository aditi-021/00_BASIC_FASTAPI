
from fastapi import HTTPException
from src.todo.dtos import TodoCreateDTO
from src.todo.models import TodoDB
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


async def getAllTask(todoId:int | None = None, db:AsyncSession = None):
    result = await db.execute(
        select(TodoDB)
    )
    
    return list(result.scalars())


async def createNewTask(todoData:TodoCreateDTO, db:AsyncSession = None):
    todo = TodoDB(
        **todoData.model_dump()
    )
    db.add(todo)
    await db.commit()
    await db.refresh(todo)
    return todo
    


def deleteTask(taskIndex:int):
    return {"message":"Task Deleted......"}
    
    



