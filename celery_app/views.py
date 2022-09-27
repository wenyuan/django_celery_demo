from django.http import HttpResponse
from celery.result import AsyncResult
from .tasks import my_task


def index(request):
    # 将 my_task 任务加入到 celery 队列中
    # 如果 my_task 函数有参数，可通过 delay() 传递
    # 例如 my_task.delay(10, 20)
    res = my_task.delay()
    result = AsyncResult(res.task_id)

    return HttpResponse(
        "<h1>服务器返回响应内容!</h1><h2>status: {0}</h2><h2>task_id: {1}</h2>"
        .format(result.status, result.task_id)
    )
