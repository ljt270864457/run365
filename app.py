#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/26 下午8:57
# @Author  : liujiatian
# @File    : app.py

from flask import Flask

from views.wechat import wechat

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.ProductConfig')
# 注册蓝图
app.register_blueprint(wechat)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9999)
