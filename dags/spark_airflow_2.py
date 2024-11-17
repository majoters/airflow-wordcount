from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

dag = DAG(
    dag_id = "sparkingFlow",
    default_args = {
        "owner": "Supakorn",
        "start_date": days_ago(1)
    },
    schedule_interval = "@daily"
)

start = PythonOperator(
    task_id = "start",
    python_callable = lambda : print("Job Started"),
    dag = dag
)

python_job = SparkSubmitOperator(
    task_id = "python_job",
    conn_id = "spark-conn",
    application = "jobs/python/word_count_job.py",
    dag = dag
)

end = PythonOperator(
    task_id = "end",
    python_callable = lambda : print("Job Completed"),
    dag = dag
)

start >> python_job >> end
