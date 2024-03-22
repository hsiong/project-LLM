from typing import List

from flask import Blueprint, request
from pydantic import BaseModel

from services.lingyiwanwu.chat import openai_exec
from services.lingyiwanwu.chat.openai_exec import PerMessage

lingyi_api = Blueprint('lingyi', __name__)


@lingyi_api.route('/chat', methods=['POST'])
def chat():
    # 解析请求体中的JSON数据为PerMessageList对象
    data = PerMessageList.parse_obj(request.json)
    print(f'data.messages: {data.messages}')
    return openai_exec.excute(data.messages)


# 定义一个新的Pydantic模型，用于接收PerMessage对象的列表
class PerMessageList(BaseModel):
    messages: List[PerMessage]
