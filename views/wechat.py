#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/26 下午10:24
# @Author  : liujiatian
# @File    : wechat.py

import requests
import json

from flask import Blueprint, request, jsonify
from flask import current_app as app

wechat = Blueprint('wechat', __name__)


@wechat.route('/wechat/login/', methods=['POST'])
def wechat_login():
    '''
    登录微信，获取open_id 和session_id
    返回 openid，session_key
    :return:
    '''
    body = json.loads(request.data)
    app_id = app.config['WECHAT_ID']
    secret = app.config['WECHAT_SECERET_KEY']
    js_code = body.get('login_code')

    url = 'https://api.weixin.qq.com/sns/jscode2session?appid={app_id}&secret={secret}&js_code={js_code}&grant_type=authorization_code'.format(
        app_id=app_id,
        secret=secret,
        js_code=js_code
    )
    r = requests.get(url)
    call_back = r.json()
    return jsonify(call_back)
