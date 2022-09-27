from django_celery_demo.celery import app
import time


# 加上 app 对象的 task 装饰器
# 此函数为任务函数
@app.task
def my_task():
    print("任务开始执行....")
    time.sleep(5)
    print("任务执行结束....")
