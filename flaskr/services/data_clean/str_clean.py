import json
import re


def extract_json(text):
	match_general = re.search(r'\[[\s\S]*\](?=\s*)|\{[\s\S]*\}(?=\s*)', text)  # 匹配完整的JSON
	
	if match_general:
		jsonStr_general = match_general.group(0)
		# 尝试格式化捕获的JSON字符串以便清晰显示
		try:
			formatted_json_general = json.loads(jsonStr_general)
			formatted_json_str_general = json.dumps(formatted_json_general, indent=2, ensure_ascii=False)
			print("解析成功")
			return formatted_json_str_general
		except json.JSONDecodeError as e:
			print("解析错误:", e)
	else:
		print("没有找到JSON字符串")
	raise UserWarning('JSON解析错误')
