# FOR CELERY WORKER LOGS AND SPECIFYING LOG LEVEL
# celery -A celery_app.celery worker --loglevel=debug

# FOR CELERY FLOWER
# celery -A main.celery flower --port=5555

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
