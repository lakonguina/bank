psql -U $POSTGRES_USER -d postgres <<EOF
DROP DATABASE frontoffice WITH (FORCE);
\i /usr/src/sql/schemas/frontoffice.sql


DROP DATABASE backoffice WITH (FORCE);
\i /usr/src/sql/schemas/backoffice.sql
EOF
