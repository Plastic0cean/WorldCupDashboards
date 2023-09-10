FROM python:3.10.11
COPY dataset/. dataset
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY db/. db
COPY source/. source
WORKDIR "source"
CMD gunicorn --bind 0.0.0.0:5000 app:app