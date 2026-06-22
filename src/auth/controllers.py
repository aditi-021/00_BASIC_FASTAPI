## check that if user exist or not - hash the password - pwdlib
## login - check that if user exist or not - hash the password again and == hased_password if True
## then generate the JWT toekn - that lib for token is pyjwt

from fastapi import HTTPException, status, Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timedelta
from src.auth.dtos import RegisterDTO, LoginDTO
from src.auth.models import User
from src.utils.settings import setting


### libs for ajwt token and hash the password
from pwdlib import PasswordHash
import jwt

hashalgo = PasswordHash.recommended()

def get_hashed_password(password:str) -> str:
    return hashalgo.hash(password)

def verify_password(password: str, hash_pass:str) -> bool:
    return hashalgo.verify(password, hash_pass)
    

async def RegisterController(user: RegisterDTO, db:AsyncSession):
    isUser = await db.execute(
        select(User).where(User.username == user.useranme)
    )
    if isUser.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Username already exist..")
    
    newUser = User(
        name = user.name,
        username = user.useranme,
        hashed_password = get_hashed_password(user.rePassword)
    )
    
    db.add(newUser)
    await db.commit()
    await db.refresh(newUser)
    
    return newUser

async def LoginController(user:LoginDTO, db:AsyncSession):
    isUser = await db.execute(
        select(User).where(User.username == user.username)
    )
    isUser = isUser.scalar_one_or_none()
    
    if not isUser:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You entered wrong username")
    
    if not verify_password(user.password, isUser.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You have entered wrong password")
    
    expTime = datetime.now() + timedelta(minutes=30)
    token = jwt.encode({"_id":isUser.id, "exp":expTime}, setting.AUTH_SECRET_KEY, "HS256")
    return {"token": token}
    

async def IsAuthController(request:Request, db:AsyncSession):
    token = request.headers.get("authorization", "")
    token = token.spilt(" ")[-1]
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"error":"You are Unathorized !"})
    
    try:
        data = jwt.decode(token, setting.AUTH_SECRET_KEY, "HS256")
    except:
        data = {}
    user_id = data.get("_id")
    time = data.get("exp")
    
    if time < datetime.now():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"error":"Token Expired..."})
    
    user = await db.execute(select(User).where(User.id == user_id))
    user = user.scalar_one_or_none
    
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"error":"You are unauthorized!"})
    
    return user
    

    
