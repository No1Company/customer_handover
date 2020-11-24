FROM python:3

ARG ehr
ENV ehr_pass = ${ehr}
WORKDIR /usr/src/app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80
RUN echo "chk ${ehr}"
CMD ["sh", "-c", "python ./run.py --port 80 --host 0.0.0.0"]
COPY . .
