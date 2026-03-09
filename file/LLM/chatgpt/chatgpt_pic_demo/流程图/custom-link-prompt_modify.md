你是一个上市科技公司的软件架构师, 使用中文回答, 帮我完成如下html代码

+ 基于 GoJS html 来实现流程图

+ 请根据我给你技术方案文档相关模块下的技术实现方案, 自行分析该模块的建设重点, 请不要捏造

+ 不能遗漏功能, 并且需要扩展我的功能, 系统不是单向的系统, 有并行和闭环的功能

+ 内容需要使用中文

+ 使用让人舒服的颜色, 使用命名配色(例如 lightblue, pink...), 各流程节点需要使用不同的颜色(颜色不能重复), 且避免使用 lightyellow lightgoldenrod , 因为会和背景色重合,

+ 模型demo如下

  ```
  						const nodes = [
  
                  // 主链路2 - 第一层
                  { key: "确定育种目标", color: "lightblue", loc: { x: 600, y: 0 } },
                  { key: "育种任务发布", color: "lightgreen", loc: { x: 600, y: 0 } },
  
                  // 主链路3
                  { key: "育种任务成功", color: "lightgreen", loc: { x: 1200, y: 900 } },
                  { key: "育种任务失败", color: "lightcoral", loc: { x: 300, y: 0 } },
  
                  
              ];
              const links = [
                  { from: "水肥一体机", to: "土壤传感器", text: "数据反馈", }
              ];
  ```

+ from, to 要和 key 对应

+ 根据 from, to, 按照业务逻辑, 合理生成 text

+ 你只需要完成 nodes 和 links 这两部分, 无需完成整个 html 代码

+ 每个 主链路2 - 第一层 逐层链接, 且都会链接到 育种任务失败 节点; 只有 专利申请 连接到 育种任务成功

+ 根据上述要求, 改变 node 的 color 和 loc 的值 ( x 不变, 逐层递增 y 值 + 200), 并生成 links



