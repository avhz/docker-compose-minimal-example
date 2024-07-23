FROM    python:3.12-slim
RUN     python3.12 -m pip install --upgrade pip
RUN     python3.12 -m pip install duckdb polars dash gunicorn werkzeug
# EXPOSE  1995

CMD ["gunicorn", "server:server", "--reload", "--bind", "0.0.0.0:1995"]