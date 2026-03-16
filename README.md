# Apache Airflow Template Project

<img alt="airflow logo" src="https://upload.wikimedia.org/wikipedia/commons/d/de/AirflowLogo.png" width="40%" height="auto">

## Introduction
Airflow is a Python-based workflow management tool for data engineering pipelines.
It simplifies the development, deployment, and monitoring of data pipelines by using
DAGs. Visit [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/index.html) for more information.

This project template uses **Apache Airflow 3.1.8** with Docker Compose for local
development and deployment.

## Requirements

- Docker & Docker Compose
- (Optional) Python 3.12+ for local development

## Project Structure

```
.env.example              # Environment variable template
.env                      # Your local environment variables (git-ignored)
Dockerfile                # Custom Airflow image
docker-compose.yml        # Docker Compose stack
requirements.txt          # Python dependencies
dags/                     # DAG definitions
  ├── dags.py             # Main DAG
  └── operators.py        # Custom operators
doc/                      # Documentation assets
```

## Getting Started

### 1. Configure Environment

```bash
cp .env.example .env
# Edit .env with your settings
```

### 2. Build & Start

```bash
docker-compose up -d --build
```

This will:
- Build the custom Airflow image
- Start PostgreSQL database
- Run database migrations (`airflow db migrate`)
- Start the Airflow webserver and scheduler

### 3. Access Airflow UI

Open [http://localhost:8080](http://localhost:8080) in your browser.

> **Note:** Airflow 3.x uses SimpleAuthManager by default — no login required.

### 4. Stop

```bash
docker-compose down
```

To also remove database volumes:
```bash
docker-compose down -v
```

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `POSTGRES_USER` | PostgreSQL username | `airflow` |
| `POSTGRES_PASSWORD` | PostgreSQL password | `airflow` |
| `POSTGRES_DB` | PostgreSQL database name | `airflow` |
| `MY_APP_SECRET` | Application secret | — |
| `AIRFLOW__DATABASE__SQL_ALCHEMY_CONN` | DB connection string | see `.env` |
| `AIRFLOW__CORE__FERNET_KEY` | Encryption key | see `.env` |
| `AIRFLOW__API__SECRET_KEY` | API secret key | see `.env` |

## Adding Dependencies

Add Python packages to `requirements.txt`, then rebuild:

```bash
docker-compose up -d --build
```

## Architecture

- **LocalExecutor**: Tasks run as subprocesses of the scheduler
- **PostgreSQL 15**: Metadata database
- **Webserver (api-server)**: Airflow UI and API
- **Scheduler**: DAG parsing and task scheduling
