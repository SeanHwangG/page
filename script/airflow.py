from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {'owner': 'rbtmd1010',
                'depends_on_past': False,
                'email': ['rbtmd1010@gmail.com'],
                'email_on_failure': True,
                'retries': 1,
                'retry_delay': timedelta(minutes=5)}

dag = DAG('classroom',
          default_args=default_args,
          description='Automatically update problem and solution',
          schedule_interval=timedelta(hours=6),
          start_date=days_ago(2),
          tags=['example'])

# Fetch problem
# da crawl_problems -s BJ
# da crawl_problems -s CF
# da crawl_problems -s CC
# da crawl_problems -s LC
# da crawl_problems -s KT

# Read Solution
# da read_solutions -u rbtmd1010@gmail.com -t * -tt

# Deploy
# da combine_problems -u rbtmd1010@gmail.com -tt "problem/*" -t "*" -r embed

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(task_id='parse_problem',
                  bash_command='django-admin -s BJ && django-admin -s LC && django-admin -s KT',
                  dag=dag)

t2 = BashOperator(task_id='sleep',
                  depends_on_past=False,
                  bash_command='django-admin -p "cs/embed/*/*.md" && django-admin -t prake -s BJ',
                  dag=dag)

t1 >> t2

t1 >> [t2, t3]
