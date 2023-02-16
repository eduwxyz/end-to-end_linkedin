from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime
from random import randint
from airflow.operators.bash import BashOperator
import sys

sys.path.append("/opt/airflow/dags/scripts")


with DAG(
    "my_dag", start_date=datetime(2021, 1, 1), schedule_interval="@daily", catchup=False
) as dag:
    download_data = PythonOperator(
        task_id="download_data",
        python_callable=start_scrapy,
    )
x
