import sys
import os

import pendulum

from airflow.decorators import task
from airflow import DAG

# Define the absolute path to the scripts directory
scripts_path = os.path.abspath('/opt/airflow/scripts')

# Add the scripts directory to sys.path
sys.path.append(scripts_path)

from collect_data import collect_all
from exchanges.binance import BinanceClient

DAG_ID = "financial_data_processing_dag"

with DAG(
    dag_id=DAG_ID,
    start_date=pendulum.datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:
    
    @task(task_id="collect_store_raw_data")
    def collect_store_raw_data():
        """Collect data from broker in store raw data into HDF5 database"""
        client = BinanceClient()

        collect_all(client, "Binance", "BTCUSDT")

        print("why")

    @task(task_id="process_raw_data")
    def process_raw_data():
        """Process raw data by ... ... """
        pass

    @task(task_id="create_visualization")
    def create_visualization():
        """Create visualization to show ..."""
        pass

    collect_store_raw_data() >> process_raw_data() >> create_visualization()