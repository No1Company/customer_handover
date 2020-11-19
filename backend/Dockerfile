FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /usr/src/app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 80
CMD "python3 -m venv venv", "source venv/bin/activate", "cd backend", "python resetDB.py", "python run.py"
COPY . .