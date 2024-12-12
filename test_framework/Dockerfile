FROM python:3.11-slim
RUN pip install poetry
WORKDIR /test_framework
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install
COPY . /test_framework
CMD ["pytest", "./tests", "-sv"]