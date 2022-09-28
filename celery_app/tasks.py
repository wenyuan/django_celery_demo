from django_celery_demo.celery import app
import time


# 加上 app 对象的 task 装饰器
# 此函数为任务函数
@app.task
def my_task():
    print("任务开始执行....")
    time.sleep(5)
    print("任务执行结束....")


# 用于定时执行的任务
@app.task(bind=True)
def interval_task(self, *args, **kwargs):
    task_context = self.request.__dict__
    desc = args[0] if args else ''
    print('task name: {0}, desc: {1}'.format(
        task_context['properties']['periodic_task_name'], desc)
    )


# 用于定时执行的任务
@app.task(bind=True)
def crontab_task(self, *args, **kwargs):
    task_context = self.request.__dict__
    desc = args[0] if args else ''
    print('task name: {0}, desc: {1}'.format(
        task_context['properties']['periodic_task_name'], desc)
    )
