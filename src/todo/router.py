
from fastapi import APIRouter, Request, Depends
from src.todo.controllers import getAllTask, createNewTask, deleteTask
from src.todo.dtos import TodoCreateDTO, TodoReturnResponse
from src.utils.base import get_db
from sqlalchemy.ext.asyncio import AsyncSession
todoRoute = APIRouter(prefix="/todo")

## path params, query params

@todoRoute.get("/", response_model=list[TodoReturnResponse])
async def getAllTodos(request:Request, db:AsyncSession = Depends(get_db)):
    return await getAllTask(None,db)


@todoRoute.get("/{todoId}", status_code=200)
async def getOneTodo(todoId:int):
    return getAllTask(todoId)   


@todoRoute.post("/", response_model=TodoReturnResponse)
async def createNewTodo(todoData:TodoCreateDTO, db:AsyncSession = Depends(get_db)):
    return await createNewTask(todoData, db)


@todoRoute.delete("/", status_code=200)
async def deleteOneTodo(todoId:int):
    return deleteTask(todoId)  