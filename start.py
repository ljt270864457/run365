#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/26 下午9:24
# @Author  : liujiatian
# @File    : start.py

import os
import sys

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_DIR = os.path.join(PROJECT_DIR, 'config')


def lazy_config(env):
    if env not in ['default', 'development', 'production', 'staging']:
        raise BaseException('config not found')

    config_path = os.path.join(CONFIG_DIR, '.'.join([env, 'py']))
    os.environ.setdefault('APP_CONFIG_FILE', config_path)


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        print 'load default env'
        env = 'default'
    else:
        env = args[1]
    lazy_config(env)
    shell = 'cd {project_dir};python app.py'.format(project_dir=PROJECT_DIR)
    os.system(shell)
