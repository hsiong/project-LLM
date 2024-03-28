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
                "content": "你是一个农业专家，请以专业、清晰的方式提供解答。请以中文回答,除非涉及特定缩写。不要回答与问题无关的部分,直接给出答案;严格按照回答格式回答问题"
            },
            {
                "role": "user",
                "content": "请回答西红柿-晚疫病的病虫害分类(真菌/病毒/生理性病害/虫害, 只用回答四选一), 回答格式如下: 病虫害分类为xxxxx"
            }
        ]'''
	# 使用json.loads将JSON字符串解码为Python列表  
	raw_data = json.loads(json_string)
	msg: List[openai_exec.PerMessage] = TypeAdapter(List[openai_exec.PerMessage]).validate_python(raw_data)
	
	result: ChatCompletion = openai_exec.excute(msg)


