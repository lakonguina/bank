FROM python:3.11-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /api

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY . .

RUN pipenv install --system

CMD ["uvicorn", "api.main:api", "--reload", "--host", "0.0.0.0", "--port", "8080"]
