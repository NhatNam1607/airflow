from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# Định nghĩa các tham số mặc định
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Khởi tạo DAG
with DAG(
    'hello_world_dag',
    default_args=default_args,
    description='Một DAG đơn giản để kiểm tra hệ thống',
    schedule='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:

    # Task 1: In ra câu chào
    t1 = BashOperator(
        task_id='print_hello',
        bash_command='echo "Hello World from Antigravity!"',
    )

    # Task 2: In ra ngày hiện tại
    t2 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    # Thiết lập thứ tự chạy
    t1 >> t2
