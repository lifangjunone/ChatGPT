#!/usr/bin/env python
# coding=utf-8

import os
from flask import Flask, request
# from flask_consulate import Consul
from flask_cors import CORS
from flask_migrate import Migrate
from werkzeug.utils import import_string

from common.log_handler import LogHandler
from common.utils import get_ip_address
from common.extensions import db, main_app_create_engine
from conf.default import config, BaseConfig
from conf import celeryconfig
from .api import VERSIONS_ALLOWED, API_VERSION_MAPPING, APP_BLUEPRINTS
from flask_jwt_extended import jwt_required
import logging
from datetime import datetime
import mysql.connector

_logger = logging.getLogger(__name__)

app_ = Flask(__name__)

TOKEN_ERROR_INFO = ['Signature verification failed', 'Invalid crypto padding', 'Token has expired',
                    'Missing Authorization Header']


def create_test_data():
    """
    insert test data
    :return:
    """
    with main_app_create_engine.connect() as con:
        con.execute('INSERT INTO user (username, age, sex,  is_delete, created_at)VALUES '
                    '("张三", 20, "男", 0, "2022-12-07 20:54:35")')


def init_celery(app, celery):
    """
    :param app:
    :param celery:
    :return:
    """
    celery.config_from_object(celeryconfig)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


def create_db():
    mydb = mysql.connector.connect(
        host=BaseConfig.MYSQL_HOST,  # 默认用主机名
        user=BaseConfig.MYSQL_USER,  # 默认用户名
        password=BaseConfig.REDIS_PASSWORD,  # mysql密码
        charset='utf8'  # 编码方式
    )
    cursor = mydb.cursor()
    sql = """create database if not exists {0} default character set utf8 collate utf8_general_ci;"""\
        .format(BaseConfig.MYSQL_DATABASE)
    print(sql)
    cursor.execute(sql)
    # 关闭数据库
    # db.close()


def create_app(config_name):
    """应用工厂方法

    :param config_name:
    :return: flask_app
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    _create_need_dir()
    _register_extensions(app)
    _register_blueprint(app)

    # Init SQLAlchemy and create table and test data
    if BaseConfig.ENV == 'testing':
        try:
            with app.app_context():
                db.init_app(app)
                create_db()
                db.create_all()
                create_test_data()
        except Exception as e:
            print(str(e))
            pass
    else:
        # 初始化SQLAlchemy
        db.init_app(app)

    # 非调试模式下执行
    if not app.debug:
        # 初始化日志处理
        LogHandler(app)
        _register_service_to_consul(app)
    return app


@jwt_required()
def _verify_token():
    pass


@app_.before_request
def before_request():
    """
    这个钩子会在每次客户端访问视图的时候执行
    # 可以在请求之前进行用户的身份识别，以及对于本次访问的用户权限等进行判断。..
    """
    if 'login' in request.base_url:
        pass
    elif 'version' in request.base_url:
        pass
    elif 'chat_manage' in request.base_url:
        pass
    else:
        _verify_token()
    pass


@app_.after_request
def after_request(response):
    """
    请求返回之前做一些事
    """
    # print("----after_request----")
    return response


def _create_need_dir():
    """
    创建需要用到的文件件
    """
    pass


def _get_url_prefix(version):
    """根据API版本返回URL路径前缀

    :param version: 版本号，字符型
    :return: str, url路径
    """
    return '/api/{0}'.format(str(version))


def _register_extensions(app):
    """注册扩展模块

    :param app:
    :return:
    """
    cors = CORS()
    migrate = Migrate()
    # 跨域请求设置
    cors.init_app(app, resources=app.config['CORS_RESOURCES'], supports_credentials=True)
    # compare_type默认为False,不检测字段数据变化
    migrate.init_app(app, db, compare_type=False)


def _register_blueprint(app):
    """注册不同类型的API蓝图：1.根据API版本；2.根据自定义API

    :param app: app_context
    :return: None
    """

    # 自动根据API版本注册蓝图
    for version in VERSIONS_ALLOWED:
        app.register_blueprint(
            API_VERSION_MAPPING[version], url_prefix=_get_url_prefix(version))

    # 自定义注册API蓝图
    for bp_name in APP_BLUEPRINTS:
        bp = import_string(bp_name)
        app.register_blueprint(bp)


def _register_service_to_consul(app):
    """将服务注册到Consul服务

    :param app: app_context
    :return: None
    """
    """
    host_ip = get_ip_address(app.config['HOST_ADAPTER'])
    consul = Consul(
        app=app,
        consul_host=app.config['CONSUL_SERVER_HOST'],
        consul_port=app.config['CONSUL_SERVER_PORT']
    )
    consul.apply_remote_config(
        namespace=app.config['CONSUL_NAMESPACE'])
    consul.register_service(
        address=host_ip,
        name=app.config['SERVICE_NAME'],
        interval=app.config['CONSUL_REGISTER_INTERVAL'],
        tags=app.config['CONSUL_REGISTER_TAGS'],
        port=app.config['SERVER_PORT'],
        httpcheck='http://{host}:{port}/healthcheck'.format(
            host=host_ip, port=app.config['SERVER_PORT'])
    )
    """

