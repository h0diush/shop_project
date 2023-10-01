FROM python:3.11
WORKDIR /code
COPY requirements.txt /code
RUN pip3 install -r requirements.txt
COPY . .
CMD python3 manage.py runserver 0.0.0.0:8000
