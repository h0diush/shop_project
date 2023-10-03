FROM python:3.11
WORKDIR /code
COPY requirements.txt /code
RUN pip3 install -r requirements.txt
COPY . .
CMD gunicorn your_app_name.wsgi:application --bind 0.0.0.0:8000
