import time

from fastapi import FastAPI

from celery_app import reverse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/celery/reverse")
async def celery_task(name_to_reverse: str):
    task = reverse.delay(name_to_reverse)
    print(type(task))

    new_state = task.state
    print(new_state, new_state != "PENDING")
    while new_state == "PENDING":
        print(task.state, task.result)
        time.sleep(0.25)
        new_state = task.state

    return {
        "status": task.state,
        "result": task.result,
    }
