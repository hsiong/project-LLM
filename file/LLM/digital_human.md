# 数字人常用技术

## 数字人建模与渲染

### 使用开源模型和资源

- **MetaHuman Creator（Unreal Engine）**：提供高质量的开源3D数字人模型，支持定制化生成角色，并自带高质量皮肤、头发和服装贴图。
- **BlenderKit**：Blender插件，包含丰富的3D模型库，可以直接调用进行修改和使用，简化建模流程。
- **MakeHuman**：一个开源工具，支持快速生成定制化的人体模型，提供导出到Blender等工具进一步修改的选项。

### 动作捕捉替代方案

- **Mixamo（Adobe）**：提供免费预训练动作库，适用于各种基础的身体动作，如走路、跑步、跳跃等，直接应用到模型中。
- **CMU Motion Capture Database**：提供丰富的开源动作捕捉数据，用户可以将这些数据应用于数字人，实现自然的肢体动作。
- **DeepMotion**：AI驱动的动作捕捉解决方案，通过视频生成3D角色的动作，减少对传统Mocap设备的依赖。

### 贴图与纹理处理

- **Texture Haven / Poliigon**：提供高清材质贴图，包括皮肤、衣物、头发等纹理，可直接用于3D模型的材质处理。
- **SkinGen（Character Creator）**：一个生成高质量皮肤纹理的工具，可无缝集成到现有数字人模型中，增强逼真度。

### 渲染与动画

- **Unity / Unreal Engine**：用于实时渲染和动画处理。内置对MetaHuman和Mixamo等资源的支持，可以快速导入并渲染高质量的数字人模型。
- **物理模拟**：通过Nvidia PhysX、Havok等引擎，处理衣服、头发等物理效果，使动画更加真实。

## 语音处理与情感识别

### ASR（Automatic Speech Recognition，自动语音识别）

- **Google Speech-to-Text / Microsoft Azure Speech**：商用API，提供高精度的语音识别功能，支持多语言和实时语音处理。
- **VAD（语音活动检测）**：结合VAD技术检测语音的起点和终点，优化语音识别性能，减少误识别。

### TTS（Text-to-Speech，语音合成）

- **Google Text-to-Speech / Microsoft Azure TTS**：商用API，能够快速实现高质量的语音合成，生成自然流畅的对话语音。
- **情感语音合成**：通过调整API中的参数，生成不同情感的语音输出，如喜悦、愤怒、忧郁等，增强数字人的情感表达。

### 情感语音识别（Speech Emotion Recognition, SER）

- **OpenSMILE / pyAudioAnalysis**：开源工具，用于识别语音中的情感特征，提取如基频、MFCC等情感相关参数。
- **情感反馈**：结合SER，数字人可以根据用户的情感状态作出相应的表情或声音调整，提升交互的情感化效果。

## 大语言模型（LLM）与垂直领域应用

### LLM在垂直领域的应用

- **GPT-4 / BERT微调**：使用预训练的GPT-4、BERT等模型，通过微调技术将模型应用到特定的垂直领域（如医疗、教育、客服等），为数字人提供专业知识支持。
- **RAG（Retrieval-Augmented Generation）**：结合大语言模型与领域知识库，确保生成的对话内容更加专业和准确，尤其在复杂问答中表现更加出色。

### 情感生成与理解

- **情感生成**：通过情感标注和自然语言生成模型（如GPT-4），根据用户输入的情感状态生成带有情感色彩的回复，让数字人在对话中表达情感反应。
- **情感分析**：使用Hugging Face的情感分析模型，检测用户文本中的情感，让数字人根据用户的情感状态调节语气和表达。

## 网络通信与实时交互

### WebRTC（实时音视频通信）

- **功能**：实现数字人与用户之间的实时音视频通信。WebRTC可以保证音视频的低延迟传输，适合虚拟会议、实时互动等场景。
- **STUN/TURN/ICE协议**：解决网络NAT穿透问题，确保不同网络环境下的音视频传输顺畅。使用STUN服务器快速发现对等端的公网地址。

### Socket通信

- **WebSocket / Socket.IO**：通过WebSocket或Socket.IO实现服务器与客户端的双向、实时数据传输，适合需要频繁互动的场景，如实时聊天、多人协作中的虚拟人互动。
- **应用场景**：实时数据交换和交互，WebSocket可以高效地支持用户和数字人的实时交互。

### SSE（Server-Sent Events）

- **功能**：服务器端可以主动推送数据到客户端，适用于单向更新的场景，如新闻推送、实时通知。
- **技术实现**：基于HTTP长连接的实现，SSE允许服务器不断推送事件到客户端，适合较为轻量化的实时消息传递。

### CDN与边缘计算

- **内容分发网络（CDN）**：通过全球部署的边缘节点，将内容缓存到用户最近的节点，减少网络延迟，提升用户体验。
- **边缘计算**：将计算任务分布到靠近用户的边缘节点，以减少响应时间，优化全球用户的实时交互。

## 前端呈现与用户交互

### Web前端渲染与交互

- **Three.js**：基于WebGL的开源JavaScript库，用于在浏览器中进行轻量级的3D数字人渲染。支持与数字人的实时交互，适合网页上的3D数字人展示。
- **React / Vue前端框架**：结合WebGL技术，使用React或Vue构建交互式Web界面，支持复杂的前端交互，如手势识别、表情控制等。

### 移动端与桌面端呈现

- **Flutter / React Native**：使用跨平台开发框架构建移动端和桌面端的数字人展示与交互，适合移动虚拟助手、虚拟主播等场景。
- **Native应用开发**：针对iOS和Android平台的原生开发工具，可以实现高效的移动端虚拟人应用，支持手势、语音等多种交互方式。

### AR/VR集成

- **AR.js / WebXR**：将数字人集成到增强现实或虚拟现实中，通过AR眼镜或VR头显设备实现沉浸式互动体验。用户可以在现实场景中看到虚拟人并与之互动。

### 多模态交互

- **手势识别与体感交互**：通过摄像头和体感设备，支持手势识别和体感控制，用户可以用手势指挥数字人做出相应的动作。
- **语音与表情同步**：通过语音合成与语音识别技术，实时控制数字人的语音与口型同步，提供更自然的交互体验。

# 解决方案 V1.0


## NLP(除LLM)

+ 语音识别（ASR）: 将用户的语音输入转换为文本
+ 语音合成（TTS）: 将生成的文本转化为语音输出



## LLM 大模型

+ 自然语言理解（NLU）: 理解用户的意图和语境
+ 自然语言生成（NLG）: 根据对话内容生成合适的回答
+ 对话管理（DM）: 关系抽取, 上下文管理, 上下文理解 (根据用户历史对话, 来动态生成答案)
+ 知识注入及 AI 幻觉: 将外部知识整合到大型语言模型, 即各类问答对以及文本材料的注入, 常用方法: 微调、COT、RAG、Diversity Threshold、后处理验证
+ 提示语工程: 通过提示语工程, 可以引导模型生成特定的输出; 并使输出可控
+ 多模态融合: 语音、图像、文本输入与输出
+ 唤醒: 关键词唤醒、事件驱动唤醒、



## 数字人

+ 数字人建模与渲染
+ 面部表情引擎
+ 口型同步（Lipsync）
+ 肢体动作生成
+ 数字人模型输出 (主流使用 webRTC)
+ 多路输出

