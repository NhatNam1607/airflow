from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

# Khởi tạo DAG đơn giản
with DAG(
    dag_id='sample_test_dag',
    schedule='@daily',        # Chạy hàng ngày
    start_date=datetime(2024, 1, 1),
    catchup=False,            # Không chạy bù các ngày trong quá khứ
    tags=['test'],
) as dag:

    # Task 1: Thông báo bắt đầu
    start_task = BashOperator(
        task_id='start_message',
        bash_command='echo "Airflow 3 is running perfectly!"'
    )

    # Task 2: Kiểm tra thư mục dags
    check_dir_task = BashOperator(
        task_id='check_dags_folder',
        bash_command='ls -l /opt/airflow/dags'
    )

    # Thứ tự chạy: start_task xong mới đến check_dir_task
    start_task >> check_dir_task
