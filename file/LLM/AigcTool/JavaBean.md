
生成 JavaDTO

1. 使用 @ApiModelProperty(value = "字段注释")
2. 必填的使用 required=true 明确; 实体用@Notnull, String 用 @Notblank
3. 长度用 @Size(max = …; min..), 以及其他限制用注解实现
3. 内部类使用 成员内部类
4. 类注释不需要 @ApiModel("类说明") 而是使用注释