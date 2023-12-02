FROM python:3.11-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# This workdir for copy file and install
WORKDIR /app/api

# Install pipenv and compilation dependencies
RUN pip install pipenv

COPY . .

RUN pipenv install --system


# This workdir to launch app
WORKDIR /app/

CMD ["uvicorn", "api.main:api", "--reload", "--host", "0.0.0.0", "--port", "8080"]
