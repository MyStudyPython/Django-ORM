# study_django
慕课网 学习全面掌握Django ORM 和  Django REST framework前后端分离框架

# 开发环境
- 前端 ：HTML/CSS + JQuery v3.7
- Django v4.2.3
- Python v3.11.3
- MySQL 8.0.33

[Django ORM 可查看相关资料](https://www.lmlphp.com/user/57927/article/item/1403116/)

# DRF 是drf_tutorial 文件夹
# ORM 是整个项目

# 重新启动项目遇到的问题
## 问题一
```sh
error: subprocess-exited-with-error

  × Getting requirements to build wheel did not run successfully.
  │ exit code: 1
  ╰─> [25 lines of output]
     
     
      You need Cython to compile Pyjnius.
     
      ...
      ModuleNotFoundError: No module named 'Cython'
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: subprocess-exited-with-error

× Getting requirements to build wheel did not run successfully.
│ exit code: 1
╰─> See above for output.
```
### 问题解决
需要单独pip安装一下Cython


