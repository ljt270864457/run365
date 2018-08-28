#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 下午7:41
# @Author  : liujiatian
# @File    : config123.py

class BaseConfig(object):
    SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'

    WECHAT_ID = 'd178ad5d932bedd92f13aaca3b785a42'
    WECHAT_SECERET_KEY = 'd178ad5d932bedd92f13aaca3b785a42'


class DevConfig(BaseConfig):
    '''
    开发环境
    '''
    pass


class StagingConfig(BaseConfig):
    '''
    测试环境
    '''
    pass


class ProductConfig(BaseConfig):
    '''
    正式环境
    '''
    pass
