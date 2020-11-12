from time import sleep

from celery import Celery

celery=Celery('tasks', broker="amqp://localhost", backend="rpc://localhost")
#AMQP = Advanced messege queue protocol
#RPC=Remote Procedure Call


@celery.task
def sleep_test(duration):
    sleep(duration)
    return

@celery.task
def cel_add(a: int, b: int):
    return a+b

