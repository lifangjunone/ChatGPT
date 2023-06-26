#!/usr/bin/env python
# coding=utf-8

from .chat_manage import chat_manage_bp
from .common import api_common_bp
from .backend import backend_manage_bp

# ------------------------------
# API配置
# ------------------------------

# 允许访问的API版本
VERSIONS_ALLOWED = ['chat_manage', 'api_common', 'backend_manage']

# API版本映射
API_VERSION_MAPPING = {
    'chat_manage': chat_manage_bp,
    'api_common': api_common_bp,
    'backend_manage': backend_manage_bp,
}

# 注册自定义蓝图
APP_BLUEPRINTS = [
    'common:common_bp',
]
