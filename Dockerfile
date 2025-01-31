FROM python:3.10

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY app/ app/
COPY add_products.py /app/

RUN pip install --no-cache-dir poetry

RUN poetry install --no-root --no-interaction

EXPOSE 8000

CMD ["sh", "-c", "poetry run python add_products.py && poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"]