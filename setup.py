#coding:utf-8
#package project

from setuptools import setup, find_packages

setup(
    name="xtc",
    version="1.0.0",

    author="potato_xie",
    author_email="potato_xie@163.com",

    #自动寻找带有 __init__.py 的文件夹
    packages=find_packages(exclude=["logs"]),

    install_requires = ['django==1.11.14'],
    description = "xtc web site system",

    #单独的一些py脚本,不是在某些模块中
    scripts = [ "manage.py", "settings.py",
               "uwsgi.py", "__ini__.py"],

    include_package_data=True,    # 启用清单文件MANIFEST.in
    exclude_package_date={'':['.gitignore']} ,

    #如果是正式的项目，还会有更多的信息（例如开源证书写在下面）
    url = "http://littlegenius.com.cn",
)


