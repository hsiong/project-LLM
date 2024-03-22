from typing import List

from openai import OpenAI
from pydantic import BaseModel


class PerMessage(BaseModel):
    role: str  # 声明各成员变量
    content: str


API_BASE = "https://api.lingyiwanwu.com/v1"
API_KEY = "mykey"
MODEL = "yi-34b-chat-200k"


def excute(messages: List[PerMessage]):
    global API_BASE
    global API_KEY
    global MODEL

    messages = [message.dict() for message in messages]  # 转为 json 对象

    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=API_KEY,
        base_url=API_BASE
    )
    completion = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )
    print(completion)
    return completion.dict()
