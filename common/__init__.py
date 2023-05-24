#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint
from flask_restful import Api

from common.healthcheck import HealthCheck

common_bp = Blueprint('common', __name__)

common_api = Api(common_bp, catch_all_404s=True)

# 服务健康检测
common_api.add_resource(HealthCheck, '/healthcheck')
