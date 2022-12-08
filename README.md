## ACTIVATING VIRTUAL ENV
### $ source celery_venv/bin/activate

## INSTALLING REQUIREMENTS
### $ pip install -r requirements.txt

## RUNNING FASTAPI PROGRAM
### $ uvicorn main:app --reload

## FOR CELERY WORKER LOGS AND SPECIFYING LOG LEVEL
### $ celery -A celery_app.celery worker --loglevel=debug

## FOR CELERY FLOWER
### $ celery -A main.celery flower --port=5555

## FOR ACTIVATING REDIS SERVER
### $ brew services start redis && redis-server


## WITH DOCKER
### BUILDING THE CONTAINERS
### $ docker compose build

### RUNNING THE CONTAINERS IN DETACHED MODE
### $ docker compose up -d

### CHECKING THE LOGS FOR CONTAINER
### $ docker compose logs -f {container-name}
