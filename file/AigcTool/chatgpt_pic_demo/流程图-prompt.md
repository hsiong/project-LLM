+ 你是一个上市科技公司的软件架构师, 使用中文回答, 帮我完成如下html代码

  + 基于 GoJS html 来实现流程图 

  + 请根据我给你技术方案文档相关模块下的技术实现方案, 自行分析该模块的建设重点, 请不要捏造

  + 不能遗漏功能, 并且需要扩展我的功能, 系统不是单向的系统, 有并行和闭环的功能

  + 内容需要使用中文

  + 使用让人舒服的颜色, 使用命名配色(例如 lightblue, pink...), 各流程节点需要使用不同的颜色, 且避免使用 lightyellow lightgoldenrod , 因为会和背景色重合, 

  + 不同层各node的y间距为200; 同一层各node的x间距为200

  + 流程图整体方向是从上到下, 方向为纵向, 图标和link不能重合(x 肯定是不一致的)

  + 模型demo如下

    ```
    						const nodes = [
    
                    { key: "水肥一体机", color: "lightblue", loc: { x: 100, y: 0 } },
                    { key: "土壤传感器", color: "lightgreen", loc: { x: 600, y: 200 } }
                    
                ];
                const links = [
                    { from: "水肥一体机", to: "土壤传感器", text: "数据反馈", }
                ];
    ```

  + from, to 要和 key 对应

  + 你只需要完成 nodes 和 links 这两部分, 无需完成整个 html 代码

  + 总体架构如下: 
  ```
  xxxx
  ```
