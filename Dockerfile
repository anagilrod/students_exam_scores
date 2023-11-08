FROM python:3.11

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install

COPY src/ /app/src/
COPY deploy/ /app/deploy/

EXPOSE 8000

CMD ["sh", "deploy/run_app.sh"]
