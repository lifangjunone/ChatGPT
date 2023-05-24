#!/usr/bin/env python
# coding=utf-8
"""Application configuration.

Most configuration is set via environment variables.

For prod environment, use consul-k/v
to set environment variables.
"""
import os
from common.utils import get_ip_address

_basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    # ------------------------------
    # 全局通用配置
    # ------------------------------

    PROD_NAME = 'ChatGPT'
    SERVICE_NAME = 'ChatGPT'
    CURRENT_VERSION = 'v0.0.1'
    # *需手动配置生成秘钥 os.urandom(24)
    SECRET_KEY = '\xbb2\xe1\x0cL\xbd\xb6\x9a\xf2iZ\xb6O\xed\x97\x97l3ZyN\x94N\xc3'
    # 跨域设置
    CORS_RESOURCES = {r"/api/*": {"origins": "*"}}
    CSRF_ENABLED = True
    # 运行环境
    ENV = os.getenv('ENVIRONMENT', 'development')

    # ------------------------------
    # 服务器配置
    # ------------------------------
    HOST_ADAPTER = os.getenv('HOST_ADAPTER', 'eth0')
    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 8000
    USE_RELOADER = False

    # ------------------------------
    # 日志配置 默认值：INFO
    # ------------------------------
    """
        CRITICAL = 50
        ERROR = 40
        WARNING = 30
        INFO = 20
        DEBUG = 10
        NOTSET = 0
    """
    GLOBAL_LOGLEVEL = 20

    # 日志文件存储路径
    LOG_DIR_PREFIX = _basedir + '/../logs/'
    # 日志文件命名
    LOG_FILE = LOG_DIR_PREFIX + SERVICE_NAME + '.log'

    # ------------------------------
    # E-mail配置
    # ------------------------------
    MAIL_SERVER = 'lifj@ebondhm.com'
    MAIL_PORT = 568
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'lifj@ebondhm.com'
    MAIL_PASSWORD = 'your-password'

    # ------------------------------
    # OpenAI配置
    # ------------------------------
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    NET_CARD = os.getenv("NET_CARD", 'ens33')
    ORG_NAME = os.getenv("ORG_NAME", '')
    HOST_IP = get_ip_address(NET_CARD)
    PROXY_PROT = os.getenv("PROXY_PROT", 7890)

    # ------------------------------
    # Redis配置
    # ------------------------------
    REDIS_HOST = os.getenv("REDIS_HOST", '127.0.0.1')
    REDIS_PORT = os.getenv("REDIS_PORT", 6379)
    REDIS_DB = os.getenv("REDIS_DB", 5)
    REDIS_DB_CELERY_RESULT = os.getenv("REDIS_DB", 9)
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "123456")

    # ------------------------------
    # Celery配置
    # ------------------------------
    if REDIS_PASSWORD:
        BROKER_URL = 'redis://:' + REDIS_PASSWORD + '@' + REDIS_HOST + ':' + str(REDIS_PORT) + '/' + str(REDIS_DB)
        RESULT_BACKEND = 'redis://:' + REDIS_PASSWORD + '@' + REDIS_HOST + ':' + str(REDIS_PORT) + '/' + \
                         str(REDIS_DB_CELERY_RESULT)
    else:
        BROKER_URL = 'redis://' + REDIS_HOST + ':' + str(REDIS_PORT) + '/' + str(REDIS_DB)
        RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + str(REDIS_PORT) + '/' + str(REDIS_DB_CELERY_RESULT)

    # Mysql配置
    # ------------------------------
    MYSQL_HOST = os.getenv("MYSQL_HOST", "127.0.0.1")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "123456")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", 'chatgpt')
    MYSQL_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT,
                                                        MYSQL_DATABASE)

    # ------------------------------
    # MINIO 相关配置
    # ------------------------------
    MinIO_IP_PORT = os.getenv("MinIO_IP_PORT", "127.0.0.1:9000")
    MinIO_ACCESS_KEY = os.getenv("MinIO_ACCESS_KEY", "")
    MinIO_SECRET_KEY = os.getenv("MinIO_SECRET_KEY", "")
    MinIO_SECURE = os.getenv("MinIO_SECURE", False)
    BUCKET_NAME = os.getenv("BUCKET_NAME", 'test')

    # ------------------------------
    # JWT配置
    # ------------------------------
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-key'
    JWT_COOKIE_CSRF_PROTECT = True
    JWT_CSRF_CHECK_FORM = True
    JWT_ACCESS_TOKEN_EXPIRES = os.environ.get('JWT_ACCESS_TOKEN_EXPIRES') or 36000
    PROPAGATE_EXCEPTIONS = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    # ------------------------------
    # 数据库连接配置
    # ------------------------------
    # SQLALCHEMY_DATABASE_URI = 'postgresql://root:password@localhost/myapp'
    SQLALCHEMY_DATABASE_URI = BaseConfig.MYSQL_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    # ------------------------------
    # 数据库连接配置
    # ------------------------------
    SQLALCHEMY_DATABASE_URI = BaseConfig.MYSQL_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    # ------------------------------
    # 数据库连接配置
    # ------------------------------
    SQLALCHEMY_DATABASE_URI = BaseConfig.MYSQL_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
