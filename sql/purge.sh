psql -U test <<EOF
DROP DATABASE frontoffice WITH (FORCE);

\i /usr/src/sql/schemas/frontoffice.sql
EOF
