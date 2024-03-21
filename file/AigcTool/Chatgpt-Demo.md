# API-Doc
已知
+ 测试环境
+ 接口地址
+ 接口名为
+ 接口请求方式
+ 入参如下
```java
        @ApiModelProperty(value = "sn码")
        @NotBlank(message = "sn码不能为空！")
        private String sn;

        @ApiModelProperty(value = "用户unionId")
        @NotBlank(message = "用户unionId不能为空！")
        private String unionId;
```
+ 返回结构如下
```java
    private int code;
    private String message;
    private T data;
    private Boolean success;
```
	+ 操作成功  success true && code 200
	+ 出现异常 success false && code 100
+ 异常情况如下
    + 参数验证 xxx 不能为空!
    + sn解绑失败: 用户不存在！param: %入参
    + sn解绑失败: 绑定显卡信息不存在！param: %入参

帮我完成一份接口文档
