from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow import DAG
from datetime import timedelta

default_args = {
    'owner': 'rbtmd1010',
    'depends_on_past': False,
    'email': ['rbtmd1010@gmail.com'],
    'email_on_failure': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'classroom',
    default_args=default_args,
    description='Automatically update problem and solution',
    schedule_interval=timedelta(hours=6),
    start_date=days_ago(2),
    tags=['example'],
)

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='parse_problem',
    bash_command='django-admin -s BJ && django-admin -s LC && django-admin -s KT',
    dag=dag,
)

t2 = BashOperator(
    task_id='sleep',
    depends_on_past=False,
    bash_command='django-admin -p "cs/embed/*/*.md" && django-admin -t prake -s BJ',
    dag=dag,
)

t1 >> t2

t1 >> [t2, t3]
