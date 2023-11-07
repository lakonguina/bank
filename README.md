# Import schemas into database
`docker compose exec -i -T db psql -U test < sql/schemas/*.sql`
`docker compose exec -it db /bin/sh "/usr/src/sql/purge.sh"`

# Import csv data into database
`\copy countries '/usr/src/sql/data/prod/frontoffice/countries.csv' delimiter ',' csv header;`
