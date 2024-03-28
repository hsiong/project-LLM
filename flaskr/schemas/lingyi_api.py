from typing import List

from flask import Blueprint, request
from openai.types.chat import ChatCompletion
from pydantic import BaseModel

from services.lingyiwanwu.chat import openai_exec
from services.lingyiwanwu.chat.openai_exec import PerMessage

lingyi_api = Blueprint('lingyi', __name__)

# 返回json格式的数据
@lingyi_api.route('/chat', methods=['POST'])
def chat() -> str:
	data = PerMessageList.parse_obj(request.json)
	msg = data.messages
	result: ChatCompletion = openai_exec.excute(msg)
	temp = result.choices[0].message
	content = temp.content
	return content

# 返回json格式的数据
@lingyi_api.route('/chatJson', methods=['POST'])
def chatJson() -> str:
	# 解析请求体中的JSON数据为PerMessageList对象
	data = PerMessageList.parse_obj(request.json)
	msg = data.messages
	content = openai_exec.excute_clean(msg)
	return content


# 定义一个新的Pydantic模型，用于接收PerMessage对象的列表
class PerMessageList(BaseModel):
	messages: List[PerMessage]
