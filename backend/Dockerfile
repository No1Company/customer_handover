FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /usr/src/app

COPY . .
WORKDIR /usr/src/app/backend
RUN pip install -r requirements.txt

EXPOSE 80
ENTRYPOINT ["python"]
CMD run.py
COPY . .