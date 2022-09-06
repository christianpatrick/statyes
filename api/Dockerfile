FROM python:3.9-alpine

RUN apk update && apk upgrade
RUN apk add --no-cache gcc musl-dev libc-dev libc6-compat linux-headers build-base libffi-dev openssl-dev postgresql-dev

# Init environment
ENV PYTHON_ENV=development \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  POETRY_VERSION=1.1.14

# Install poetry
RUN pip install "poetry==$POETRY_VERSION"

# Copy reqs
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# No virtual environment needed
RUN poetry config virtualenvs.create false

# Install the project
RUN poetry install --no-interaction --no-ansi

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]