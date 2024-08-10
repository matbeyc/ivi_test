FROM python:3.11-slim
RUN pip install poetry
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --no-dev
COPY . .
EXPOSE 8080
CMD ["python", "main.py"]