FROM python:3


WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
WORKDIR /usr/src/app/backend

EXPOSE 80
ENTRYPOINT [ "python" ]
CMD resetDBtest.py, run.py
COPY . .
