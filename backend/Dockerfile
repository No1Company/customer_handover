FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7


WORKDIR /usr/src/app
COPY . .

RUN pip install -r requirements.txt

COPY . .
WORKDIR /usr/src/app/backend

EXPOSE 80
ENTRYPOINT ["python"]
CMD run.py
COPY . .