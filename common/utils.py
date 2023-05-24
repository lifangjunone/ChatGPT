#!/usr/bin/env python
# coding=utf-8

# 通用工具方法

import smtplib
from email.mime.text import MIMEText

import arrow

DATE_FMT = "YYYY-MM-DD HH:mm:ss"
TIME_ZONE = 'Asia/Shanghai'


def get_local_utc():
    return arrow.utcnow().to('local')


def get_datetime():
    """
    获取当前的时间，按照标准时间格式输出
    :return: 
    """
    return arrow.now().format(DATE_FMT)


def red(words):
    return "\033[31m\033[49m%s\033[0m" % words


def get_ip_address(ifname):
    """
    获取当前服务运行主机的IP
    Args:
        ifname: 网卡适配器名称

    Returns: ip地址

    """
    import socket
    import fcntl
    import struct

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,
            struct.pack('256s', ifname[:15].encode('utf-8'))
        )[20:24])
    except Exception:
        return "127.0.0.1"


def send_mail(from_addr, mailto_list, mail_sub, mail_content, mail_host, mail_user, mail_pass, mail_port=0,
              mail_ssl=False, mail_tls=True):
    """
    发送邮件

    :param from_addr:发件人
    :param mailto_list: 收件人列表
    :param mail_sub: 邮件主题
    :param mail_content: 邮件内容
    :param mail_host: 邮件主机
    :param mail_user: 用户名
    :param mail_pass: 密码
    :param mail_port: 主机端口
    :param mail_ssl: 启用SSL安全连接
    :param mail_tls: 启用TLS安全连接
    :return: 成功/失败
    """

    # 这里的displayName可以任意设置，收到信后，将按照设置显示
    # me = "displayName" + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(mail_content, _subtype='html', _charset='utf-8')
    msg['Subject'] = mail_sub
    msg['From'] = from_addr
    msg['To'] = ";".join(mailto_list)
    try:
        if mail_ssl:
            s = smtplib.SMTP_SSL()
        else:
            s = smtplib.SMTP()
        s.set_debuglevel(1)
        s.connect(mail_host, mail_port)
        if mail_tls:
            s.starttls()
        s.login(mail_user, mail_pass)  # 登陆服务器
        s.sendmail(from_addr, mailto_list, msg.as_string())
        s.close()
        return True
    except Exception as e:
        print(e)
        return False
