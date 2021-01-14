FROM python:3.7.9-alpine3.12

WORKDIR /usr/src
RUN pip install pymysql

COPY ./example.py ./

CMD ["python", "example.py"]