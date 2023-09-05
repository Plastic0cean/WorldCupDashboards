FROM python:3.10.11
COPY dataset/. dataset
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY db/. db
COPY source/. source
# RUN python source/DataImporting/files/run_data_import.py
WORKDIR "source"
CMD FLASK_APP=app python -m flask run --host=0.0.0.0