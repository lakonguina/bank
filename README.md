# FullStack Dockerized Project with FastAPI, Svelte, Local SMTP Server, Backoffice and PostgreSQL

## Overview

This is a full-stack web application. Docker for containerization, FastAPI for the API and Backoffice, Svelte for the frontend, Local SMTP and PostgreSQL as the database. The project is designed to provide a robust and scalable foundation for building modern full-stack web applications.

## Prerequisites

Make sure you have the following tools installed on your machine:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Node.js](https://nodejs.org/)
- [npm](https://www.npmjs.com/)
- [Python](https://www.python.org/)

## Get started
1. **Clone the repository:**
2. **Copy & rename `.env-template` to `.env` and fill it**
3. **`docker compose up --build`**

   
## Applications
- API (FastAPI): http://0.0.0.0:3000/docs
- Frontend (Svelte): http://0.0.0.0:7000
- Backoffice: http://0.0.0.0:8000
- SMTP: http://0.0.0.0:5000

## Command
- Purge & update sql schemas: `docker compose exec -it db bash "/usr/src/sql/purge.sh"`
- Import data into db: `docker compose exec -it db bash "/usr/src/sql/import.sh"`
- Launch tests: `pytest tests/*.py`
