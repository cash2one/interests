### 重要提示
1、适用项目
```
project_demo
├── bin                                    # 项目安装部署脚本
│   └── install-ctl
├── etc                                    # 项目所有的配置都从这里配置，包括django的settings.py配置
│   ├── config.yaml
│   └── config.yaml.template
├── project_demo                           # 名称与顶层目录一致
│   ├── apps                               # 用来扩展之后的app代码
│   │   └── app_demo           
│   │       ├── for_mock.py
│   │       ├── models.py
│   │       ├── urls.py
│   │       └── views.py
│   ├── manage.py
│   ├── settings                           # django的settings文件
│   │   ├── base.py                        # 基础配置（一般不修改）
│   │   ├── develop.py.template            # develop.py.template为开发者配置，开发者需要拷贝一份模板文件进行配置
│   │   ├── product.py                     # product为生产配置（一般不修改）
│   │   └── test.py                        # UT配置（一般不修改）
│   ├── templates                          # 前端模板文件
│   │   ├── apps                           # 模板根据apps里面的app分开存放
│   │   │   └── app_demo
│   │   ├── includes                       # app可能会引用的，如ajax动态生成的或者公共的模板提取
│   │   │   └── model_for_app_demo.html
│   │   └── index.html
│   ├── tests                              # 用于存放单元测试的目录
│   │   └── app_demo                       # 根据apps目录分开
│   │       ├── test_mock.py
│   │       └── test_views.py
│   ├── urls.py
│   ├── utils                              # 存放公共方法或者类
│   │   ├── config.py                      # 项目统一配置入口
│   │   ├── exception.py
│   │   ├── singleton.py
│   │   └── thirdparty
│   └── wsgi.py
├── README.md
└── site-packages                          # 项目依赖第三方包，开发人员需要在requirementss.ini中注明类型和版本
    └── requirements.ini                   
```
2、安装路径及配置
```
python3.4安装路径：/usr/local/py34
nginx安装路径：/usr/local/nginx
nginx配置文件夹： /etc/nginx/conf.d
surpervisor安装路径：系统pip2对应的site-packages
supervisor配置文件夹：/etc/supervisor.d/
```
3、日志文件路径
```
uwsgi日志：{project_dir}/var/log/7lk.{project_name}.log
supervisor日志：/var/log/7lk.supervisord.log 
```

### 一、命令说明
```
Usage:
        sh install-ctl <command> [option]
Command:
        install
Option:
        --all
        --with-conf-env
        --with-mysql-db
        --with-conf-file
        --with-sys-env
        --with-py34
        --with-web-env
        --with-supervisor
        --with-py-extra
        --with-djdb
        --with-start-services
        --update-local
        --update-remote
Comments:
Command:
        install                  安装
Option:
        --all                    安装全部模块
        --with-conf-env          配置环境变量
        --with-mysql-db          初始化数据库
        --with-conf-file         初始化配置文件
        --with-sys-env           安装系统依赖的软件
        --with-py34              安装python3
        --with-web-env           安装web服务依赖软件
        --with-supervisor        安装supervisor
        --with-py-extra          安装python项目第三方包
        --with-djdb              初始化django数据库
        --with-start-services    开始所有的服务
        --with-update-local      更新本地代码(update)
        --with-update-remote     打包本地代码(update)
```

### 二、开发者使用
1、执行以下命令就可以安装所有的依赖包自动部署
```
sh install-ctl install --all
```
