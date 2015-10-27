##### 备注：

1、所有的ini, yaml, conf结尾的文件都已经被过滤掉，如果有新配置增加，需要同步到template文件提交

2、执行以下命令，可以自动拷贝etc中的nginx、uwsgi、supervisor模板配置
```
bash install-ctl format_config
```