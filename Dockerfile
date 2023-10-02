FROM python:3.11
WORKDIR /code
COPY requirements.txt /code
RUN pip3 install -r requirements.txt
COPY . .
