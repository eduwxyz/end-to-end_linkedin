from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime
from random import randint
from airflow.operators.bash import BashOperator
from end_to_end_linkedin_scraping.end_to_end_linkedin.spiders.linkedin_jobs import (
    LinkedJobsSpider,
)

from scrapy.crawler import CrawlerProcess


def main():
    process = CrawlerProcess()
    process.crawl(LinkedJobsSpider)
    process.start()


with DAG(
    "my_dag", start_date=datetime(2021, 1, 1), schedule_interval="@daily", catchup=False
) as dag:
    download_data = PythonOperator(
        task_id="download_data",
        python_callable=main,
    )
x
