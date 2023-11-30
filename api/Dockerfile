FROM python:3.11-bullseye

WORKDIR /api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "api.main:api", "--reload", "--host", "0.0.0.0", "--port", "8080"]
