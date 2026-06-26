from dotenv import load_dotenv
load_dotenv()


from src.todo.dtos import (TodoAiCreateDTO, TodoCreateDTO)
# from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic


def getLLM():
    # llm = ChatOpenAI(model="gpt-4o-mini")
    llm = ChatAnthropic(model="claude-haiku-4-5-20251001")
    llm = llm.with_structured_output(TodoCreateDTO)
    return llm
    


def get_todo_object(rawQuery:TodoAiCreateDTO):
    # print(rawQuery.raw_query)
    llm = getLLM()
    payload = llm.invoke([{"role":"user", "content":rawQuery.raw_query}])
    return payload