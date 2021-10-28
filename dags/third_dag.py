from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

our_third_dag = DAG(
    "third_dag",
    start_date=days_ago(0, 0, 0, 0, 0)
)

operation_1 = DockerOperator(
    task_id='docker_command',
    image='centos:latest',
    command="/bin/sleep 30",
    dag=our_third_dag
)

operation_1
