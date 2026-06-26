""" Async & await, sync
1. async & await - when i/o blocking task, i(process) is waiting for a task but other process can start till then
2. sync - when cpu/compute blocking task, i(process) is waiting for a task and other process can't start till then
"""
from fastapi import FastAPI
from src.todo.router import todoRoute
from src.auth.router import authRouter
from src.ai.router import aiRoute
from src.utils.settings import setting
from contextlib import asynccontextmanager
from src.utils.base import Base, engine

### the funstion not needed when we have ambelic and table i
# ## using this funtion as context manager
# @asynccontextmanager
# async def onStart(app):
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
        
#     print("DB Connection Done")
#     yield
#app = FastAPI(lifespan=onStart)

app = FastAPI()

@app.get("/health")
def Health():
    return {"status":"Success"}


app.include_router(todoRoute, prefix="/v1")
app.include_router(authRouter, prefix="/v1")
app.include_router(aiRoute, prefix="/v1")