# This is a sample Python script.
import json
from typing import List

from openai.types.chat import ChatCompletion
from pydantic import TypeAdapter

import openai_exec
from services.data_clean import str_clean



if __name__ == '__main__':
	# msg: List[openai_exec.PerMessage] = [openai_exec.PerMessage(role="user", content="你好")]
	json_string = '''[
            {
                "role": "system",
                "content": "你是一个农业专家，请以专业、清晰的方式提供解答。请以中文回答, 除非涉及特定缩写。"
            },
            {
                "role": "user",
                "content": "请回答西红柿的常见病虫害; 要求如下: 1.只能以json列表[{\\\"key\\\", \\\"value\\\"}] 返回, key为中文"
            }
        ]'''
	# 使用json.loads将JSON字符串解码为Python列表  
	raw_data = json.loads(json_string)
	msg: List[openai_exec.PerMessage] = TypeAdapter(List[openai_exec.PerMessage]).validate_python(raw_data)
	
	content = openai_exec.excute_clean(msg)


