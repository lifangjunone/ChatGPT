#!/usr/bin/env python
# coding=utf-8
from common.extensions import celery


@celery.task()
def add_together(a, b):
    return 'The result is:', str(a + b)
