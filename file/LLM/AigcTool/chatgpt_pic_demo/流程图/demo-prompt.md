+ 你是一个上市科技公司的软件架构师, 使用中文回答, 帮我完成如下html代码

  + 基于 GoJS html代码来实现农场管理模块的流程图 

  + 请根据我给你技术方案文档相关模块下的技术实现方案, 自行分析该模块的建设重点, 请不要捏造
  
  + 不能遗漏功能, 并且需要扩展我的功能, 系统不是单向的系统, 有并行和闭环的功能
  
  + 内容需要使用中文
  
  + 使用让人舒服的颜色, 使用命名配色(例如 lightblue, pink...), 各流程节点需要使用不同的颜色, 且避免使用 lightYellow lightgoldenrod , 因为会和背景色重合, 
  
  + 模型demo如下
  
    ```
                // 设置模型数据
                var model = $(go.GraphLinksModel);
                model.nodeDataArray = [
                    { key: "1", name: "环控数据采集", color: "lightblue" },
                    { key: "2", name: "监控数据采集", color: "lightgreen" }
                ];
                model.linkDataArray = [
                    { from: "1", to: "2", text: "数据输入" }
                ];
    ```
  
  + 你只需要完成 model.nodeDataArray 和 model.linkDataArray , 一起给我
  
  
