FROM    python:3.12-slim
RUN     python3.12 -m pip install --upgrade pip
RUN     python3.12 -m pip install duckdb polars dash gunicorn
WORKDIR /app
EXPOSE  8001

CMD ["gunicorn", "app:server", "--bind", "0.0.0.0:8001", "--reload"]