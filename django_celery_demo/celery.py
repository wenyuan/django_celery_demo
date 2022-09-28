import os
from celery import Celery
from django.conf import settings

# 为 celery 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_demo.settings')

# 创建应用
app = Celery("django_celery_demo")
# 配置应用
# namespace 表示所有与 celery 相关的配置键都有一个 CELERY_ 的前缀
app.config_from_object('django.conf:settings', namespace='CELERY')
# 从已经安装的 app 中加载任务模块
app.autodiscover_tasks()
