from dotenv import load_dotenv
load_dotenv()

import asyncio
# from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from time import sleep


def getLLM():
    # llm = ChatOpenAI(model="gpt4o-mini")
    llm = ChatAnthropic(model="claude-haiku-4-5-20251001")
    return response

async def chatController(question:str):
    llm = getLLM()
    # response = llm.invoke([{"role":"user", "content":question}])
    # return response.content
    
    response = llm.astream([{
        "role":"user",
        "content":question
    }])
    async for chunk in response:
        yield chunk.content
        await asyncio.sleep(0.06)
            
    