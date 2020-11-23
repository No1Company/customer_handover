FROM python:3

ARG ehr_pass

WORKDIR /usr/src/app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
WORKDIR /usr/src/app/backend

EXPOSE 80
CMD ["python", "run.py --port 80 --host 0.0.0.0 --ehrpassword ${ehr_pass}" ]
COPY . .
