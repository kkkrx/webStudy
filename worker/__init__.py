"""
配置 celery 异步设置
使用语句：celery -A your_app_name worker --pool=solo -l info 启动 celery
"""


import os
from celery import Celery


# 设置环境变量， 加载 Django 的settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webStudy.settings")

# 创建 Celery Application
celery_app = Celery('webStudy')
celery_app.config_from_object('worker.config')
celery_app.autodiscover_tasks()


def callByWorker(func):
    """
    将任务在 Celery 中异步执行
    """
    task = celery_app.task(func)
    return task.delay

