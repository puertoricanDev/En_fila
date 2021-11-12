# Guide for developers

## This guide is for running development server.

### Requirements:

    1. Install python and pip: 
        1. [https://realpython.com/installing-python/](Python)
        2. [https://phoenixnap.com/kb/install-pip-windows](pip)
    2. Clone repo from Github.
    3. Open in VS code.
    4. change directory:
        - ` cd en-fila`
    5. Install requirements:
        - `pip install -r requirements.txt`
    6. Install docker:
        - [https://docs.docker.com/desktop/windows/install/](Docker)
    7. Deploy needed docker container:
        - First time in vs code terminal run:
           - `docker run -p 6379:6379 -d redis:5`
        - After that just turn on redis container before starting server:
    8. Run Django server:
        - `python manage.py runserver`



