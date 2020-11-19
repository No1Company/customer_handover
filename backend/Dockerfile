FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /usr/src/app

COPY . .
WORKDIR /usr/src/app/backend

EXPOSE 80
CMD venv/scripts/activate.ps1, python run.py
COPY . .