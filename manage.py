#!/usr/bin/env python
# coding=utf-8

import os

from flask_migrate import MigrateCommand
from flask_script import Manager, Shell, Server
from common.extensions import celery
from ChatGPT import create_app, db, init_celery
from conf.default import BaseConfig

app = create_app(os.getenv('ENVIRONMENT', BaseConfig.ENV))
init_celery(app, celery)


def make_shell_context():
    return dict(app=app)


manager = Manager(app)

# 命令行工具
manager.add_command('shell', Shell(make_context=make_shell_context))
# 操作数据库迁移
manager.add_command('db', MigrateCommand)
# 添加管理命令
manager.add_command('runserver', Server(host=app.config['SERVER_HOST'],
                                        port=app.config['SERVER_PORT'],
                                        use_debugger=app.config['DEBUG'], use_reloader=app.config['USE_RELOADER']))


@manager.command
def create_db():
    db.create_all()


if __name__ == '__main__':
    manager.run()
