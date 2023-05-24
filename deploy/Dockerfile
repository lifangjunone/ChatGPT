# Microservice skeleton
# VERSION 1.0.0
# MAINTAINER lifangjun <lifj@ebondhm.com>

FROM harbor.ebondhm.com/library/ipid:v1.0.1

ENV LANG=C.UTF-8
WORKDIR /usr/src/backend
COPY . .
RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir \
    && pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt \
    && chmod +x ./deploy/docker-entrypoint.sh
