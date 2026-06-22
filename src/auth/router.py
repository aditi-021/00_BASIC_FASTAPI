#### three routes = register. login. auth


from fastapi import APIRouter, Depends, Request
from src.auth.dtos import RegisterDTO, LoginDTO, UserResponseDTO
from src.utils.base import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.controllers import RegisterController, LoginController, IsAuthController

authRouter = APIRouter(prefix="/auth")


@authRouter.post("/signup", response_model=UserResponseDTO)
async def Register(user:RegisterDTO, db:AsyncSession = Depends(get_db)):
    print("\n\n", user, "\n\n")
    return await RegisterController(user, db)


@authRouter.post("/login")
async def Login(user:LoginDTO, db:AsyncSession = Depends(get_db)):
    return await LoginController(user, db)


@authRouter.get("/user", response_model=UserResponseDTO)
async def UserDetails(request:Request, db:AsyncSession = Depends(get_db)):
    return await IsAuthController(request, db)

