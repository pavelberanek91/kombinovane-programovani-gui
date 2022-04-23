#python3 -m pip install apache-airflow

from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.dummy_operator import DummyOperator

with DAG(
    "etl_sales_daily",
    start_date=days_ago(1),
    schedule_interval=None,
) as dag:
    task_a = DummyOperator(task_id="task_a")
    task_b = DummyOperator(task_id="task_b")
    task_c = DummyOperator(task_id="task_c")
    task_d = DummyOperator(task_id="task_d")
    task_a >> [task_b, task_c]                  #a je upstraam pro downstreamy b,c (nejdriv a, pak b,c)
    task_c >> task_d