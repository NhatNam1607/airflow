FROM apache/airflow:3.1.8-python3.12

USER airflow

COPY requirements.txt /opt/airflow/requirements.txt
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt

COPY --chown=airflow:0 dags /opt/airflow/dags
RUN chmod -R 775 /opt/airflow/dags
