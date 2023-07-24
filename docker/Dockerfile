FROM python:3.10

RUN pip install pipenv

WORKDIR /app

COPY ./ ./
COPY Pipfile Pipfile.lock /app
RUN pipenv install


CMD ["pipenv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
