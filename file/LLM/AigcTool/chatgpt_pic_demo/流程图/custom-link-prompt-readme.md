# 使用办法

```html
            const nodes = [
                { key: "小天气气象站", color: "lightblue", loc: { x: 100, y: 0 } },
                { key: "土壤传感器", color: "lightgreen", loc: { x: 300, y: 0 } },
                { key: "高分天气预报", color: "lightpink", loc: { x: 500, y: 0 } },
                { key: "土壤水肥分析模型", color: "lightcoral", loc: { x: 300, y: 200 } },
                { key: "AI Box", color: "lightseagreen", loc: { x: 100, y: 200 } },
                { key: "水肥一体机", color: "lightsteelblue", loc: { x: -100, y: 200 } },
                { key: "校正函数", color: "lightgoldenrodyellow", loc: { x: 300, y: 400 } }
            ];
```
+ key: node 名
+ color: node yanse
+ loc: node 坐标

```html
            const links = [
                { from: "小天气气象站", to: "土壤水肥分析模型", text: "数据传输", customPoints: [] },
                { from: "土壤传感器", to: "土壤水肥分析模型", text: "数据传输", customPoints: [] },
                { from: "高分天气预报", to: "土壤水肥分析模型", text: "数据传输", customPoints: [] },
                { from: "土壤水肥分析模型", to: "AI Box", text: "分析结果", customPoints: [] },
                { from: "AI Box", to: "水肥一体机", text: "控制信号", customPoints: [] },
                { from: "水肥一体机", to: "土壤传感器", text: "数据反馈", startEndPoints: [CoordinateType.UP, CoordinateType.UP], customPoints: [{ x: 100, y: 100 }, { x: 300, y: 100 }] },
                { from: "校正函数", to: "土壤水肥分析模型", text: "校正数据", customPoints: [] }
            ];
```
+ from: 起始node
+ to: 终止node
+ text: link描述
+ startEndPoints: 从 from/to node 出发的link线的位置; 如果只输入 startEndPoints, 那么只支持同时为 up/down 或者 right/left
+ customPoints: link 线需要经过的位置