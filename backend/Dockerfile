FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY . /app
WORKDIR /usr/src/app

RUN pip install -r requirements.txt

EXPOSE 80
CMD python3 -m venv venv, venv\scripts\Activate.ps1, cd backend, python resetDB.py, python run.py
COPY . .