from services.data_clean.str_clean import extract_json

# 示例输入
inputs = '''
content: {  "西红柿细菌性软腐病": "晚疫病",  "别名": "番茄晚疫病",  "病虫害分类": "真菌病害",  "危害部位": "叶片、茎、果实",  "危害特征": "病斑圆形或不定形，边缘不规则，病部变软腐烂，表面有白色霉层", "发病条件": "高湿、低温环境，适宜温度为18-24℃",  "发病周期": "全年均可发生，多雨季节易发",  "传染性": "强",  "传播途径": "病菌通过雨水、灌溉水传播",  "防治措施": "选用抗病品种，合理密植，及时清除病叶，使用杀菌剂如霜霉威、甲霜灵等",}, length: 260
'''
extracted_data = extract_json(inputs)
print(f'extracted_data: {extracted_data}')

