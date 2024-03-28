# This is a sample Python script.
import json
from typing import List

from pydantic import TypeAdapter

import openai_exec

if __name__ == '__main__':
	# msg: List[openai_exec.PerMessage] = [openai_exec.PerMessage(role="user", content="你好")]
	json_string = '''[
            {
                "role": "system",
                "content": "你是一个农业专家，请以专业、清晰的方式提供解答。请以中文回答, 除非涉及特定缩写。每次回答保证是完整的"
            },
            {
                "role": "user",
                "content": "请回答西红柿-番茄细菌性软腐病的别名 病虫害分类(真菌/病毒/生理性病害/虫害) 危害部位 危害特征 发病条件 发病周期 传染性 传播途径 防治措施; 要求如下: 1.只能以json列表[{\\\"key\\\", \\\"value\\\"}] 返回, key为中文 2.详细写出危害特征/发病条件/危害特征/传播途径/防治措施, 每一项100字左右"
            },
            {
                "role": "assistant",
                "content": "回答格式如下:{\\\"种类\\\":\\\"value\\\",\\\"别名\\\":\\\"value0\\\",\\\"病虫害分类\\\":\\\"value1\\\",\\\"危害部位\\\":\\\"value2\\\",\\\"危害特征\\\":\\\"value3\\\",\\\"发病条件\\\":\\\"value4\\\",\\\"发病周期\\\":\\\"value5\\\",\\\"传染性\\\":\\\"value6\\\",\\\"传播途径\\\":\\\"value7\\\",\\\"防治措施\\\":\\\"value8\\\"}"
            }
        ]'''
	# 使用json.loads将JSON字符串解码为Python列表  
	raw_data = json.loads(json_string)
	msg: List[openai_exec.PerMessage] = TypeAdapter(List[openai_exec.PerMessage]).validate_python(raw_data)
	
	content = openai_exec.excute_clean(msg)
