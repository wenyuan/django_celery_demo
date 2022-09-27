import os
from celery import Celery
from django.conf import settings

# 为 celery 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_demo.settings')

# 创建应用
app = Celery("django_celery_demo")
# 配置应用
app.config_from_object('django.conf:settings')
# 设置 app 自动加载任务
# 从已经安装的 app 中查找任务
app.autodiscover_tasks(settings.INSTALLED_APPS)
