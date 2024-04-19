from typing import List

from openai import OpenAI
from openai.types.chat import ChatCompletion
from pydantic import BaseModel

from services.data_clean import str_clean


# open-ai
class PerMessage(BaseModel):
	role: str  # 声明各成员变量
	content: str


API_BASE = "https://api.lingyiwanwu.com/v1"
API_KEY = "8e29a997ae204127948e0486439af07c"
# MODEL = "yi-34b-chat-200k"
MODEL = "yi-34b-chat-0205"


def excute(messages: List[PerMessage]) -> ChatCompletion:
	global API_BASE
	global API_KEY
	global MODEL
	
	messages = [message.dict() for message in messages]  # 转为 json 对象
	
	print(f'提示语: messages: {messages}')# 答应提示语
	
	client = OpenAI(
		# defaults to os.environ.get("OPENAI_API_KEY")
		api_key=API_KEY,
		base_url=API_BASE
	)
	completion = client.chat.completions.create(
		model=MODEL,
		messages=messages,
		temperature=0.2
	)
	
	print(completion) # 打印01结果
	return completion


def re_excute(oldAnswer: PerMessage, msg: List[PerMessage]) -> str:
	oldContent = oldAnswer.content
	appendMsg = PerMessage(**oldAnswer.dict())  # 使用字典解包拷贝, 将生成答案附在msg内
	msg.append(appendMsg)
	appendMsg = PerMessage(role="user", content="请继续生成")
	msg.append(appendMsg)
	result: ChatCompletion = excute(msg)  # 再次询问
	content = oldContent + result.choices[0].message.content
	contentResult = str_clean.extract_json(content)
	return contentResult


def excute_clean(messages: List[PerMessage]) -> str:
	result: ChatCompletion = excute(messages)
	temp = result.choices[0].message
	content = temp.content
	# 数据清洗
	print(f'content: {content}, length: {len(content)}') # 打印数据清洗入参
	contentResult = str_clean.extract_json(content)
	# if contentResult == None and '{' in content: # 未找到JSON但是结果包含{, 则再执行一次, 至多执行5次
	# 	contentResult = re_excute(temp, messages)
	return contentResult
