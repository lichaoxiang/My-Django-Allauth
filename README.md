## My-Django-Allauth

&ensp;&ensp;django-allauth 是非常受欢迎的管理用户登录与注册的第三方 Django 安装包，django-allauth 集成了 local用户系统 和 social用户系统，其 social用户系统 可以挂载多个账户。


### 项目目录树

- 创建与配置 Django 项目
- 扩展用户模型，个人 URLs
- 增加邮箱验证功能
- 支持 Github 等第三方账号登录
- 美化 Django-Allauth 自定义模板文件

### 效果图

- 用户登录
![用户登录][38]

- 用户注册
![用户注册][39]

  [38]: http://p7kk8oo3f.bkt.clouddn.com/QQ20180831-220214@2x.png
  [39]: http://p7kk8oo3f.bkt.clouddn.com/QQ20180831-220428@2x.png
  
### 使用步骤 

- 克隆版本库至本地
```
git@github.com:lichaoxiang/My-Django-Allauth.git
```

- 安装依赖文件
```
pip install -r requirements.txt
```

- 创建 MySQL 数据库

- 修改配置文件(password)

- 生成数据库
```
python manage.py makemigrations
python manage.py migrate
```

### 参考资料 

<a href="https://django-allauth.readthedocs.io/en/latest/">https://django-allauth.readthedocs.io/en/latest/</a>
