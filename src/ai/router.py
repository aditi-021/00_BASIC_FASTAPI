from fastapi import APIRouter
from src.ai.qna import chatController
from fastapi.responses import StreamingResponse

aiRoute = APIRouter(prefix="/ai")

@aiRoute.get("/chat/{question}")
async def chat(question:str):
    return StreamingResponse(
        chatController(question),
        media_type = "text/plain"
    )
