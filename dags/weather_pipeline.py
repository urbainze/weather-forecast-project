from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import pandas as pd



# Définir le DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'etl_pipeline',
    default_args=default_args,
    description='Simple ETL pipeline',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 11, 20),
    catchup=False,
) as dag:
    
    extract = PythonOperator(
        task_id='extract',
        python_callable=extract_data,
        provide_context=True,
    )

    transform = PythonOperator(
        task_id='transform',
        python_callable=transform_data,
        provide_context=True,
    )

    load = PythonOperator(
        task_id='load',
        python_callable=load_data,
        provide_context=True,
    )

    extract >> transform >> load