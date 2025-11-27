html如下

```
<!DOCTYPE html>
<html lang="zh">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>系统架构图</title>
  <style>
    body {
font-family: 'Arial', sans-serif;
background-color: #FAF9DE;
color: #333;
display: flex;
flex-wrap: wrap;
justify-content: center;
padding: 20px;
}
.main-module {
border: 2px solid #333;
margin: 10px;
padding: 10px;
border-radius: 10px;
box-shadow: 2px 2px 5px #888888;
width: 300px;
position: relative;
min-height: 200px;
}
.module-title {
font-weight: bold;
color: #333;
margin-bottom: 5px;
}
.sub-module {
background: linear-gradient(to right, #d6dde3 0%, #fcfaf3 100%); /* 从左到右的渐变，从淡灰蓝到白 */
color: #2c3e50; /* 深蓝灰色，提供良好的可读性 */
margin: 5px;
padding: 5px;
border-radius: 8px;
box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.2); /* 恰当的阴影以增强视觉层次感 */
}
.main-module:nth-child(1) {
background-color: #E9EBFE;
}
.main-module:nth-child(2) {
background-color: #BFD7ED;
}
.main-module:nth-child(3) {
background-color: #A4D4AE;
}
.main-module:nth-child(4) {
background-color: #CBE4F9;
}
.main-module:nth-child(5) {
background-color: #FBE4E8;
}
.main-module:nth-child(6) {
background-color: #F9E4C8;
}

.centered-title {
text-align: center;
margin-top: 20px;
margin-bottom: 20px;
width: 100%; /* 确保标题占满整行 */
}
  </style>
</head>

<body>
<h1 class="centered-title">建设清单</h1>  <!-- 添加 class 以应用 CSS 样式 -->
<div class="main-module">
  <div class="module-title">父级1</div>
  <div class="sub-module">内容</div>
</div>

</body>

</html>
```

参考html, 生成以下功能的功能清单

```
xxxx
```

要求如下

+ 你需要根据我的模块功能设计, 形成系统模块架构图
+ 要美观, 不要使用svg, 你使用 bootstrap 等前端框架实现, 结合div等等实现
+ div的排版要美观, 可以使用层次布局/星形布局/环形布局/管道布局等等, 不需要使用连接线, 而是需要使用其他的div来区分各个父模块和子模块
+ 各div的宽度固定的, 实现自动化响应式布局; 体现包含关系
+ 不能通过定义规则来实现响应式页面, 因为你不可能为无限种样式定义规则
+ 父层的长度和宽度需包含子级
+ 同一行div长度应相同, 使用js或者自适应实现
+ 父层主色调使用让人舒服的颜色, 比如 #FAF9DE,  #E9EBFE, #DCE2F1 这种柔和的颜色, 各父模块要用不同的颜色; 
+ 内容需要使用中文
+ 不能遗漏我的任何一项要求
+ + `aim1`例如 体系 对应 `父级1`
+ 你需要添加样式, 来对应`aim2`例如管理系统这层模块代表所在的层级
+ `aim3`例如 控制模块 对应 内容
+ `aim2`的背景色与父级`aim1`一致, 但是边框需用实体边框做区别
+ 一共三层, `aim1`-> `aim2` -> `aim3`; 如果同一aim2, 则说明是aim3属于aim2, 需合并; 例如在`aim1`运营体系包含`aim2`微信小程序/Web管理后台, 而`aim2`微信小程序包含`aim3`温室管理/水肥管理等等;
+ 不能忽略`aim2`, 如果无, 则无需渲染本层
+ 不能忽略`aim3`, 如果无, 则无需渲染本层
+ 注意参照所给的html和css来生成, 仅加入`aim2`这块, 无需做过多修改
+ 不能遗漏我的任何一项要求
