#!/usr/bin/env python
# coding=utf-8

from flask_restful import Api
from flask import Blueprint
from ChatGPT.api.common.version import ApiVersion


api_common_bp = Blueprint('api_common', __name__)
api_common = Api(api_common_bp, catch_all_404s=True)


# 获取API版本
api_common.add_resource(ApiVersion, '/version')