from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from utils.extract import extract_data
from utils.transform import transform_data
from utils.load import load_data_to_postgres
from datetime import datetime, timedelta
import requests
import pandas as pd



# we specify the dags arguments
default_args = {
    'owner': 'Urbain ZE',
    'start_date': days_ago(0),
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

# we define the dag architecture 
dag = DAG(
    'weather-forecast-dag',
    default_args = default_args,
    description = 'this DAG aims to extract data from open meteo with and api , transform them and display a visualisation',
    schedule_interval = timedelta(hours = 1)
)

# now we define the tasks
#**********************************************************************************************************
# task to extract the data 
execute_extract = PythonOperator(
    task_id = 'extract',
    python_callable = extract_data,
    dag = dag
)

# task to transform the data 

execute_transform = PythonOperator(
    task_id = 'transform',
    python_callable = transform_data,
    dag = dag
)

# task for loading the data to the database

execute_load = PythonOperator(
    task_id = 'load',
    python_callable = load_data_to_postgres,
    dag = dag
)

#******************************************************************************************************

# here we define the task dependencies

execute_extract >> execute_transform >> execute_load