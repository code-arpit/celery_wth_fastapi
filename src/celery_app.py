import time

from celery import Celery

celery = Celery(
    __name__,
)
celery.conf.broker_url = "redis://localhost:6379/0"
celery.conf.result_backend = "redis://localhost:6379/0"


@celery.task
def reverse(a: str):
    print("Original:", a)
    time.sleep(5)
    reverse = a[::-1]
    print("Reversed : ", reverse)

    return reverse
