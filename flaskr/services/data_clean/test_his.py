from services.data_clean.str_clean import extract_json

'''
```json
[
	{ "key": "晚疫病",   "value": "Phytophthora infestans" },
	{ "key": "早疫病",    "value": "Alternaria solani" },
	{ "key": "灰霉病",    "value": "Botrytis cinerea" },
	{ "key": "叶斑病",    "value": "Septoria lycopersici" },
	{ "key": "病毒病",    "value": "Viruses (e.g., TMV)" },
	{ "key": "线虫病害",  "value": "Nematodes (e.g., Meloidogyne spp.)" },
	{ "key": "蚜虫",      "value": "Aphids (e.g., Myzus persicae)" },
	{ "key": "白粉虱",    "value": "Whiteflies (e.g., Trialeurodes vaporariorum)" },
	{ "key": "红蜘蛛",    "value": "Mites (e.g., Tetranychus urticae)" },
	{ "key": "马铃薯甲虫", "value": "Colorado potato beetle (Leptinotarsa decemlineata)" },
	{ "key": "番茄夜蛾",   "value": "Tomato fruitworm or corn earworm (Helicoverpa zea)" },
]
```
'''

# 示例输入
inputs = '''
content: 当然可以。以下是以JSON列表形式呈现的西红柿常见病虫害及其对应的英文名称：

```json
[
  {
    "key": "晚疫病",
    "value": "Late blight (Phytophthora infestans)"
  },
  {
    "key": "早疫病",
    "value": "Early blight (Alternaria solani)"
  },
  {
    "key": "叶霉病",
    "value": "Leaf mold (Cladosporium fulvum)"
  },
  {
    "key": "灰霉病",
    "value": "Gray mold (Botrytis cinerea)"
  },
  {
    "key": "病毒病",
    "value": "Viral diseases (e.g., Tomato mosaic virus, Cucumber mosaic virus)"
  },
  {
    "key": "蚜虫",
    "value": "Aphids (e.g., Myzus persicae)"
  },
  {
    "key": "白粉虱",
    "value": "Whiteflies (e.g., Trialeurodes vaporariorum)"
  },
  {
    "key": "烟粉虱",
    "value": "Bemisia tabaci (Silverleaf whitefly)"
  },
  {
    "key": "潜叶蝇",
    "value": "Leafminers (e.g., Liriomyza trifolii)"
  },
  {
    "key": "番茄夜蛾",
    "value": "Tomato fruitworm or corn earworm (Helicoverpa zea)"
  },
  {
    "key": "红蜘蛛",
    "value": "Red spider mites (Tetranychus evansi)"
  },
  {
    "key": "线虫",
    "value": "Nematodes (e.g., Meloidogyne incognita)"
  ]
```

这些疾病和害虫对西红柿种植者来说是很, length: 1051
'''

inputs = '''
content: JSON列表格式如下：
```json
[
  {
    "key": "叶霉病",
    "value": "灰白色或紫灰色霉层"
  },
  {
    "key": "早疫病",
    "value": "圆形至近于菱形褐色病斑"
  },
  {
    "key": "晚疫病",
    "value": "水浸状暗绿色病斑"
  },
  {
    "key": "病毒病",
    "value": "黄化、坏死和畸形"
  },
  {
    "key": "蚜虫",
    "value": "刺吸式口器吸取汁液，传播病毒"
  },
  {
    "key": "白粉虱",
    "value": "刺吸式口器吸取汁液，造成叶片褪绿黄化"
  },
  {
    "key": "红蜘蛛",
    "value": "吸取植物汁液，导致叶片失绿并出现黄棕色斑点"
  },
  {
    "key": "线虫",
    "value": "寄生在根部，引起根系发育不良，影响植株生长"
  },
  {
    "key": "细菌性青枯病",
    "value": "维管束褐变，茎及叶缘萎蔫"
  },
  {
    "key": "真菌性枯萎病",
    "value": "根部和茎基部腐烂，上部枝叶逐渐枯萎"
  }
]
```
'''

# 尝试清洗并打印结果
extracted_data = extract_json(inputs)
# print(f'extracted_data: {extracted_data}')

# 示例输入
inputs = '''
content: 在JSON格式中，您的要求可以这样表示：
```json
{
  "疾病名称": "细菌性软腐病",
  "病原体类型": "细菌",
  "病虫害分类": ["细菌"],
  "危害部位": "果实、茎叶",
  "危害特征": {
    "症状表现": "果皮或茎叶组织软化腐败，有恶臭味",
    "受影响作物范围": "广泛影响茄科植物",
    "易感时期": "成熟期及收获后",
    "对产量的影响": "严重时可导致大量减产",
    "与其他疾病的区别": "与真菌引起的病变不同，无霉层形成"
  },
  "发病条件": {
    "环境因素": "高温高湿的环境最有利于细菌繁殖",
    "农艺管理": "灌溉不当、种植密度过高容易加剧病情",
    "机械损伤": "伤口利于细菌侵入",
    "寄主抵抗力": "植株抗病能力下降会加重感染",
    "土壤pH值": "过酸或过碱的土壤都可能促进细菌生长"
  },
  "发病周期": "夏季至秋季的高温季节最容易发生",
  "传染性": "强",
  "传播途径": [
    "雨水淋洗",
    "昆虫叮咬",
    "人为操作（如修剪）",
    "病株残余物污染工具",
    "种子带菌"
  ],
  "防治措施": [
    "合理密植，保持良好的通风透光",
    "适时浇水并避免积水",
    "及时清除病株并销毁",
    "定期轮作，减少土壤中的细菌数量",
    "使用抗病品种并加强田间监测"
  ]
}
```
由于您还要求以完整的中文进行解释，以下是上述JSON内容对应的详细说明：
### 疾病名称：细菌性软腐病
### 病原体类型：细菌
### 病虫害分类：细菌性病害
### 危害部位：果实、茎叶
### 危害特征：
#### 症状表现：西红柿的果皮或茎叶组织会出现软化, length: 821
'''

# 尝试清洗并打印结果
extracted_data = extract_json(inputs)
# print(f'extracted_data: {extracted_data}')