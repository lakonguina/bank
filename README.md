# Get started
- Clone this repo
- Copy & rename `.env-template` to `.env` and fill it
- `docker compose up --build`

Head over `0.0.0.0:8080/docs` for documentation

# Command
- Purge & update sql schemas: `docker compose exec -it db bash "/usr/src/sql/purge.sh"`
- Import data into db: `docker compose exec -it db bash "/usr/src/sql/import.sh"`
- Launch tests: `pytest tests/*.py`
