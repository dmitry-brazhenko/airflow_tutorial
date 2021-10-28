import os

import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

our_first_dag = DAG(
    "second_dag",
    description='Python DAG example',
    schedule_interval="* * * * *",
    start_date=days_ago(0, 0, 0, 0, 0),
    tags=['python'],
    doc_md='*Python DAG doc* :)'
)


def download_titanic_dataset():
    df = pd.read_csv("https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv")
    df.to_csv("df.csv")


download_dataframe = PythonOperator(
    task_id='download_titanic_dataset',
    python_callable=download_titanic_dataset,
    dag=our_first_dag
)


def transform_titanic_dataset():
    df = pd.read_csv("df.csv")
    del df['Unnamed: 0']
    gr = df.groupby("Pclass").agg({"Survived": "mean"})
    gr.to_csv("output.csv")

    from airflow.models import Variable
    value = Variable.get("var")
    print("our value:", value)


transform_dataframe = PythonOperator(
    task_id='transform_dataset',
    python_callable=transform_titanic_dataset,
    dag=our_first_dag
)

# change working directory to /
# You should not use it in production

os.chdir("/")

download_dataframe >> transform_dataframe
