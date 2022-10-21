# Django 集成 Celery 使用案例

## 环境

> 本项目需要在 Linux 服务器上运行。

* Python 3.8.9
* Django 4.0.7
* Celery 5.2.7
* Redis 7

## 前置准备

* 本项目配套文档参考 [Django 与 Celery 的集成](https://www.fedbook.cn/backend-knowledge/django/django-integrating-celery/)
* 安装 Redis 参考 [Redis 的安装与卸载](https://www.fedbook.cn/basic-skills/redis/installation-of-redis/)
* 安装 Python 及虚拟环境参考 [Python 多版本虚拟环境共存](https://www.fedbook.cn/backend-knowledge/python/multiple-python-install-on-linux/)

## 运行代码

### 初始化项目

安装好依赖包后，进入 `django_celery_demo/` 目录下。

首先进行 Django 工程运行前的初始化工作：

```bash
python manage.py makemigrations
python manage.py migrate
```

接下来创建后台管理员帐号，后面可用于登录管理后台 Admin：

```bash
python manage.py createsuperuser
```

### 运行 Django 工程

执行以下命令：

```bash
python manage.py runserver
```

## 调用异步任务

### 启动 worker

执行以下命令：

```bash
# celery -A 你的工程名 worker -l info
celery -A django_celery_demo worker -l info
```

### 执行任务

执行一次异步任务，即打开浏览器访问：`ip:port/`。然后可以观察浏览器页面返回值和服务端 worker 的输出。

## 开启定时任务

### 配置定时任务

访问 `ip:port/admin/`，在 `PERIIOIC TASKS` 中先添加 `Crontabs` 或 `Intervals`，然后添加 `Periodic tasks`。

### 启动 beat

执行以下命令：

```bash
# celery -A 你的工程名 beat -l info
celery -A django_celery_demo beat -l info
```

接下来就可以在服务端等待并观察 worker 和 beat 的输出了。
